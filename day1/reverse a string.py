#reversed a string
s = input("enter a string = ")

index= -1
rev = ""
for i in s:
    rev = rev+s[index]
    index=index-1
print(rev)
   
   # reversed_s = s[::-1]
# print(reversed_s)