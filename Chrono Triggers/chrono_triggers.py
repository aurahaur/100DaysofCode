import random

SHOP = {
    "ether": {
        "ether": 50,
        "mid-ether": 100,
        "hi-ether": 150,
        "turbo-ether": 200
    },
    "potion": {
        "potion": 25,
        "mid-potion": 30,
        "hi-potion": 70
    },
    "vest": {
        "black-vest": 100,
        "ruby-vest": 150,
        "dark-vest": 200
    },
    "sword": {
        "masamune": 500,
        "wooden-sword": 200,
        "thunder-blade": 400,
    }

}

life = {
    "HP": 500,
    "MP": 90,
    "Strength": 10
}

lavos_life = {
    "HP": random.randint(600, 2000),
    "MP": random.randint(100, 1000),
    "Strength": random.randint(70, 500)
}

money_bank = 5000
item_bank = 0
item_type = ""
item_bucket = {}
i_name = ""
i_total = 0
user_score = 0


def report(chosen_chara):
    if chosen_chara == "report":
        print("\n")
        for key, val in life.items():
            print(f"{key}: {val}")
        print("\n")


def shop_list(chosen_items):
    global money_bank
    global item_bank
    global item_type
    if chosen_items in SHOP:
        print()
        print(f"You chose {chosen_items.capitalize()}!")
        print(f"What type of {chosen_items.capitalize()}?\n")
        for a, b in SHOP[chosen_items].items():
            print(f"{a.capitalize()}: {b} zeen")
        print()
        item_type = input("Type here: ").lower()
        item_c = input("How many: ")
        item_count = int(item_c)
        if item_type in SHOP[chosen_items].keys():
            if item_bank != 99:
                print(f"You will buy {item_count} {item_type.capitalize()}\n")
                print(f"Your money before: {money_bank} zeen")
                total = int(item_count * SHOP[chosen_items][item_type])
                if money_bank >= total:
                    print(f"{item_count} {item_type.capitalize()}: {total} zeen")
                    money_bank = money_bank - total
                    item_bank = item_bank + item_count
                    print(f"Your money now: {money_bank} zeen")
                    print(f"Your items now: {item_bank} items\n")
                    item_bucket[item_type] = item_c
                else:
                    print(f"Sorry, you do not have enough money to buy {item_type.capitalize()}\n")
        elif item_type not in SHOP[chosen_items].keys():
            print("Sorry, the item that you want to buy is not in the list. Try again....\n")
    elif chosen_items == 'e':
        print("You exit shopping....\n")
    elif chosen_items not in SHOP:
        print("Sorry, the item that you want to buy is not in the list. Try again....\n")


def customize_life(items_name, items_total):
    global i_name
    global i_total
    if items_name in ['ether', 'black-vest']:
        life['MP'] = life['MP'] + (50 * int(items_total))
    elif items_name in ['mid-ether', 'ruby-vest']:
        life['MP'] = life['MP'] + (100 * int(items_total))
    elif items_name in ['hi-ether', 'dark-vest']:
        life['MP'] = life['MP'] + (150 * int(items_total))
    elif items_name == 'turbo-ether':
        life['MP'] = life['MP'] + (200 * int(items_total))
    if items_name == 'potion':
        life['HP'] = life['HP'] + (35 * int(items_total))
    elif items_name == 'mid-potion':
        life['HP'] = life['HP'] + (100 * int(items_total))
    elif items_name == 'hi-potion':
        life['HP'] = life['HP'] + (175 * int(items_total))
    if items_name == 'masamune':
        life['Strength'] = life['Strength'] + (100 * int(items_total))
    elif items_name == 'wooden-sword':
        life['Strength'] = life['Strength'] + (30 * int(items_total))
    elif items_name == 'thunder-blade':
        life['Strength'] = life['Strength'] + (70 * int(items_total))

    for X, Y in life.items():
        print(X, Y)
    print()


def fight_lavos(lavos, you):
    global user_score
    print("\n*** FIGHT LAVOS ***\n")
    print("LAVOS\n")
    for K, V in lavos_life.items():
        print(f"{K}: {V}")
    print("\nVS.\n")
    print("YOU!\n")
    for X, y in life.items():
        print(f"{X}: {y}")
    it = iter(lavos.values())
    it_u = iter(you.values())
    hp_u, mp_u, st_u = next(it_u), next(it_u), next(it_u)
    hp, mp, st = next(it), next(it), next(it)
    if hp_u > hp:
        user_score += 1
    if mp_u > mp:
        user_score += 1
    if st_u > st:
        user_score += 1
    else:
        user_score = 0
    print()
    print(f"Your score is {user_score}")


print("🌟►CHRONO TRIGGERS◄🌟\n")


while True:
    print(f"You have {money_bank} zeen in your Money Bank!\n"
          f"Let's buy something to help you fight big boss, Lavos!\n")
    print("""What do you want to buy?\n""")
    for k, v in SHOP.items():
        print(f"{k.capitalize()}")
    item_buy = input("\nType here ('e' to exit shopping): ").lower()
    shop_list(item_buy)
    print(f"Your bucket:")
    if item_buy != 'e':
        for i_name, i_total in item_bucket.items():
            print(f"{i_name.capitalize()} => {i_total}")
        customize_life(i_name.casefold(), i_total)
    if item_buy == 'e':
        print('Thank you for shopping! Now, you are ready to fight with Lavos!')
        fight_lavos(lavos_life, life)
        if user_score == 3:
            print("You win! Congratulations! You saved the earth!")
        else:
            print("You lose.... The future refused to change....")
        print("\n*** Thank you for playing! ***\n")
        break
