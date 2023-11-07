from flask import Flask, render_template, request
from fuzzywuzzy import fuzz

app = Flask(__name__)

location = {
    "673 Ayres Ave": ["acs building", "BLDG 750", "soldier support center"],
    "BLDG 683": ["Desmond Doss Health Clinic", "Desmond Doss", "clinic"],
    "694 McCornack Rd": ["PX", "Post Exchange", "schofield main exchange"],
    "1470 Foote St": ["tropics", "recreation center", "rec center", "tropics rec center", "bldg 589"]
}

def address_finder(locations, user_input, threshold=80):
    best_match = None
    best_ratio = 0
    user_input = user_input.lower()
    suggestions = []

    for key, values in locations.items():
        for val in values:
            ratio = fuzz.ratio(user_input, val.lower())
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = key

            if ratio >= threshold:
                suggestions.append(val)

    if best_ratio >= threshold:
        result = f"The location for '{user_input}' is: {best_match}"
    else:
        result = f"The location for '{user_input}' not found in the dictionary."

    if best_ratio < 100:
        result += " We think you meant: " + ', '.join(suggestions)

    return result

if __name__ == '__main__':
    while True:
        user_input = input("Enter a location: ").lower()
        if user_input == 'exit':
            break
        result = address_finder(location, user_input)
        print(result)