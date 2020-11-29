name = input("please enter your name: ")
number_limit = 10

print(f"hello {name}")

input_number = input(f"how many times do you want to see your name? (no more than {number_limit}) ")


int_number = int(input_number)

if int_number>number_limit:
	print(f"the bnumer {input_number} is too big, it is higher than {number_limit}")
	exit()

for counter in range(int_number):
	print(f"{name} {counter+1}")


