# Class 
class Dog():
   def __init__(self, name, age, kind):
      self.name = name
      self.age = age
      self.kind = kind
   def sit(self, sit = False):
       if sit == True:
        return f"{self.name} oturur"
       else:
        return f"{self.name} oturmur"
   def roll_over(self, roll_over = False):
      if roll_over == True:
       return f"{self.name} fırlanır"
      else:
        return f"{self.name} fırlana bilmir"
my_dog = Dog('willie',6 , 'Golden retriwer') 
your_dog = Dog('Lucy', 4, 'Pitbull')
her_dog = Dog('Leslie', 5, 'Husky')
print(f"Mənim itimin adı {my_dog.name}dır.{my_dog.name}nin {my_dog.age} yaşı var. Onun cinsi {my_dog.kind}dır.{my_dog.sit(True)}, lakin {my_dog.roll_over(False)}. ")
print(f"Mənim itimin adı {your_dog.name}dır.{your_dog.name}nin {your_dog.age} yaşı var. Onun cinsi {your_dog.kind}dır.{your_dog.sit(False)}, lakin {your_dog.roll_over(True)}.")
print(f"Mənim itimin adı {her_dog.name}dır.{her_dog.name}nin {her_dog.age} yaşı var. Onun cinsi {her_dog.kind}dır.{her_dog.sit(True)} və {her_dog.roll_over(True)}. ")   
      
    