import _core as core
import Adafruit_DHT
import time


DEFAULT_OPTIONS = {
  'maxupdate' : 2
}


_instantiated = False

class DHT22(core.HardwareSensor):
    def __init__(self, pin, options={}):
	self.options = core.mergeOptions(DEFAULT_OPTIONS, options)
        self.sensor = Adafruit_DHT.DHT22
        self.pin = pin
        self.value = {"humidity": 0, "temperature": 0}

        self.lastUpdate = time.time()

    def update(self):
        timeNow = time.time()
        if timeNow >= (self.lastUpdate + self.options["maxupdate"]):
            self.lastUpdate = timeNow
        else:
            return 1
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            self.value["humidity"] = round(humidity,2)
            self.value['temperature'] = round(temperature,2)
            return 0
        else:
            return 1

    def read(self):
        return (self.value["humidity"], self.value["temperature"])


if __name__ == "__main__":
    dht22 = DHT22(4)
    for i in range(100):
	time.sleep(2)
    	print dht22.update()
    	print dht22.read()
