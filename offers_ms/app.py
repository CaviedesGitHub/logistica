from offers_ms import create_app
from offers_ms.vistas.vistas import VistaOffer, VistaGetOffer, VistaPing
from offers_ms.modelos.modelos import db, Offer
from flask_restful import Api
from flask_jwt_extended import JWTManager

app=create_app('default')
app_context=app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaOffer, '/offers/')
api.add_resource(VistaGetOffer, '/offers/<id>')
#api.add_resource(VistaOtra, '/offers?')   #?post=id&filter=me
api.add_resource(VistaPing, '/offers/ping')


jwt = JWTManager(app)