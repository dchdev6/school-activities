'''
	multiplication table
	--------------------
	A program that would accept a positive integer value not greater than 20, which represents th arow and column of the multiplication table matrix
'''
from os import system
def main()->None:
    system("cls")
    print("multiplication table")
    print("-"*80)
    try:
        n:int = int(input("Enter matrix size(n):"))
        if n>0 and n<=20:
            for i in range(1,n+1): #outer loop
                for j in range(1,n+1): #inner loop
                    print(f"{(i*j):4}",end=" ")
                print() #move to next line of the matrix
        else:
            print("Accept only 1 to 20")
    except:
        print("Invalid Input")
    
    
if __name__=="__main__":
	main()