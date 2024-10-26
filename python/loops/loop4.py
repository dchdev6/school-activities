'''
	A program that would display the content of a list
	['hello',10,1.5,{'id':'0001'}]
'''
from os import system

def main()->None:
    mylist:list = ['hello',10,1.5,{'id':'0001'}]
    myname:str = "durano"
    system("cls")
    print(mylist)
    print(myname)
    for item in mylist:
        print(item)
    for c in myname:
        print(c,end=" ")

if __name__=="__main__":
	main()