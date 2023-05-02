menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                    **
** To quit at any time, type 'quit' **
**************************************""")

for category, items in menu.items():
    print("\n" + category)
    print("----------")
    for item in items:
        print(item)

print("""\n***********************************
** What would you like to order? **
***********************************""")

order = {}
while True:
    user_input = input("> ").lower()
    if user_input == "quit":
        print ("Thanks for using snakes cafe application !")
        break
    else:
        found_item = False
        for item_list in menu.values():
            if user_input.title() in item_list:
                item_name = user_input.title()
                if item_name not in order:
                    order[item_name] = 1
                else:
                    order[item_name] += 1
                print(f"** {order[item_name]} order(s) of {item_name} have been added to your meal **")
                found_item = True
                break
        if not found_item:
            print("Sorry, that item is not on the menu. Please try again.")
