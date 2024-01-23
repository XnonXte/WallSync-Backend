from flask import Flask

from routes.wallpapers import bp as wallpapers_bp
from utils.sqlite3_interface import Sqlite3Interface

app = Flask(__name__)
DATABASE = "./db/wallpapers.db"

# Assigning sqlite3_interface to wallpapers_bp to be used in there.
sqlite3_interface = Sqlite3Interface(app, DATABASE)
wallpapers_bp.sqlite3_interface = sqlite3_interface

# Register blueprint with the prefix "/wallpapers".
app.register_blueprint(wallpapers_bp, url_prefix="/wallpapers")

if __name__ == "__main__":
    # Module save.
    app.run(port=8080, debug=True)
