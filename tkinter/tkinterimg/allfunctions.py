from value_manager import ValueManager

value1 = ValueManager()
picvalue = ValueManager()
value1.set("value")

def printvalue():
    print(value1.get())

def printvalue2():
    value1.set("value2")
    print(value1.get())