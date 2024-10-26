'''
A program that would disply values 10 to 1 using while loop
a terminating loop(
    1. initialization
    2. condition
    3. iteration
)
'''
from os import system

def main()->None:
    system("cls")
    i:int = 11 #initialization
    while i>1: #condition
        i-=1 #iteration (incremental/decremental)
        if i==5 or i==3:
            continue #skip 5 and 3 in the display
        print(i,end=" ") #operation
    else:
        print("\nloop ends...")
        
if __name__ == "__main__":
	main()