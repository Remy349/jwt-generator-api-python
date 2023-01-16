import sqlalchemy as sa
from flaskr import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    user_id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(30), nullable=False, unique=True, index=True)
    email = sa.Column(sa.String(140), nullable=False, unique=True, index=True)
    password_hash = sa.Column(sa.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"""
            user:
                user_id: {self.user_id},
                username: {self.username},
                email: {self.email},
        """


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(
        db.select(User).filter_by(user_id=int(user_id))
    ).scalar_one()
