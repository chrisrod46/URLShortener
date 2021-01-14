from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
class ShortUrl(db.Model):
    __tablename__ = 'shorturl'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String)
    short_url = db.Column(db.String)
    date = db.Column(db.Date)


    def __repr__(self):
        return 'ShortUrl({}, {}, {}, {})'.format(repr(self.id),
        repr(self.original_url), repr(self.short_url), repr(self.date))
