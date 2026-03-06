
print("Hello sir! What would you like to drink ?")
type_of_drink = input("(cold drink , soft drink)\n Choose a drink?\n")

if type_of_drink == "soft drink":
    print("Nice!")
    type_of_soft_drink = input(" tea or coffee,please ?\n")
    if type_of_soft_drink == "tea":
        print("Good choice!")
        color_of_tea = input("red or green tea sir?\n")
        if color_of_tea == "red":
            print("Thank you for waiting sir \n Here your red Tea sir")
        elif color_of_tea == "green":
            print("Thank you for waiting sir \n Here your green Tea sir")
        else:
            print("Sorry")    
    elif type_of_soft_drink == "coffee":
        print("good choice!")
        type_of_coffe = input("Nescafe or black tea sir?\n")
        if type_of_coffe == "Nescafe":
            print("Thank you for waiting sir \n Here your Nescafe sir")
        elif type_of_coffe == "black":
            print("Thank you for waiting sir \n Here your Black coffe sir")
        else:
            print("Sorry")             
elif  type_of_drink == "cold drink":
        print("Nice")
        type_of_cold_drink = input("ice cream or juicie,please?\n")  
        if type_of_cold_drink == "ice cream":
            print("Good choice!")
            Flavor = input("Which flavor sir?\n")
            print("Thank you for your waitting sir, Here your" ,Flavor, "ice cream sir")
        elif type_of_cold_drink == "juicie":
             print("Good choice!")
             Flavour = input("Which flavor sir?\n")
             print("Thank you for your waitting sir, Here your" ,Flavour, "juicie sir")
        else:
            print("Sorry")    
else:
    print("Sorry")            