from flask import Flask
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os
from models.users import User
from flask_login import LoginManager
from extension import db
from models.vehicles import Vehicle
from models.partner import Partner
from models.partner_detail import PartnerSection
from models.faqs import FAQS
from models.driver_details import DriverDetails
from models.contact import Contact
from models.ins_company import InsuranceCompany

login_manager = LoginManager()

load_dotenv()  # os env (environmental variable)
print(os.environ.get("AZURE_DATABASE_URL"), os.environ.get("FORM_SECRET_KEY"))

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FORM_SECRET_KEY")

connection_string = os.environ.get("AZURE_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

# db = SQLAlchemy(app)  # orm
db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # Query your User model to retrieve the user based on the user_id
    return User.query.get(user_id)


try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
        # db.drop_all()  # if table exists and you add columns it will not recreate, so we drop it to create it
        db.create_all()  # syncing
except Exception as e:
    print("Error connecting to the database:", e)

from routes.users_bp import users_bp
from routes.contact_bp import contact_bp
from routes.faqs_bp import faqs_bp
from routes.home_bp import home_bp
from routes.partner_bp import partner_bp
from routes.cars_bp import cars_bp
from routes.quotes_bp import quotes_bp

app.register_blueprint(users_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(faqs_bp)
app.register_blueprint(home_bp)
app.register_blueprint(partner_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(quotes_bp)
