import _core as core

DEFAULT_OPTIONS = {

}

class Sensor(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    

if __name__ == "__main__":
    rain = Sensor()
    print rain.getValue()