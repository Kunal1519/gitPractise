#main program

class people:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(f"{self.name}")


def addition(a,b):
    print(a+b)
    return a+b

def multiplicaiton(a,b):
    return a*b

def division(a,b):
    return a/b

def data(a,b):
    print(a,b)