 #Write a program that gets one input, a number. The input number indicates how many times to execute the below function. 
#Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.



#int(input())
n=5

def pepe():
    num = 0
    for i in range (10001):
        num += i
    print (num)

for j in range (1,n+1):
    pepe()