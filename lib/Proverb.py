import random
class Proverb():
    def __init__(self, filename="./data/data.txt"):
        self.proverb_list = []
        self.out_list = []
        self.loadProverb(filename)

    def loadProverb(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        self.proverb_list = [line.strip() for line in lines if line.strip()]

    def getRandomProverb(self, num_lines):
        if num_lines > len(self.proverb_list):
            raise ValueError(f"Cannot select {num_lines} lines from a list of {len(self.proverb_list)} elements")
        random_list = random.sample(self.proverb_list, num_lines)
        self.out_list += random_list
    
        return random_list
