import datetime

from flask import current_app
from sqlalchemy.ext.declarative import declared_attr

from extensions import db
from shortener.converter import Converter
from utils.models.meta import Model


class Base(Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    read_only_fields = ['id', 'created_at', 'updated_at']


class ShortUrl(Base):
    short_key = db.Column(db.String(30))
    original_url = db.Column(db.TEXT)

    @property
    def full_short_url(self):
        return '{}{}'.format(current_app.config['BASE_URL'], self.short_key)

    @classmethod
    def create_entry(cls, original_url):
        converter = Converter(current_app.config['ALPHABET'])

        entry = cls()
        entry.original_url = original_url
        # saving to db to get id
        db.session.add(entry)
        db.session.flush()
        entry.short_key = converter.shorten(entry.id)
        # saving after short key added
        db.session.add(entry)
        db.session.commit()

        return entry

    @classmethod
    def find_by_short_key(cls, short_key):
        converter = Converter(current_app.config['ALPHABET'])

        real_id = converter.decipher(short_key)
        return cls.query.filter_by(id=real_id).first()
