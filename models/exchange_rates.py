from app import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from .base import BaseModel


class ExchangeRates(db.Model, BaseModel):
    __tablename__ = 'exchange_rates'

    id = db.Column(db.Integer, primary_key=True)
    created_at = datetime.utcnow()
    base = db.Column(db.String())
    rates = db.Column(JSON)

