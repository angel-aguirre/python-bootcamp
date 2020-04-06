import json

from difflib import get_close_matches

def search_word(word):
    """
    Function that takes a word give by the user and look for its meaning in the json file
    """
    # Load the data from the json file
    with open("data.json") as file:
        # Store the data from the json file in a variable
        data = json.load(file)

    if word.upper() in data:
        # If the word given by the user is in the dictionary, we return the meaning
        return data[word.upper()]
    else:
        return "Opps, make sure the word you entered is right."

word = input("Enter the word you want to search: ")
print(f"  -  {search_word(word)}")
