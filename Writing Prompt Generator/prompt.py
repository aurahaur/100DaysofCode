import random
DEFAULT_NAME = '[name]'
TOTAL_PROMPTS = 5
RANDOM_PROMPT = [random.randint(0, TOTAL_PROMPTS)]


class Prompt:

    def __init__(self, name, genre, number_of_prompt):
        self.name = name
        self.genre = genre
        self.number_of_prompt = number_of_prompt

    def romance(self):
        roin = open('romance.txt', 'rt')
        rut = open('romance_final.txt', 'wt')
        if self.number_of_prompt == 1:
            for index, line in enumerate(roin):
                if index in RANDOM_PROMPT:
                    rut.write(line.replace(DEFAULT_NAME, self.name.capitalize()))
        elif self.number_of_prompt > 1:
            prompt_count = [i for i in range(self.number_of_prompt)]
            for index, line in enumerate(roin):
                if index in prompt_count:
                    rut.write(line.replace(DEFAULT_NAME, self.name.capitalize()))
        roin.close()
        rut.close()
        print(open('romance_final.txt').read())

    def children(self):
        rin = open('children.txt', 'rt')
        rout = open('children_final.txt', 'wt')
        if self.number_of_prompt == 1:
            for index, line in enumerate(rin):
                if index in RANDOM_PROMPT:
                    rout.write(line.replace(DEFAULT_NAME, self.name.capitalize()))
        elif self.number_of_prompt > 1:
            prompt_count = [i for i in range(self.number_of_prompt)]
            for index, line in enumerate(rin):
                if index in prompt_count:
                    rout.write(line.replace(DEFAULT_NAME, self.name.capitalize()))
        rin.close()
        rout.close()
        print(open('children_final.txt').read())

    def comedy(self):
        coin = open('comedy.txt', 'rt')
        cout = open('comedy_final.txt', 'wt')
        if self.number_of_prompt == 1:
            for index, line in enumerate(coin):
                if index in RANDOM_PROMPT:
                    cout.write(line.replace(DEFAULT_NAME, self.name.capitalize()))
        elif self.number_of_prompt > 1:
            prompt_count = [i for i in range(self.number_of_prompt)]
            for index, line in enumerate(coin):
                if index in prompt_count:
                    cout.write(line.replace(DEFAULT_NAME, self.name.capitalize()))
        coin.close()
        cout.close()
        print(open('comedy_final.txt').read())
