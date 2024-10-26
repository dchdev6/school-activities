'''
	A program that display 1 to 10 using for loop
'''
from os import system
def main()->None:
    system("cls")
    for i in range(1,11,+2):
        #if i==5 or i==7: continue
        print(i,end=" ")

if __name__ == "__main__":
	main()