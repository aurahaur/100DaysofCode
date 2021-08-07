import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    matching = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(matching) > 0:
        y_n = input(f"Do you mean it's \"{matching[0]}\"?\nType Y if yes, N if no: ").upper()
        if y_n == "Y":
            return data[matching[0]]
        elif y_n == "N":
            return f"The word \"{w}\" doesn't exist. Please check it again."
        else:
            return "Sorry, we didn't understand your word...."
    else:
        return f"The word \"{w}\" doesn't exist. Please check it again."


while True:
    print("*** WINETOXINIFY DICTIONARY APP ***")
    word = input("Enter a word (Type 'e' to exit program): ").lower()
    print()
    if word == "e":
        print("You exit the Winetoxinify Dictionary App!\nThank you for using!")
        break
    else:
        output = translate(word)

        if type(output) == list:
            for i in output:
                print(i)
        else:
            print(output)
        print()
