def addition(x,y):
    answer = x + y
    return answer

products = (("Bread", 65.0), ("Milk", 60.0), ("Eggs", 60.0))
choice = input("Choose your product: ")

if choice == "1":
    price = 65
    print(f"Bread: Ksh {price}")

elif choice == "2":
    price = 60
    print(f"Milk: ksh {price}")

elif choice == "3":
    price = 60
    print(f"Eggs: ksh {price}")

def receipt(**kwargs):
    print("-- YOUR RECEIPT --")
    subtotal = 0
    for item, price in kwargs.items():
        print(f"{item}: Ksh {price:.2f}")
        subtotal += price
    print(f"Subtotal: Ksh {subtotal:.2f}")

receipt(bread=65.0, milk=60.0, eggs=60.0)