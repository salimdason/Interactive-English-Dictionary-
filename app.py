import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word does not exist. Please check and try again."

word = input("Enter your word: ")

print(translate(word))

