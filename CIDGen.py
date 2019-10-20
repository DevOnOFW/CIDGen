import sys, time
from colorama import Fore, Back, Style
from colorama import init
init()

#So now we will start with the actual coding of the project. First ill save it so you can see nice colors :fa:

print(Fore.GREEN + "=" * 17)
print(Fore.MAGENTA + "Mr.ION CID Generator")
print("Subscribe: http://Youtube.Com/User/MultiBrute Leader")
print(Fore.GREEN + "=" * 17)

#Now this is where we will input the data for it to generate a console ID
#Sorry, had to find a base of a CID

a = input("Input a number <1-9> ONLY: ")
b = input("Input a number <1-9> ONLY: ")
c = input("Input a number <1-9> ONLY: ")
d = input("Input a number <1-9> ONLY: ")
a = str(a)
b = str(b)
c = str(c)
d = str(d)

#The last part of that converts the integers to strings :)

cidbase = str("00000001008766A39D091E82DCB8") #this also has to be a string, i almost forgot

if len(cidbase + a + b + c + d) > 32:
	print(Fore.RED + "Cannot Output ID")
	time.sleep(5)
	sys.exit()
else:
		print("\n" + Fore.MAGENTA + cidbase + a + b + c + d + Fore.WHITE + "\n")
		print("Closing In 15 Seconds!\nPrinting The ID And Outputting To CID.txt")
		with open('CID.txt', 'a') as output:
			output.write(cidbase + a + b + c + d)
			output.close()
		time.sleep(15)
		sys.exit()

		"""


		Thats basically it! And To Test It, Just Run It Really Quick!
		Ill be including the source and the compiled code in the description. 
		Subscribe for more!




		"""