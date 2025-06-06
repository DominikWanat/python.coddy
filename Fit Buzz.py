print("Welcome to FizzBuzz!")

a = 35 +1 ##int(input())

def fizzbuzz (a):
    if a% 3 ==0 and a %7==0:
        print("FizzBuzz")
    elif a %3 == 0:
        print("Fizz")
    elif a %7 ==0:
        print("Buzz")
    elif '3' in str(a):
        print("Almost Fizz")
    else:
        print(a)
for i in range(1,a):
    fizzbuzz(i)