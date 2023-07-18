from flask import request, session
from sqlalchemy.exc import IntegrityError


from config import app, db
from models import User, Playlist


@app.post("/signup")
def signup():
    pass



@app.get('/check_session')
def check_session():
    user_id = session.get('user_id')

    user = User.query.filter(
        User.id == user_id
    ).first()


    if not user:
        return {"error": "Not autrhorized"}, 401
    

    return user.to_dict(), 200


@app.post('/login')
def login():
    data = request.get_json()

    user = User.query.filter(
        User.username ==data.get("username")
    ).first()


    if not user or not user.authenticate(data.get('password')):
        return {"error": "Invalid login"}, 401
    
    session['user_id'] = user.id
    return user.to_dict(), 201


@app.get('/home')
def home():
    return (
        "<h1> hahaha </h1>"
    )



if __name__ == '__main__':
    app.run(port=5555, debug=True)