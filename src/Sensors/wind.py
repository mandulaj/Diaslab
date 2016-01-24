import _core as core

SPEED_DEFAULT_OPTIONS = {

}
DIRECTION_DEFAULT_OPTIONS = {

}



class SensorSpeed(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(SPEED_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
        
class SensorDirection(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(DIRECTION_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    

if __name__ == "__main__":
    windSpeed = SensorSpeed()
    windDirection = SensorDirection()
    print windSpeed.getValue()
    print windDirection.getValue()