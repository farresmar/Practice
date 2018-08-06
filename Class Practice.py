class FirstClass:
    a = 1 #Classes property
    b = 2 #Classes property

object1 = FirstClass() #Creates an object by making a variable = the class
object2 = FirstClass()
object3 = FirstClass().a #restricts object to just one of the classes variables
print(object1.a)
print(object2.b)
num = object1.a + object2.b
print(num)
#Object can equal any of the classes properties
print(object1.b)
print(object3)



#Real use of a class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = self.name + " is a " + self.color + " " + self.kind + " worth " + str(self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

        
