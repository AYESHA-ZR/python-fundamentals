# sorting practice
marks = [34,12,45,67,89,34,90,43,65,29]
# sorted(marks)
# → new sorted list return karta hai
# → original marks unchanged

# marks.sort()
# → original marks ko change karta hai
# → return value = None
acs = sorted(marks)
print("acsending marks is ",acs)

marks.sort()
print("sorted marks = ",marks)

dec = sorted(marks,reverse=True)
print("descending marks = ",dec)
