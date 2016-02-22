import .. _core as core
import Adafruit_DHT
import time


waitTime = 2
_instantiated = False

class Sensor(core.HardwareSensor):
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = pin
        self.value = {"humidity": 0, "temperature": 0}
    
        self.lastUpdate = time.time()
        
    def update(self):
        timeNow = time.time()
        if timeNow >= (self.lastUpdate + waitTime):
            self.lastUpdate = timeNow
        else:
            return 1
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            self.value["humidity"] = humidity
            self.value['temperature'] = temperature
            return 0
        else:
            return 1
            
    def read(self):
        return (self.value["humidity"], self.value["temperature"])
    
    
    if __name__ == "__main__":
        dht22 = Sensor(4)
        print dht22.update()
        print dht22.read()