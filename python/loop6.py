'''
	A program that would display the content of a list
	['1','2','3','4','5']
'''
from os import system
def main()->None:
    mylist:list = ['1','2','3','4','5']
    system("cls")
    #for item in mylist:  print(item)
    #list comprehension
    [print(item,end=" ") for item in mylist if item !='3']

if __name__=="__main__":
	main()