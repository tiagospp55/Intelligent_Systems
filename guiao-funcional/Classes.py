class Constant:

    def __init__(self):
        self.value = 73

    def __str__(self):
        return "value" + str(self.value)
    
class Variable:

    def __init__(self, value):
        self.x = value

    def __str__(self):
        return "x" + str(self.x)
