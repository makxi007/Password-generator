import string
from random import randint

punctuation = string.punctuation
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits

def formulate_easy(values):
	length = randint(5, 11)
	value = 0
	result = ""
	for i in range(length):
		value = randint(0, len(values) - 1)
		result += values[value]
	print(result)

def formulate_medium(values):
	length = randint(5, 17)
	value = 0
	result = ""
	for i in range(length):
		value = randint(0, len(values) - 1)
		result += values[value]
	print(result)

def formulate_strong(values):
	length = randint(5, 20)
	value = 0
	result = ""
	for i in range(length):
		value = randint(0, len(values) - 1)
		result += values[value]
	print(result)

print("Hello.\nThis is a password generator choose the password power: ")
print(
"""
1. Easy(only lower letters and digits)
2. Medium(lower, upper letters and digits)
3. Strong(lower, upper letters, digits and punctuation)
"""
)

password_power = int(input("Your choice -> "))

if ( password_power == 1 ):
	formulate_easy(lower_case+digits)
elif ( password_power == 2):
	formulate_medium(lower_case+upper_case+digits)
elif ( password_power == 3):
	formulate_strong(lower_case+upper_case+digits+punctuation)


