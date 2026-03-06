x = 5
print(type(x))

Name1 = "Pixl"
print(type(Name1))

Value = True
print(type(Value))

class Student:
    Num_Of_Students = 0
    def __init__(Self,Name, Age=0 , Courses="None"): #Default Atrributs ___
        Self.Name = Name                                                 # |
        Self.Age  = Age                                                  # |
        Self.Courses = Courses                                           # |
        Student.Num_Of_Students +=1                                      # |
                                                                         # |
    def describe(self):                                                  # |
        print(f"My name is: {self.Name} \n My age is: {self.Age}")       # |
                                                                         # |
Student_1= Student("Ali", 12, ["Math", "Chemistry"])                     # |
Student_2 = Student("Ali", 12, ["Math", "Chemistry"])                    # |
print(id(Student_1),"\n",id(Student_2))                                  # |
print(id(Student_1) == id(Student_2))                                    # |
Student_3 = Student("Ahmed")                                             # |
print(Student_3.Age,"\n",Student_3.Courses)                   #<<----------|
Student_4 = Student("Islam", 23, ["C++", "HTML"])
print(Student.Num_Of_Students) #4

Student_1.describe()

#########################################################################################################################################################################
                                                                # Encapsulation 
                                                                # Constructor
                                                                # Test                 
class BankAccountMangment:
    account_count = 0   
     
    def __init__(self , name , acc_number , balance):
        self.User_Name = name
        self.Account_Number = acc_number
        self.__Balance = 0
        BankAccountMangment.account_count += 1
    def get_Balance(self):
        return self.__Balance
    
    def Set_Balance(Self , Amount):
       if Amount  >= 0:
           Self.__Balance = Amount
       else:
           print("Balance cann't be negative!")
 
    def Deposit(Self , Amount):
        if Amount > 0:
            Self.__Balance = (Self.__Balance + Amount) 
            print(f"Deposited balance = {Amount} \nNew Balance ={Self.__Balance}")
        else:
            print("Amount must be positive!")

    def Withdraw(Self , Amount):
        if Self.__Balance >= Amount :
            Self.__Balance = (Self.__Balance - Amount)
            print(f"Withdrewed balance = {Amount}\nNew Balance = {Self.__Balance}")
        else:
            print("Sorry, Your Balance is not enough")    

    def __str__(self):
        return  f"User Name: {self.User_Name}\nAccount Number: {self.Account_Number}\nBalance: {self.__Balance}"

    def __len__(self):
        return len(self.account_number)

    def __eq__(self , other):
        self.account_number == other.account_number

@classmethod
def from_string(cls,data):
        name , acc_number , balance = data.split(",")
        return cls(name , int(acc_number) , int(balance))

@classmethod
def get_account_number(cls):
        return cls.account_count

@staticmethod
def validate_acc_number(account_number):
    return str(account_number).isdigit() and len(str(account_number)) == 6     

Acc1 = BankAccountMangment("M.SALAH" , "357592" , 1000)
print(Acc1)

Acc1.Deposit(300)

Acc1.Withdraw(200)

print("Your Balance: " , Acc1.get_Balance())

Acc1.Set_Balance(700)
print("Your New Balance: " , Acc1.get_Balance())

#print(BankAccountMangment.validate_acc_number(Acc1.Account_Number))
#########################################################################################################################################################################
                                                                # Inheritance
                                                                # Overriding
                                                                # Super
from datetime import date 
class person:

    def __init__(self , Name , Age):
        self.Name = Name
        self.Age = Age

    def display(self):
        return f"Your Name is: {self.Name}\nYour Age is: {self.Age}\n"
    
    @classmethod
    def initFromBirthYear(cls , Name , BirthYear , extra = None):
        from datetime import date
        currentYear = date.today().year
        Age = currentYear - BirthYear
        return cls(Name , Age , extra)
    
class MAN(person):
    Num_of_men = 0

    def __init__(self , Name , Age , Voice):
        super().__init__(Name , Age)
        self.voice = Voice
        MAN.Num_of_men += 1

    def display(self):
        string = super().display()
        return string + f"Your voice is: {self.voice}"
    
man1 = MAN("Ali" , 15 , "Hight")
print(man1.display()) 
print(MAN.Num_of_men)
man2 = MAN.initFromBirthYear("Ahmed" , 2000 , "Low")

class WOMAN(person):
    Num_of_woman = 0

    def __init__(self , Name , Age , Hair):
        super().__init__(Name , Age)
        self.hair = Hair
        WOMAN.Num_of_woman += 1

    def display(self):
        string = super().display()
        return string + f"Your Hair is: {self.hair}"
    
woman1 = WOMAN("Sara" , 15 , "Black")
print(woman1.display()) 
print(WOMAN.Num_of_woman)
print(person.display(man1))  
woman2 = WOMAN.initFromBirthYear("Mona" , 1995 , "Brown")
print(woman2.display())

print(isinstance(man1 , person))  
print(isinstance(woman1 , person))
##########################################################################################################################################################################
                                                                # Abstraction
from abc import ABC , abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):

    def sound(self):
        return "Woof Woof"

    def sleep(self):
        return "Dog is sleeping"
    
class Cat(Animal):

    def sound(self):
        return "Meow Meow"

    def sleep(self):
        return "Cat is sleeping"
    
dog1 = Dog()
print(dog1.sound())
print(dog1.sleep())
cat1 = Cat()
print(cat1.sound())
print(cat1.sleep())
##########################################################################################################################################################################
                                                                # Polymorphism
class English:
    def greet(self):
        return "Hello"
class Spanish:
    def greet(self):
        return "Hola"
class French:
    def greet(self):
        return "Bonjour"
    
def welcome_language(language):
    print(language.greet())
eng = English()
span = Spanish()
fr = French()
welcome_language(eng)
welcome_language(span)
welcome_language(fr)
##########################################################################################################################################################################
                                                                # Descriptors 
    
class SlugFromName:
    """Computes a slug from .name at access time."""
    def __get__(self, obj, owner):
        if obj is None:
            # Keep the example readable when accessed on the class:
            return "<SlugFromName descriptor>"
        name = getattr(obj, "name", "")
        return "-".join(name.lower().split()) or "<no-name>"

class EmailField:
    """Normalizes on set, then returns the stored value."""
    def __get__(self, obj, owner):
        if obj is None:
            return "<EmailField descriptor>"
        return obj.__dict__.get("_email", None)

    def __set__(self, obj, value):
        obj.__dict__["_email"] = value.strip().lower()

class User:
    slug = SlugFromName()
    email = EmailField()

u = User()
u.name = "Guido van Rossum"
u.slug = "custom-slug"
u.email = "USER@Example.COM"

print(u.slug, u.email, User.slug, User.email)
##########################################################################################################################################################################
                                                                # Basic Syntax

