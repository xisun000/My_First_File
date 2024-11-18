# 1 x 2 x 3 x …… x n

n = int(input ("enter the last number : "))
sum = 1
for x in range (1,n+1,1):
    sum = sum * x
    print(sum)