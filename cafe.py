#Define the menu of the restraunt
menu = {
    'Chappati':10,
    'Tandoori Naan':15,
    'Garlic Naan':25,
    'Butter Chicken':350,
    'Chicken handi':400,
    'Mutton Tadka':450,
    'Mutton Biryani':650,
    'Chicken Biryani':500,
    'Jeera Rice':100,
    'Ice-cream':50,
    'Rabdi':80,
    'Falooda':100,
}

#greetings
print("Welcome to Al-Falah Restraunt ")
print("Chappati : Rs.10\n Tandoori Naan : Rs.15\n Garlic Naan : Rs.25\n Butter Chicken: Rs.350\n Chicken Handi: Rs.400\n Mutton Tadka: Rs.450\n Mutton Biryani: Rs.650\n Chicken Biryani: Rs.500\n Jeera Rice: Rs.100\n Ice-cream: Rs.50\n Rabdi: Rs.80\n Falooda: Rs.100")

order_total = 0
# order amount maths

#membership operator
item_1 = input("Enter the name of the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1] 
    print (f"Your item {item_1} is added ")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order =input("Do you want another item(Yes/No):")
if another_order == "Yes":
    item_2 = input("Enter the name of the item you want to order:")
    if item_2 in menu:
        order_total += menu[item_2]
        print (f"Your item {item_2} is added ")
    else:
        print(f"Ordered item {item_2} is not available yet!")

another_order2 =input("Do you want another item(Yes/No):")
if another_order2 == "Yes":
    item_3 = input("Enter the name of the item you want to order:")
    if item_3 in menu:
        order_total += menu[item_3]
        print (f"Your item {item_3} is added ")
    else:
        print(f"Ordered item {item_3} is not available yet!")

print(f"The Total amount of items is {order_total}")


