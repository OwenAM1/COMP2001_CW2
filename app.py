# app.py

from flask import render_template

import config
from models import Trail
<<<<<<< HEAD
=======
import connexion  # Ensure this import is here for proper app setup
>>>>>>> parent of a9aad22 (Last save before restarting)


app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    people = Trail.query.all()
    return render_template("home.html", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)