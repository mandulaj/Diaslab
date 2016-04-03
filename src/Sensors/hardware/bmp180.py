import _core as core
import time
import Adafruit_GPIO.I2C as I2C
import threading

DEFAULT_OPTIONS = {
  "maxupdate":2,
  "address": 0x77
}

BMP180_REG_CONTROL = 0xF4
BMP180_REG_RESULT = 0xF6

BMP180_COMMAND_TEMPERATURE = 0x2E
BMP180_COMMAND_PRESSURE0 = 0x34
BMP180_COMMAND_PRESSURE1 = 0x74
BMP180_COMMAND_PRESSURE2 = 0xB4
BMP180_COMMAND_PRESSURE3 = 0xF4


_instantiated = False

class BMP180(core.HardwareSensor):
    def __init__(self, options={}):
        self.options = core.mergeOptions(DEFAULT_OPTIONS, options)
        self.device = I2C.get_i2c_device(self.options["address"])

        self.valueLock = threading.Lock()
        self.value = {"pressure": 0, "temperature": 0}
        self.lastUpdate = time.time()

        self._setup()

    def _setup(self):
        C1 = float(self.device.readS16BE(0xAA))
        C2 = float(self.device.readS16BE(0xAC))
        C3 = float(self.device.readS16BE(0xAE))
        C4 = float(self.device.readU16BE(0xB0))
        C5 = float(self.device.readU16BE(0xB2))
        C6 = float(self.device.readU16BE(0xB4))
        B1 = float(self.device.readS16BE(0xB6))
        B2 = float(self.device.readS16BE(0xB8))
        Mb = float(self.device.readS16BE(0xBA))
        Mc = float(self.device.readS16BE(0xBC))
        Md = float(self.device.readS16BE(0xBE))

        self._calibration = {
            "c3": 160 * pow(2,-15) * C3,
            "c4": pow(10,-3) * pow(2,-15) * C4,
            "c5": (pow(2,-15) / 160.0) * C5,
            "c6": C6,
            "b1": 160**2 * pow(2,-30) * B1,

            "mc": (pow(2,11) / (160.0**2)) * Mc,
            "md": Md / 160.0,

            "x0": C1,
            "x1": 160 * pow(2,-13) * C2,
            "x2": 160**2 * pow(2,-25) * B2,

            "p0": (3791 - 8)/1600.0,
            "p1": 1 - 7357 * pow(2,-20),
            "p2": 3038*100*pow(2,-36)
        }
        self._calibration["y0"] = self._calibration["c4"] * pow(2,15)
        self._calibration["y1"] = self._calibration["c4"] * self._calibration["c3"]
        self._calibration["y2"] = self._calibration["c4"] * self._calibration["b1"]


    def update(self):
        timeNow = time.time()
        if timeNow >= (self.lastUpdate + self.options["maxupdate"]):
            self.lastUpdate = timeNow
        else:
            return 1

        self._readThread = threading.Thread(group=None, target=self._read)
        self._readThread.start()
        return self._readThread

    def _read(self):
        self.device.write8(0xF4, 0x2E) #Get temperature
        time.sleep(0.5)
        UT = self.device.readList(0xF6, 2)
        self.device.write8(0xF4, 0xF4) #Get temperature
        time.sleep(0.5)
        UP = self.device.readList(0xF6, 3)

        UT = (UT[0] * 256.0) + UT[1]
        UP = (UP[0] * 256.0) + UP[1] + (UP[2]/256.0)


        X1 = (UT- self._calibration["c6"]) * self._calibration["c5"]
        Temperature = X1 + (self._calibration["mc"] / (X1 + self._calibration["md"]))

        s = Temperature - 25
        x = self._calibration["x2"] * s**2 + self._calibration["x1"] * s + self._calibration["x0"]
        y = self._calibration["y2"] * s**2 + self._calibration["y1"] * s + self._calibration["y0"]

        z = (UP - x)/y
        Pressure = self._calibration["p2"] * z**2 + self._calibration["p1"] * z + self._calibration["p0"]

        self.valueLock.acquire()
        self.value["pressure"] = round(Pressure,3)
        self.value["temperature"] = round(Temperature,2)
        self.valueLock.release()



    def read(self):
        self.valueLock.acquire()
        data = (self.value["pressure"], self.value["temperature"])
        self.valueLock.release()
        return data


if __name__ == "__main__":
    bmp180 = BMP180()
    time.sleep(2)
    bmp180.update()
    time.sleep(3)
    print bmp180.read()
