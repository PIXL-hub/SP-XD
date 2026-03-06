                                                    #بسم الله الرحمن الرحيم#
 ###############################################################################################################################################                                                   
                                                             #Test
Name1 = "ahamed"
Name2 = "mohamed"
Age1 = 25 
Age2 = 30
print(f"Name is: {Name1} and Age is: {Age1} \n Name is: {Name2} and Age is: {Age2}")
print("Name is" + Name1)

################################################################################################################################################
                                                            #Function                                                            
def demo():
    print('my name is M.salah')
demo()    

def function(KeyOne,KeyTow):
    print("KeyOne for Ahmed is:",KeyOne ,"\n KeyTow for mohamed is:",KeyTow)
function(20,50)

def info(name):
    return f"Youer name is: {name}"
print(info("M.SALAH"))
###################################################################################################################################
                                                         #input
Name = input("Enter Your Name :")
Age = int(input("Enter Your Age: "))
Gpa = float(input("Enter Your Gpa: "))

print('Your Name is : '+ Name)                                                         
print('Your Age is : '+str(Age))
print('Your Gpa is :'+str(Gpa))

################################################################################################################################################
                                                          #list
list = ['ali','mohammed','ahamed']
print(list[1])
list.clear()
print(list)
list.insert(0,'max')
print(list)
################################################################################################################################################
                                                         #Tuple
tuple = ('korea','china','japan')
print(tuple[0])

################################################################################################################################################
                                                        #Dictionary
User = {'Name' : 'M.SALAH' , 'Age' : '25' }
print(User['Age'])

################################################################################################################################################
                                                       #Class
class Data:
    def zero():
        print('My Name Is Ali')
        Users  = 'Ali'
        Age = '70'
        print(f'Your Name Is:{Users} \n Youer Age Is:{Age}')
Data.zero()        
       
class index:
    def __init__(self,grade,agee):
        self.grade = grade
        self.agee = agee
    def result(self):
        return f"My Grade is:{self.grade}\n,My age is:{self.agee}"
Myinformtion = index( 8 , 18)         
print(Myinformtion.result())

###############################################################################################################################################
                                                    #For in
word = "Python"
for number in word:
    print(number)

for i in range(2):
    print(i)

for i in range(1,11):
        print(i)

###############################################################################################################################################        
                                                    #While
i = 5
while i<=15:
     print(i)
     i+=1                                                    
################################################################################################################################################

