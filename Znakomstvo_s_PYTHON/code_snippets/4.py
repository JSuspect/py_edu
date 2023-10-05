def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word += word[i] + "_"
    return new_word
phrase = "hello"
print(add_underscores(phrase))

#Рефакторинг функции add_underscores
def add_underscores_ref(word):
    new_word = "_"
    for letter in word:
        new_word = new_word + letter + "_"
    return new_word

phrase3 = "ПРИВЕТЫ"
print(add_underscores_ref(phrase3))