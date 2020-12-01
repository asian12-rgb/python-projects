with open('data.txt') as f:
	lines = f.readlines()

currencyDict = {}
for line in lines:
	parsed = line.split("\t")
	

amount = float(input("Enter amount:\n"))
print("enter the name of the currency you want to convert this amount to? Available options:\n")
[print(item) for item in currencyDict.keys("")]
currency = input("please enter one of these Values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
