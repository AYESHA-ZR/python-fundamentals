#print numbers from 1 to 10 using while loop
n = 1
while n<=10:
    print(n)
    n = n+1
    
#Write a program that calculates the sum:
# 1 + 2 + 3 + ... + N
n = int(input("ENTER N = "))
i =1
TOTAL = 0
while i<=n:
    TOTAL = TOTAL+i
    i = i+1
print("total = ",TOTAL)