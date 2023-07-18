#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Playlist, User

fake = Faker()

with app.app_context():

    print("Deleting all records...")
    User.query.delete()
    Playlist.query.delete()

    fake = Faker()

    print("Creating users...")

    # make sure users have unique usernames
    users = []
    usernames = []

    for i in range(20):
        
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        user = User(
            username=username
        )

        user.password_hash = user.username + 'password'

        users.append(user)

    db.session.add_all(users)




    print("Creating playlist...")
    playlists = []
    for i in range(100):
        
        playlist = Playlist(
            title=fake.sentence(),
            songs=fake.sentance(),
        )

        playlist.user = rc(users)

        playlists.append(playlist)

    db.session.add_all(playlists)
    
    db.session.commit()
    print("Complete.")