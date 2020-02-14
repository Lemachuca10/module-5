#Luis Machuca
#02/13/2020

#this program gives you the numbers that are divible 3, 5 or both from 1 to 50
n = int(input("Type in a number:"))
for i in range(1,n +1): #Numbers from 1-50
	if i%3==0 and i%5==0: #If they are divisible by 3 and 5...
		print ("Both")
#Else if they are divisible by 3
	elif i%3==0: 
		print ("Disible by 3")
#Else if they are divisible by 5
	elif i%5==0:
		print ("Dibisible by 5")
	else:
		print(i)

#Else if none is disible by 3 or 5 print the number
		
             

