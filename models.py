from app import application
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(application)


class Shortlink(db.Model):
    id = db.Column(db.String, primary_key=True)
    fullUrl = db.Column(db.String)

    def __init__(self, id, url):
        self.id = id
        self.fullUrl = url

    def addUrl(self, id, url):
        self.id = id
        self.fullUrl = url
