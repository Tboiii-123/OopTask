class Person:
    
    def __init__(self,name,age,gender):
        self.name =name
        self.age =age
        self.gender =gender
    

    def intoduce(self):
        print(f'Welcome {self.name}')
        print(f'You are {self.age} years old')
        print(f'And your gender is {self.gender}')



obj =Person("Lawal",12,"Male")

obj.intoduce()
