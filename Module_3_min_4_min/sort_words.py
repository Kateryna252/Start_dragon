import re
str_words = input('write everything, what you want to sort\n')

str_words_sub = re.sub("\W"," ",str_words)
list_words = re.split("\s", str_words_sub)
print(list_words)
for i in list_words:
    for i in list_words:
        if i == "":
            list_words.remove(i)
print(list_words)
list_words.sort()
print(list_words)

dict_word = {i: list_words.count(i) for i in list_words}
print(dict_word)
