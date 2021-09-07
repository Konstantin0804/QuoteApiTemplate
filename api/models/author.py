from api import db


class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    surname = db.Column(db.String(32), server_default="Иванов") #Ставим фамилию Иванов по умолчанию
    quotes = db.relationship('QuoteModel', backref='author', lazy='dynamic')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname