from .. import db


class Wine(db.Model):
    __tablename__ = "wine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.public_id'), nullable=False)
    added_on = db.Column(db.DateTime, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    brand = db.Column(db.String(100))
    variety = db.Column(db.String(100))
    year = db.Column(db.Integer)

    def __repr__(self):
        return '<brand: {}>'.format(self.brand)
