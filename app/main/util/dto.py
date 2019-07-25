from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(
            required=True,
            description='user email address'
        ),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(
            required=True,
            description='The user password'
        )
    })


class WineDto:
    api = Namespace('wine', description='wine related operations')
    wine = api.model('wine', {
        'public_id': fields.String(description='wine identifier'),
        'brand': fields.String(required=True, description='the wine brand'),
        'variety': fields.String(required=True,
                                 description='the wine variety'),
        'year': fields.Integer(required=True,
                               description='the year the wine was made')
    })
