import _core as core

UV_DEFAULT_OPTIONS = {

}

IR_DEFAULT_OPTIONS = {

}

VISIBLE_DEFAULT_OPTIONS = {

}

class SensorUV(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(UV_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
        
class SensorIR(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(IR_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
        
class SensorVisible(core.GeneralSensor):
    def __init__(self, options={}):
        self.active = True
        self.options = core.mergeOptions(VISIBLE_DEFAULT_OPTIONS, options)
    
    def getValue(self):
        return 0
    




if __name__ == "__main__":
    luminosityUV = SensorUV()
    luminosityIR = SensorIR()
    luminosityVisible = SensorVisible()
    print luminosityUV.getValue()
    print luminosityIR.getValue()
    print luminosityVisible.getValue()