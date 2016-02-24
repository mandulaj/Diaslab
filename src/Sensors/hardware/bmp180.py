import _core as core
import time


DEFAULT_OPTIONS = {
  "maxupdate":2
}


_instantiated = False

class BMP180(core.HardwareSensor):
    def __init__(self, pin, options={}):
	self.options = core.mergeOptions(options, DEFAULT_OPTIONS)
        self.pin = pin
        self.value = {"pressure": 0, "temperature": 0}
    
        self.lastUpdate = time.time()
        
    def update(self):
        timeNow = time.time()
        if timeNow >= (self.lastUpdate + self.options["maxupdate"]):
            self.lastUpdate = timeNow
        else:
            return 1
            
    def read(self):
        return (self.value["pressure"], self.value["temperature"])
    
    
    if __name__ == "__main__":
        bmp180 = BMP180(4)
        print bmp189.update()
        print bmp180.read()
