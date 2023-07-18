from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt



class User(db.Model):
    __tablename__ = "users"

    serialize_rules =('-password_hash', '-recipes')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)



    @hybrid_property
    def password_hash(self, new_pass):
        p_hash = bcrypt.generate_password_hash(new_pass.encode('utf-8'))
        self._password_hash = p_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    playlists = db.relationship('Playlist', backref='User')
    

    def __repr__(self):
        return f"<User {self.username}>"
    


class Playlist(db.Model, SerializerMixin):
     __tablename__ = 'playlists'
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String)
     songs = db.Column(db.String)
     
     user_id = db.Column(
         db.Integer,
         db.ForeignKey('users.id')
         )
     
     def __repr__(self):
         return f"<Recipe {self.title}>"
    

    