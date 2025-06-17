# Write your code below
n = 12

for i in range (1,n+1):
   # print (i)
    for j in range (n,0,-1):
        if i*j == n:
            print(f'{i} {j}')