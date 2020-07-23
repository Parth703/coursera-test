def palindrome(n):
	for i in range(int(len(n)/2)):
		if n[i] != n[len(n)-i-1]:
			return False
	return True

def paliis():
  print("Program to check if a number or string is a Palindrome")
	n = input("Enter Number or String: ")
	p = palindrome(n)
	if p :
		print("It is a Palindrome!")
	else:
		print("It is not a Palindrome!")
