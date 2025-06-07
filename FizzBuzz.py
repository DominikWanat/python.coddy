print("Welcome to FizzBuzz!")

##a = int(input())
a=7

def fizzbuzz (a):
    if a% 3 ==0 and a %7==0:
        print("FizzBuzz")
    elif a %3 == 0:
        print("Fizz")
    elif a %7 ==0:
            print("Buzz")
    else:
        print(a)

for i in range(1,a+1):
    fizzbuzz(i)