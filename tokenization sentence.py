import language_detection as ld

"""from the PreProcess.py:
        the output has been exported to "new file2"  """

# iniatialize the counter of each language frequency in the file
malay = 0
english = 0
mixed = 0
other = 0

others = []  # initalize the empty array to insert the word/token that doesnt contain malay or english language

with open("new file2", "r") as f:  # declare new file2 as f
    for index, sentence in enumerate(f, start=1):
        en_count = 0  # initialize the malay and english counter
        bm_count = 0
        row = sentence.split(" ")  # start tokenize the sentence
        for word in row:
            lang = ld.detect_language(word.lower())
            # detect which language for each word/token.
            # also, ignore the punctuation

            # increases the counter
            if lang == 'english':
                en_count += 1
            elif lang == 'indonesian':
                bm_count += 1
            """problem 1 : the language_detection doesnt malay language however its detect the indonesian language. 
            since the malay language and the indonesian doesnt have much different so i consider the indonesian is the malay"""

        """start analysis the sentences is in which language"""
        if en_count > bm_count:  # if the english counter more than the malay so it'll consider english sentence
            print(index, " :", sentence, " : english")
            english += 1
        elif bm_count > en_count:  # if the malay counter more than the english so it'll consider malay sentence
            print(index, " :", sentence, " : malay")
            malay += 1
        elif bm_count & en_count == 0:  # if the sentences doesnt contain any english or malay word so its consider other
            print(index, " :", sentence, " : other")  # because its might only contain punctuation only
            others.append(word)
            other += 1
        else:
            if (
                    bm_count == en_count) & bm_count > 0:  # if both counter is equal and the counter more than 1 its consider
                print(index, " :", sentence, " : mixed")  # as mixed language. Otherwise, it'll consider other
                mixed += 1
            else:
                print(index, " :", sentence, " : other")
                others.append(word)
                other += 1

print()
print("The frequency of each categories")
print("english : ", english)
print("malay : ", malay)
print("other : ", other)
print("mixed : ", mixed)

others = list(dict.fromkeys(others))  # remove the repetitive elements in others array
print()
print("list of others ")
print(others)
"""Problem 2 : some of the element in others array contain malay and english word however the language_detection.py 
detect these word in other language for example "bijak" was detect as arabic"""
