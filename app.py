from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from sqlalchemy.sql import text
from dotenv import load_dotenv
import uuid
import os

load_dotenv()  # os env (environmental variable)
print(os.environ.get("AZURE_DATABASE_URL"), os.environ.get("FORM_SECRET_KEY"))

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FORM_SECRET_KEY")

connection_string = os.environ.get("AZURE_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

db = SQLAlchemy(app)  # orm


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)


class Policy(db.Model):
    __tablename__ = "policies"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    policy_number = db.Column(db.String(20), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    premium = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("policies", lazy=True))


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)


class Claim(db.Model):
    __tablename__ = "claims"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    claim_number = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    policy_id = db.Column(db.String(36), db.ForeignKey("policies.id"), nullable=False)
    policy = db.relationship("Policy", backref=db.backref("claims", lazy=True))
    customer_id = db.Column(
        db.String(36), db.ForeignKey("customers.id"), nullable=False
    )
    customer = db.relationship("Customer", backref=db.backref("claims", lazy=True))


class FAQS(db.Model):
    __tablename__ = "faqs"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)


class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )


try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
        db.create_all()  # syncing
except Exception as e:
    print("Error connecting to the database:", e)

from users_bp import users_bp
from contact_bp import contact_bp
from faqs_bp import faqs_bp

app.register_blueprint(users_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(faqs_bp)


@app.route("/")
def index():
    return "Welcome to Insurance Policy Management System!"


@app.route("/policies")
def policies():
    # Fetch policies from the database
    policies = Policy.query.all()
    return render_template("policies.html", policies=policies)


@app.route("/claims")
def claims():
    # Fetch claims from the database
    claims = Claim.query.all()
    return render_template("claims.html", claims=claims)


@app.route("/customers")
def customers():
    # Fetch customers from the database
    customers = Customer.query.all()
    return render_template("customers.html", customers=customers)


# if __name__ == "__main__":
#     app.run(debug=True)
