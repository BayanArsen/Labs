def word_frequency(word):
    words = word.split()
    return {word: words.count(word) for word in set(words)}

string = str(input())
result = word_frequency(string)
print(result)