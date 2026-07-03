from logging import exception

# Count and print the number of lines in a file.

# count = 0
#
# with open('test.txt', 'r') as reader:
#     for line in reader:
#         count += 1
# print("total no of lines",count)
#
#########################################################################################################3

# ItemsInCart = 0
#
# def add_to_cart(items_to_add):
#     global ItemsInCart
#     if items_to_add < 0:
#         raise Exception("Cannot add a negative number of items")
#     if items_to_add + items_to_add > 5:
#         raise Exception("Cart limit exceeded")
#
#     ItemsInCart += items_to_add
#     print(f"{items_to_add} items added. Total in cart:{ItemsInCart}")
#
#
# try:
#     add_to_cart(2)
#     add_to_cart(-1)
#
# except Exception as e:
#     print(e)

########################################################################################

# person = (("Rahul"),(25),(5.9))
# print(person[2])
#
# person [0] = "Mangesh"


school = ["mangesh", 34, 3.9]
print(school[1])

school [0] = "Shyam"
print(school)