# expense tracker project 
expenses =[]
while True:
    try:
        num = int(input("Enter number of expenses.. = "))
        break
    except ValueError:  
         print("enter valid number for expenses....")
         
i = 1
while i<=num:
    exp = {}
    exp["category"] = input("category = ")
    while True:
        try:
             exp["amount"] = int(input("amount = "))
             break
        except ValueError:
             print("enter valid amount...")
        
    expenses.append(exp)
    i= i+1
print(expenses)

total =0
for i in expenses:
    total+=i["amount"]
    
print("...expenses...")
for expense in expenses:
    print(expense["category"]," : ",expense["amount"])
    print("total expense = ",total)