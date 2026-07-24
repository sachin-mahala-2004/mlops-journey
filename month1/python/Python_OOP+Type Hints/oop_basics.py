class Dog:
    pass 
dog1= Dog()
print(type(dog1))

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        print(f"{self.name} says: Woof! ")
        
    def describe(self):
        print(f"{self.name} is a {self.breed}, {self.age} years old")
        
#create object 
dog1 = Dog("Bruno","Labrador",3)
dog2 = Dog("Max", "Poodle", 5)
    
dog1.bark() 
Dog.bark(dog1)    #same as above

dog2.describe()

print(dog1.name)   #Bruno
print(dog2.age)    # 5

#----------------------------------------------------------
# Instance variables vs Class Variables
class Employee:
    #Class Variables - shared by All Instances
    Company_name = "God Speed"
    employee_count = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
        Employee.employee_count+=1
        
    def show(self):
        #Access both
        print(f"{self.name} works at {self.Company_name}, salary: {self.employee_count}")
        
e1 = Employee("Alice", 94000)
print(e1.employee_count)
e2 = Employee("Jhon", 75000)
print(e2.employee_count)

e1.show()
e2.show()

print(f"Employee Count: {Employee.employee_count}")
print(f"Company Name: {Employee.Company_name}")

Employee.Company_name = "God's Speed"
print(f"Company Name: {Employee.Company_name}")


#---------------------------------------------------------
# Private and Protected Attributes 

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        #public - anyone can access
        self._type = "Savings"    #protected - convention: don't access outside class
        self.__balance = balance  #private - name-mangled, hard to access outside
        
    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            
    def get_balance(self):      #controlled access to private attributes 
        return self.__balance

account = BankAccount("Joe",85000)

print(account.owner)
print(account._type)     #works but convention says don't 
# print(account.__balance)    #AttributeError - cannot access directly 
print(account._BankAccount__balance)   #Works but don't do this 
print(account.get_balance())

