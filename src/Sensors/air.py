import _core as core

CO_DEFAULT_OPTIONS = {

}

CO2_DEFAULT_OPTIONS = {

}

MQ135_DEFAULT_OPTIONS = {

}

MQ3_DEFAULT_OPTIONS = {

}

class SensorCO(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(CO_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    
class SensorCO2(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(CO2_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    
class SensorMQ135(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(MQ135_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    
class SensorMQ3(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(MQ3_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    




if __name__ == "__main__":
    gasCO = SensorCO()
    gasCO2 = SensorCO2()
    gasMQ135 = SensorMQ135()
    gasMQ3 = SensorMQ3()
    print gasCO.getValue()
    print gasCO2.getValue()
    print gasMQ135.getValue()
    print gasMQ3.getValue()