#Tip Calculator
print ("Welcome to the Tip Calculator!.\n")
Total_bill = float(input ("Enter the total bill? $"))
Tip_precent =int( input("Enter the tip precentage? "))
people=int( input("how many people will the bill be split 12?"))

amount=(Total_bill+(Total_bill*Tip_precent/100))/people
a="{:.2f}".format(amount)
print (f"Each person should pay: ${a}")



# 
# print("Welcome to the tip Calculator!")
# bill=float(input("\nWhat was the total bill? "))
# tip_percent=int(input("\nHow much tip would you like to give? 10,12, or 15? "))
# split=int(input("\nHow many people would split the bill? "))
# result=(bill+(bill*(tip_percent/100.0)))/split
# print(f"\nEach person should pay: ${round(result,2)}")