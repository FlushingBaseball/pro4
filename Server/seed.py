from faker import Faker
from app import app
from models import db, User

fake = Faker()

with app.app_context():

    User.query.delete()


    users = []
    for n in range(50):
        user = User(username = fake.name())
        users.append(user)

        db.session.add_all(users)
        db.session.commit()

