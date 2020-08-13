from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

# Import routes
from routes.product import Product_item
from routes.vendor import Vendor_item

app = Flask(__name__)
CORS(app)
api = Api(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Project test Flask + React"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

api.add_resource(Product_item, '/product_item')
api.add_resource(Vendor_item, '/vendor_item')

if __name__ == '__main__':
    app.run(debug=True)