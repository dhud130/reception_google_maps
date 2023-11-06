from flask import Flask, render_template, request

app = Flask(__name__)


location = {
    "673 Ayres Ave": ["acs building", "BLDG 750", "soldier support center"],
    "BLDG 683": ["Desmond Doss Health Clinic", "Desmond Doss", "clinic"],
    "694 McCornack Rd": ["PX", "Post Exchange", "schofield main exchange"],
    "1470 Foote St": ["tropics", "recreation center", "rec center", "tropics rec center", "bldg 589"]
}

def address_finder(locations, user_input):
    for key, values in locations.items():
        if user_input in [val.lower() for val in values]:
            return key
    return user_input + " not found in the dictionary"

if __name__ == '__main__':
    while True:
        user_input = input("Enter a location: ").lower()
        if user_input == 'exit':
            break
        result = address_finder(location, user_input)
        print(f"The location for '{user_input}' is: {result}")