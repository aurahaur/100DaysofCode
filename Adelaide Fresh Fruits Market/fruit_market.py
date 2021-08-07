address = ["Flat Floor Street", "18", "New York"]
pins = {"Angel": 1234, "Angelo": 1111, "Angela": 2222}

key_pin = list(pins.keys())
val_pin = list(pins.values())

print("ADELAIDE FRESH FRUITS MARKET")
print(f"Address: {address[0]}, {address[1]}, {address[2]}\n")

pin = int(input("Enter your pin: "))


def find_in_file(f):
    myfile = open("sample2.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That fruit is in our warehouse."

    else:
        return "No such fruit found!"


def remove_fruit(f):
    with open("sample2.txt", "r") as r:
        lines = r.readlines()
    with open("sample2.txt", "w") as r:
        for i in lines:
            if i.strip("\n") != f:
                r.write(i)


def add_fruit(f):
    with open("sample2.txt", "a") as file_object:
        file_object.write(f"\n{f}")


def new_fruits():
    new_fruit = open("sample2.txt").read().splitlines()
    print("This is the current fruits in the warehouse:\n")
    for line in new_fruit:
        print(line)


def add_admin(name, Pin):
    pins[name] = Pin
    print("This is the current admin in Adelaide Fresh Fruits Market\n")
    for k, v in pins.items():
        print(f"Name: {k} => Pin: {v}")


while True:
    if pin in pins.values():
        position = val_pin.index(pin)
        print(f"\nWelcome, {key_pin[position]}!")
        print("""What do you want to do?
    1. Check if there is fruit in the warehouse
    2. Remove fruit from the warehouse
    3. Add fruit to the warehouse
    4. Add new admin
    0. Exit program\n""")
        admin_choice = input("Type here: ")
        if admin_choice == "1":
            fruit = input("Enter fruit you want to check: ")
            print(find_in_file(fruit))
        elif admin_choice == "2":
            fruit_to_delete = input("Type fruit name you want to remove from our warehouse: ")
            remove_fruit(fruit_to_delete)
            new_fruits()
        elif admin_choice == "3":
            fruit_to_add = input("Type fruit name you want to add to our warehouse: ")
            add_fruit(fruit_to_add)
            new_fruits()
        elif admin_choice == "4":
            admin_name = input("Type the admin's name you want to add to our market: ").capitalize()
            admin_pin = input("Type the admin's pin as you want: ")
            add_admin(admin_name, admin_pin)
        elif admin_choice == "0":
            break
    else:
        print("Incorrect pin!")
        print("This info can be accessed only by: ")
        for key in pins.keys():
            print(key)
        break
