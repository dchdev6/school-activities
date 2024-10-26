'''
LOOP - a programming construct that repeats certain line of codes in program, until a condition is meet

Python loops
--------------
1. while-else
2. for
3. nested loop - loop within a loop
4. list comprehension

Example:
An endless loop program that terminates only when a key pressed
'''
from os import system

def main()->None:
    system("cls")
    while True: #endless loop
        k:str = input("Press a key to terminate...")
        if k:
            print("loop is terminated...")
            break
        

if __name__=="__main__":
    main()
    
    
    
    





