from app import db
from sqlalchemy.dialects.postgresql import JSON

class ExchangeRates(db.Model):
    __tablename__ = 'exchange_rates'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    base = db.Column(db.String())
    rates = db.Column(JSON)

