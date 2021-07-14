while True:
	def check(n):
		while n!=1 and n!=4:
			a=0
			while n:
				r=n%10
				a+=r*r
				n//=10
			n=a
		if n==1:
			print("Happy number")
		else:
			print("Unhappy number")
	def Happy_number(p,q):
		if p>q:
			p,q=q,p
		for n in range(p,q+1):
				t=n
				while n!=1 and n!=4:
					a=0
					while n:
						r=n%10
						a+=r*r
						n//=10
					n=a
				if n==1:
					print(t)
	def Unhappy_number(p,q):
		if p>q:
			p,q=q,p
		for n in range(p,q+1):
				t=n
				while n!=1 and n!=4:
					a=0
					while n:
						r=n%10
						a+=r*r
						n//=10
					n=a
				if n==4:
					print(t)
	print("Check or Range \nType 'C' or 'Check' to check the number Happy or Not happy\nType 'R' or 'Range' for happy or not happy numbers for given range")
	t=input()
	if t in "checkCheck":
		n=int(input("Enter the number:"))
		check(n)
	elif t in "Rangerange":
		print('Do you want happy numbers or not happy numbers?\nFor happy type "Happy numbers" or "Happy number" or "Happy" or "happy number" or "happy" or "H" or "h"\nFor not happy numbers type "Unhappy numbers" or "Unhappy number" or "Unhappy" or "unhappy number" or "unhappy" or "Un" or "un" ')
		a=input()
		if a in "Happy numbershappy numbers":
			p,q=map(int,input("Enter rangye: ").split())
			Happy_number(p,q)
		elif a in "Unhappy numbersunhappy numbers":
			p,q=map(int,input("Enter range: ").split())
			Unhappy_number(p,q)
	elif t=="break" :
		break