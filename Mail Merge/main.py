PLACEHOLDER = "[name]"

with open('invited_names.txt') as names:

    names = names.readlines()

with open('the_letter.txt') as letter:
    letter_content = letter.read()
    for name in names:
        stripped = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped)
        with open(f'letter_for_{stripped}.txt', mode='w') as ready_letter:
            ready_letter.write(new_letter)
