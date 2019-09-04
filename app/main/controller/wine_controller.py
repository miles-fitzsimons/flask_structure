from flask import request
from flask_restplus import Resource

from ..util.dto import WineDto
from ..service.wine_service import save_new_wine, get_all_wines_by_user

from ..util.decorator import token_required

api = WineDto.api
_wine = WineDto.wine


@api.route('/')
class WineList(Resource):
    # MILES token_required
    @api.response(201, 'Wine successfully created.')
    @api.doc('create a new wine')
    @api.expect(_wine)
    def post(self):
        # get user
        # data, status = Auth.get_logged_in_user(request)
        data = request.json
        return save_new_wine(data=data)


@api.route('/<user_id>')
@api.param('user_id', 'the id of the user')
@api.response(404, 'User not found.')
class Wines(Resource):
    @token_required
    @api.doc('list of all users wines')
    @api.marshal_list_with(_wine, envelope='data')
    def get(self, user_id):
        wines = get_all_wines_by_user(user_id)
        if not wines:
            api.abort(404)
        else:
            return wines
