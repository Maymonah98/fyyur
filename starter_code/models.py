from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import ARRAY, DateTime
import datetime

db = SQLAlchemy()

def setup_db(app):
    moment = Moment(app)
    app.config.from_object('config')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    Migrate(app, db)
    db.init_app(app)
    db.create_all()


class Show(db.Model) :
  _tablename_= 'show'
  venue_id=db.Column(db.Integer,db.ForeignKey('venue.id'),primary_key=True)
  artist_id=db.Column(db.Integer,db.ForeignKey('artist.id'),primary_key=True)
  start_time=db.Column(db.DateTime, nullable=False,default=datetime.datetime.utcnow)

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),nullable=False)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    address = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    image_link = db.Column(db.String(500),nullable=False)
    facebook_link = db.Column(db.String(120),)
    genres=db.Column(ARRAY(db.String()))
    website_link= db.Column(db.String(500),nullable=False)
    looking_for_talent= db.Column(db.Boolean,default=False)
    seeking_desc= db.Column(db.String())
    shows = db.relationship('Show',backref='venue',lazy=True)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),nullable=False)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    genres=db.Column(ARRAY(db.String()))
    image_link = db.Column(db.String(500),nullable=False)
    facebook_link = db.Column(db.String(120))
    website_link= db.Column(db.String(500))
    looking_for_venues= db.Column(db.Boolean,default=False)
    seeking_desc= db.Column(db.String())
    shows = db.relationship('Show',backref='artist',lazy=True)


def __repr__(self):
        return f'<Artist {self.id} {self.name} {self.city} {self.state} {self.phone} {self.genres} {self.image_link} {self.facebook_link} {self.image_link} {self.website_link} {self.seeking_desc}>'

# TODO: implement any missing fields, as a database migration using Flask-Migrate
