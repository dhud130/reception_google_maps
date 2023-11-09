from flask import Flask, render_template, request
from fuzzywuzzy import fuzz

app = Flask(__name__)

location = {
    "673 Ayres Ave": ["acs building", "BLDG 750", "soldier support center"],
    "683 Waianae Ave": ["Desmond Doss Health Clinic", "Desmond Doss", "clinic"],
    "694 McCornack Rd": ["PX", "Post Exchange", "schofield main exchange"],
    "1470 Foote Ave": ["tropics", "recreation center", "rec center", "tropics rec center", "bldg 589"],
    "361 Waianae Ave": ["Tropic Lightning Museum", "museum"], 
    "560 Kolekole Ave": ["IG office", "Inspector General Office", "Inspector General"],
    "2091 Kolekole Ave": ["25ID Headquarters", "Division HQ", "Division Headquarters"],
    "698 Trimble Rd": ["Schofield Barracks Commissary", "Commissary"],
    "1316 Lyman Rd": ["Provost Marshal Office", "Provost Marshal", "Provost"],
    "540 Humprheys Rd": ["Central Issue Facility", "CIF"],
    "1020 Menoher Rd": ["Replacement Company", "Reception Company", "Repl-Co"]


}

@app.route('/')
def index():
    return render_template('Homepage.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

if __name__ == '__main__':
    app.run(debug=True)



