import string

def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def remove_symbols(text):
    dont_remove = string.ascii_lowercase
    dont_remove += " "
    text = list(text)
    for i, letter in enumerate(text):
        if letter == "\n":
            text[i] = " "
    whitelist = set(dont_remove)
    answer = ''.join(filter(whitelist.__contains__, text))
    return answer

def count_words(filename):
    text = remove_symbols(read_from_file(filename)).split(" ")
    d = {}
    for word in text:
        if "\n" in word:
            words = word.split("\n")
            for w in words:
                if w not in d:
                    d[w] = 0
                d[w] += 1
        else:
            if word not in d:
                d[word] = 0
            d[word] += 1
    return d


filename = 'alice_in_wonderland.txt'

alice_dict = count_words('Alice_in_wonderland.txt')
for word, value in alice_dict.items():
    print(word, value)
