name = input("please enter your name: ")

print(f"hello {name}")

number = input("how many times do you want to see your name? ")


int_number = int(number)

for counter in range(int_number):
	print(f"{name} {counter+1}")



