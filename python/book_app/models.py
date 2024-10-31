from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    copyright = db.Column(db.Integer)
    edition = db.Column(db.String(20))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    @property
    def total(self):
        return self.price * self.qty
