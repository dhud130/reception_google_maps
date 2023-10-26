from flask import Flask, render_template, request





location = {"673 Ayres Ave":["acs building", "ACS building", "BLDG 750", "Soldier Support Center", "soldier support center"],
"BLDG 683": ["Desmond Doss Health Clinic", "Desmond Doss", "desmond doss", "desmond doss health clinic"], 
"694 McCornack Rd":["PX", "Schofield Main Exchange", "Post Exchange", "px", "post exchange", "schofield main exchange"]}

app = Flask(__name__)
app.route("/", method=['GET', 'POST'])
def address_finder():
    if request.method == 'POST':
        user_input = request.form['location']
        result = address_lookup(location, user_input.lower())

        if result != user_input:
            return f"The location for '{user_input}' is: {result}"
        else:
            return f"'{user_input}' not found in the dictionary"
    return render_template('inputpage.html')

if __name__ == '__main__':
    app.run(debug=True)
