import string
from random import randint

punctuation = string.punctuation
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
is_special_w = False
password = ""

def formulate_easy(values, special):
	length = randint(5, 11)
	value = 0
	result = ""
	if ( special == "no" ):
		for i in range(length):
			value = randint(0, len(values) - 1)
			result += values[value]
		
	else:
		for i in range(length):
			value = randint(0, len(values) - 1)
			result += values[value]
		value = randint(0, len(result) - 1)
		result = result[:value] + special + result[value+1:]

	return result


def formulate_medium(values, special):
	length = randint(5, 17)
	value = 0
	result = ""
	if ( special == "no" ):
		for i in range(length):
			value = randint(0, len(values) - 1)
			result += values[value]
	else:
		for i in range(length):
			value = randint(0, len(values) - 1)
			result += values[value]
		value = randint(0, len(result) - 1)
		result = result[:value] + special + result[value+1:]
	print(result)

def formulate_strong(values, special):
	length = randint(5, 20)
	value = 0
	result = ""
	if special == "no":
		for i in range(length):
			value = randint(0, len(values) - 1)
			result += values[value]
	else:
		for i in range(length):
			value = randint(0, len(values) - 1)
			result += values[value]
		value = randint(0, len(result) - 1)
		result = result[:value] + special + result[value+1:]

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
print("Special word or words? If not just type 'space'")
special_w = list(map(str, input("Word(s) -> ").split()))
if ( len(special_w) != 0 ):
	is_special_w = True
print(special_w)

if ( password_power == 1 ):
	if is_special_w:
		password = formulate_easy(lower_case+digits, "_".join(special_w))
	else:
		password = formulate_easy(lower_case+digits, "no")
elif ( password_power == 2):
	if is_special_w:
		password = formulate_medium(lower_case+upper_case+digits, "_".join(special_w))
	else:
		password = formulate_medium(lower_case+upper_case+digits, "no")
elif ( password_power == 3):
	if is_special_w:
		password = formulate_strong(lower_case+upper_case+digits+punctuation, "_".join(special_w))
	else:
		password = formulate_strong(lower_case+upper_case+digits+punctuation, "no")

print(password)

input()