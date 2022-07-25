class files():
    def __init__(self):
        self.words = list()
        with open ("metin.txt","r",encoding="UTF-8") as file:
            information = file.read()
            information = information.split(" ")
            for i in information:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.words.append(i)
    def all_words(self):
        word_group = set()
        for i in self.words:
            word_group.add(i)
        print("All Words\n******************\n")
        for i in word_group:
            print(i)
            print("******************")
    def word_frequency(self):
        word_dictionary = dict()
        for i in self.words:
            if i in word_dictionary:
                word_dictionary[i] += 1
            else:
                word_dictionary[i] = 1
        for word,number in word_dictionary.items():
            print("{} Word = {} Times".format(word,number)) 
file_1 = files()
file_1.all_words()
file_1.word_frequency()