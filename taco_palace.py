def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $3.50")
    print("2. Burrito - $6.00")
    print("3. Nachos - $4.50")
    print("4. Quesadilla - $5.00")
    print("5. Quit")


def get_price(selection):
    if selection == 1:
        return 3.50
    elif selection == 2:
        return 6.00
    elif selection == 3:
        return 4.50
    elif selection == 4:
        return 5.00
    else:
        return 0.00


def main():
    ordered_items = []
    total = 0.00

    print(
        "Welcome to Taco Palace, please view the menu below "
        "and enter the number that represents your selection."
    )

    while True:
        print_menu()

        try:
            selection = int(input("Enter your selection (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if selection == 5:
            break
        elif selection == 1:
            item = "Taco"
        elif selection == 2:
            item = "Burrito"
        elif selection == 3:
            item = "Nachos"
        elif selection == 4:
            item = "Quesadilla"
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")
            continue

        print(f"You have selected {item}.")
        price = get_price(selection)
        total += price
        ordered_items.append(item)

    print("\nOrder Summary")

    if ordered_items:
        print("You ordered: " + ", ".join(ordered_items))
    else:
        print("You did not order any items.")

    print(f"Your total is ${total:.2f}")


main()