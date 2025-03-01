# initiate a class 
class employee:
    # Special function / magic method / dunder method - constructor
    def __init__(self):
        
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"

    def travel(self,destination):
        print("Employee is now travelling to " + destination)

# create a object/instance of class employee
soumen = employee()
# print(soumen.id)
soumen.travel('durgapur')