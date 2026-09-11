# calculate area of rectangle using functions

def area(Length,width):
    area_R = Length*width
    return area_R

# outside the function

leng = int(input("length = "))
wid = int(input("width = "))
print(area(leng,wid))

# defualt argument
def calculate_discount(price, discount=10):
    discount_amount = price*discount / 100

    final_price = price - discount_amount
    return final_price


Price = int(input("enter price = "))
disc = int(input("enter discount = "))
print("discounted price = ",calculate_discount(Price,disc))

Price =int(input("enter price = "))
print("discounted price = ",calculate_discount(Price))
