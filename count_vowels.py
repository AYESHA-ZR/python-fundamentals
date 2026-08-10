# count vowels from the string
s = input("enter a string:")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count +=1
        
print("vowels in a string = ",count)