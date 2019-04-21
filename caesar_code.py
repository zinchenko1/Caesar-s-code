arr1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

arr2 = []

for i in range(len(arr1)):
	arr2.append(arr1[i]) 

def change_arr2():
	for i in range(key):
		arr2.append(arr2[0])
		arr2.remove(arr2[0])

print("1. Crypt")
print("2. Decrypt")

try:
	ans = int(input("\n# Make your choice > "))

	if ans==1:
		key = int(input("\n# Write the key [0-%s] > "%(str(len(arr1)))))

		change_arr2()

		msg=input("\n# Write the text > ")

		msgc=""
		for i in msg:
			for j in range(len(arr1)):
				if i==arr1[j]:
					msgc+=arr2[j]
		crypt=open("crypt.txt","w")
		print("\nYour encryption > "+msgc+"\n")
		crypt.write(msgc)
		crypt.close()

	elif ans==2:
		key = int(input("\n# Write the key [0-%s] > "%(str(len(arr1)))))

		change_arr2()

		decrypt_r=open("crypt.txt","r")
		read=decrypt_r.read()
		msgd=""
		for i in read:
			for j in range(len(arr1)):
				if i==arr2[j]:
					msgd+=arr1[j]
		print("\n# Decrypted > "+str(msgd))

	else:
		print("\nNumber is not DEFINED!\nPlease enter 1 or 2")

except ValueError:
	print("Error! Print only Integer numbers!")

	input("\nPress ENTER to exit")