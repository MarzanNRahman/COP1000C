def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2


def total_with_tax(money, tax_rate):
    return money + (money * tax_rate)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


radius = float(input("Enter the radius: "))
print(f"{circle_area(radius):.2f}")

money = float(input("Enter the money amount: "))
tax_rate = float(input("Enter the tax rate (%): ")) / 100
print(f"{total_with_tax(money, tax_rate):.2f}")

fahrenheit = float(input("Enter the Fahrenheit temperature: "))
print(f"{fahrenheit_to_celsius(fahrenheit)}")