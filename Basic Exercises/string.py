class string():
    def __init__(self,sentence):
        self.sentence  = sentence
        self.list_sentence = self.sentence.split()

    def words(self):
        for i in self.list_sentence:
            print(i)
    def word_number(self):
        print("Number of words: {}".format(len(self.list_sentence)))
    def character_freq(self):
        characters = dict()
        for i in self.sentence.lower():
            if i in characters:
                characters[i] += 1
            else:
                characters[i] = 1
        for i,j in characters.items():
            print("Character: {} - Count: {}\n".format(i,j))


sentence = input("Enter your sentence: ")
string_1 = string(sentence)
string_1.words()
string_1.word_number()
string_1.character_freq() 