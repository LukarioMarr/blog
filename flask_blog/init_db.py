from main import app, db
from models import Entry

with app.app_context():
    db.create_all()
    print("Databáze byla inicializována!")
