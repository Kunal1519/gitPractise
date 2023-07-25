class people:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(f"{self.name}")


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


def addition(a,b):
    return a+b

def multiplicaiton(a,b):
    return a*b