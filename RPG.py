#D- Random Password Generator
import random
def rgp(user_words, required_length, no_of_passwords):
	import random 
	generated_password = ""
	for n in range(no_of_passwords):
		generated_password = ""
		for i in range(required_length):
			g = random.randrange(len(user_words))
			generated_password += user_words[g]
		print("Password", n+1, "is:", generated_password)
def rgpuse():
  user_words = []
  user_words = input("Enter any word: ")
  required_length = int(input("Length of password you require: "))
  no_of_passwords = int(input("How many passwords do you require: "))
  r = rgp(user_words, required_length, no_of_passwords)		
