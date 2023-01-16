import sqlalchemy as sa
from flaskr import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(30), nullable=False, unique=True,
                         index=True)
    email = sa.Column(sa.String(140), nullable=False, unique=True,
                      index=True)
    password_hash = sa.Column(sa.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"""
            user:
                id: {self.id},
                username: {self.username},
                email: {self.email},
        """
