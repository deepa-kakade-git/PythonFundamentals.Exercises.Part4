from random import randint

def get_numint(): # get a number from user
	user_num =input("Enter a number between 1 and 10 : ")
	return int(user_num)


def generate_random_num(): # generate a random number
	random_num=randint(1, 10)
	return random_num


def checknum(random_num): #user_num):  # check if the users guess is correct
	while True:
		user_num = get_numint()
		if user_num > random_num:  # display too high if user's number is greater than random number
			print("too high")
		elif user_num < random_num:   # display too low if user's number is greater than random number
			print("too low")
		else:
			print("correct")
			break


#random_number = generate_random_num()
checknum(generate_random_num())#,get_numint())

#checknum(generate_random_num(), user_num)
#print("The random number that was generated : "  + str(generate_random_num()))
#generate_random_num()
#print("the user's guess : " + str(user_num))
