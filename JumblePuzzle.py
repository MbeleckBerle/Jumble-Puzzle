import time


# a class to hold my functions
class CheckWord:
    # Reading the files
    with open("NounsIndex.txt", "r", encoding="utf-8") as f:
        nouns = f.readlines()

    with open("VerbsIndex.txt", "r", encoding="utf-8") as f:
        verbs = f.readlines()

    with open("AdjIndex.txt", "r", encoding="utf-8") as f:
        adjectives = f.readlines()

    with open("AdvIndex.txt", "r", encoding="utf-8") as f:
        adverbs = f.readlines()

    # class is initialised with string from the user
    def __init__(self, word):
        # Stores the parts of speech in a dictionary
        self.speech = {
            "noun": self.splitWords(self.nouns),
            "verb": self.splitWords(self.verbs),
            "adverb": self.splitWords(self.adverbs),
            "adjective": self.splitWords(self.adjectives),
        }
        self.word = word

    # Checks the NounsIndex.txt file if the word exists in it and returns True/False
    def isNoun(self):
        result = self.checkPart("noun")
        return result

    # Checks the VerbsIndex.txt file if the word exists in it
    def isVerb(self):
        result = self.checkPart("verb")
        return result

    # Checks the AdvIndex.txt if the word exist and returns True/False
    def isAdverb(self):
        result = self.checkPart("adverb")
        return result

    # Checks the AdjIndex.txt if the word exists and returns True/False
    def isAdjective(self):
        result = self.checkPart("adjective")
        return result

    # function to split and ignore all words with underscores and returns the result
    def splitWords(self, file):
        words = []
        for item in file:
            word = item.split("|")[0]
            if "_" not in word:
                words.append(word)

        return words

    # This function loops through each element in our new list
    #  sorts the string in alphabetical order and
    # compares it to a sorted version of each item in the list
    # it returns True if there is a match
    def checkPart(self, part):
        for i, n in enumerate(self.speech[part]):
            if sorted(self.word) == sorted(n):
                self.foundWord = self.speech[part][i].upper()
                # print(self.speech[part][i], " ", part)
                # return self.speech[part][i]
                return True


# class that has our start game function
class JumblePuzzle:
    def startGame():
        start = True

        while start == True:
            takeInput = input(
                "\nEnter the Jumble Puzzle word: (<Enter> to quit) >> "
            ).lower()

            print("Start time: ", time.strftime("%H:%M:%S", time.localtime()))
            if takeInput == "":
                start == False
                break
            UserInput = CheckWord(takeInput)

            # Prints the start time

            # Verb Check
            if UserInput.isNoun() == True:
                print(UserInput.foundWord, "NOUN")

            # Verb Check
            elif UserInput.isVerb() == True:
                print(UserInput.foundWord, "VERB")

            # Adverb check
            elif UserInput.isAdverb() == True:
                print(UserInput.foundWord, "ADVERB")

            # ADjective check
            elif UserInput.isAdjective() == True:
                print(UserInput.foundWord, "ADJECTIVE")

            else:
                print("<<Not found>")

            # Prints the end time
            print("End time: ", time.strftime("%H:%M:%S", time.localtime()))


# starts the game
if __name__ == "__main__":
    JumblePuzzle.startGame()
