class people:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(f"{self.name}")


obj = people("Kunal")
obj.display()


def addition(a,b):
    return a+b

def multiplicaiton(a,b):
    return a*b