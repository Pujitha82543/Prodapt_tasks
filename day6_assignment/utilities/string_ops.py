import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count