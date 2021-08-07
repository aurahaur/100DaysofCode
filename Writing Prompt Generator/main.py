from prompt import Prompt

print("WRITING PROMPT GENERATOR\n")
character = input("Type the name of your character: ")
genre = input("""\nChoose one of 3 genres that we have!
1. Romance
2. Children Story
3. Comedy
Type the number here: """)
num_of_prompt = int(input("How many prompt do you want? Type here (1-5 only!): "))
print("\n")

story = Prompt(character, genre, num_of_prompt)

if genre == "1":
    story.romance()

elif genre == "2":
    story.children()

elif genre == "3":
    story.comedy()

else:
    print("Sorry, we didn't know that type of genre.")
