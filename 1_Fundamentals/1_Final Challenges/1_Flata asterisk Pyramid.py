# Each test case has one input - an odd whole number (always odd, given).
# Your task is to print n - pyramid using *, here are some examples:


n = int(input())

for i in range(n+1):
    if i %2 != 0:
        print((i)*"*")

###############################################################
n = int(input())
rows = int(n/2)+1
for i in range(rows):
    stars = ""
    stars += "*"*(2*(i+1)-1)
    print(stars)