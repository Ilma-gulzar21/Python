
class student:
        
    def __init__(self):
         self._name = ""
         self._roll_number = 0
         self._marks = 0

    def setter(self,_name,_roll_number,_marks):
        if _marks>0:
               self._marks=_marks
        else:
             print("Marks cannot be negative")

        if 1 <= _roll_number <= 100:
              self._roll_number = _roll_number 
        else:
             print("Roll number must be between 1 and 100")
             
        if _name != "":
                self._name=_name
        else:
             print("Name cannot be empty")


    def getter(self):
         print("name = ",self._name)
         print("roll Number = ",self._roll_number)
         print("marks = ",self._marks)


obj1 = student()

obj1.setter("Ilma", 25, 85)

obj1.getter()
         
             
       


