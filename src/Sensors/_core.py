## The core sensor class
#
# This class is used as the base for all sensors and defines a common interface.

def mergeOptions(defaults, options):
    """Returns a dictionary where options are merged into the defaults""" 
    merged_options = defaults.copy()
    for key, val in options.iteritems():
        if key in merged_options:
            merged_options[key] = val
    return merged_options
        
    

DEFAULT_OPTIONS = {
    'interval': 0,
    'unit': "s"
}


class GeneralSensor(object):
    """A general super class used to define the interface for a sensor"""
    
    def __init__(self, options={}):
        self.active = True
        self.options = mergeOptions(DEFAULT_OPTIONS, options)
    
    def setupSensor(self):
        pass
    
    def getValue(self):
        """Returns the current value of the sensor"""
        pass
        
    def activate(self):
        """If implemented, wakes sensor form a sleap mode in order to take a reading"""
        self.active = True
    
    def deactivate(self):
        """If implemented, puts sensor to sleap in order to save power"""
        self.active = False
        
    def getOptionValue(self, option):
        """Returns the value of the option"""
        return self.options[option]
    
    def setOptionValue(self, option, value):
        """Sets the value for the option"""
        self.options[option] = value

class HardwareSensor(object):
    """Lowlevel class used to interface with a hardware sensor"""
    
    def __init__(self, options={}):
        self.active = True
        self.options = mergeOptions(DEFAULT_OPTIONS, options)
    
        