# app.py

from flask import render_template
import config
from models import Trail, trail_schema, trails_schema  # Ensure proper import
import connexion  # Ensure this import is here for proper app setup

# Initialize the Connexion app correctly with Flask
app = connexion.FlaskApp(__name__, specification_dir=config.basedir)

# Add API specification (OpenAPI) to the app
app.add_api(config.basedir / "swagger.yml")

# Define a Flask route
@app.route("/")
def home():
    trails = Trail.query.all()  # Query all trails from the database
    return render_template("home.html", trails=trails)

# Ensure the app runs with Flask's built-in server (for development)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
