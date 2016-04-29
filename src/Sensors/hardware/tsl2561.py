import _core as core
import time
import Adafruit_GPIO.I2C as I2C
import threading


DEFAULT_OPTIONS = {
  'maxupdate' : 2,
  'address':
}


_instantiated = False

class TSL2561(core.HardwareSensor):
    def __init__(self, pin, options={}):
	self.options = core.mergeOptions(DEFAULT_OPTIONS, options)

        self.pin = pin
        self.value = {"": 0, "": 0}

        self.lastUpdate = time.time()

    def update(self):
        timeNow = time.time()
        if timeNow >= (self.lastUpdate + self.options["maxupdate"]):
            self.lastUpdate = timeNow
        else:
            return 1


    def read(self):
        return (self.value[""], self.value[""])


if __name__ == "__main__":
    tsl = TSL2561()
    time.sleep(1)
    print tsl.update()
    print tsl.read()
