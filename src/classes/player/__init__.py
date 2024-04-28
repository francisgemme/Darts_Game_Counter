# import all Class methods as aliases, from the mainApps_functions directory;

class __init__:
    """
    Class representing a Player with all its attributes.

    Attributes:
        current_score (int): 

    """

    # Declare variables & types
    name = str('')
    current_score = int(0)
    doubleInVal = bool(False)
    
    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the mainApps_functions directory in separate .py files.
    # The name of the .py file and function must be the same in order to work properly

    def getPlayerScore(self):
        """
        A regular method that can access instance attributes.
        """
        return self.current_score
    
    def remScorePts(self, points):
        """
        A regular method that can access instance attributes.
        """
        self.current_score -= points
        return
    
    def editScorePts(self, editedScore):
        """
        A regular method that can access instance attributes.
        """
        self.current_score = editedScore
        return
    
    def getDoubleInVal(self):
        """
        A regular method that can access instance attributes.
        """
        doubleInVal = self.doubleInVal
        return doubleInVal   
    
    def setDoubleInVal(self, newVal):
        """
        A regular method that can access instance attributes.
        """
        self.doubleInVal = newVal
        return  