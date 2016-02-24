import _core as core
import time


DEFAULT_OPTIONS = {
  "maxupdate":2
}


_instantiated = False

class SI1145(core.HardwareSensor):
    def __init__(self, pin, options={}):
	self.options = core.mergeOptions(options, DEFAULT_OPTIONS)
        self.pin = pin
        self.value = {"uv": 0, "ir":0,"light":0, "temperature": 0}
    
        self.lastUpdate = time.time()
        
    def update(self):
        timeNow = time.time()
        if timeNow >= (self.lastUpdate + self.options["maxupdate"]):
            self.lastUpdate = timeNow
        else:
            return 1
            
    def read(self):
        return (self.value["uv"], self.value["ir"], self.value["light"], self.value["temperature"])
    
    
    if __name__ == "__main__":
        si = SI1145(4)
        print si.update()
        print si.read()
