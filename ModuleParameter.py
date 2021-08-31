class ModuleParameter:
    parameterName = ""
    parameterValue = ""

    def __init__(self, name):
        self.parameterName = name
        f = open("/sys/module/leetmouse/parameters/" + self.parameterName, "r")
        self.parameterValue = f.read()

    def set(self, val):
        self.parameterValue = val
        f = open("/sys/module/leetmouse/parameters/" + self.parameterName, "w")
        f.write(self.parameterValue)
        f.close()