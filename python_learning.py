# ates = "test"
# print ("\n"+ ates + "\n")
# print ("Hello " + input("What is your name?") + "!")

# str1= input("\n\nEnter your string to caluclate its length: ")
# print("\n Length of "+str1+ " is " + str(len(str1)))  


# Subscripting
# print ("hello"[0])
# print ("hello"[-1])

#type check
# print(type("Test"))
# print(type(123))
# print(type(12.341))
# print(type(True))

#Sum of 2 numbers
# t1= input("Enter a number")
# t2= input("\nEnter another number")

# t3=int(t1)+int(t2)

# print ("Sum of number is "+ str(t3))


#Tip Calculator
# 
# print("Welcome to the tip Calculator!")
# bill=float(input("\nWhat was the total bill? "))
# tip_percent=int(input("\nHow much tip would you like to give? 10,12, or 15? "))
# split=int(input("\nHow many people would split the bill? "))
# result=(bill+(bill*(tip_percent/100.0)))/split
# print(f"\nEach person should pay: ${round(result,2)}")

#Even Odd Number using If constarint
# number = int(input("Enter a number: "))

# if (number % 2 == 0):
#      print (f"{number} is an Even number.") 
# else:
#      print (f"{number} is an Odd number.")

#Ticketing system for a rollercoster

print("\nWelcome to the Rollercoster!\n") 
age = int(input("Enter your age: ")) 
height = int(input("Enter your height: ")) 
bill=0
if (height > 120):
    print("You can ride it!")
    if (age < 12):
        bill= 5
        print("Child Tickets are $5")
    elif (age >= 18):
        bill= 12
        print("Adult Tickets are $12")
    else:
        bill= 7
        print("Youth Tickets are $12")
    photo = input("Want to make the ride memorable with a photograph? Type yes or no.  ")
    if (photo=="yes"):  
        bill += 3
    print(f"Your Final Bill is ${bill}")
else:
    print("Sorry, your height doesn't meet the eligibility to take the ride.")
