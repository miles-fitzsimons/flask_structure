import uuid
import datetime

from app.main import db
from app.main.model.wine import Wine


def save_new_wine(data):
    new_wine = Wine(
        public_id=str(uuid.uuid4()),
        user_id=data['user_id'],
        added_on=datetime.datetime.utcnow(),
        brand=data['brand'],
        variety=data['variety'],
        year=data['year']
    )
    save_changes(new_wine)
    response_object = {
        'status': 'success',
        'message': 'Successfully added wine.'
    }
    return response_object, 201


def get_all_wines_by_user(user_id):
    return Wine.query.filter_by(user_id=user_id).all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
