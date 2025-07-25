from flask import Flask
from routes import predict, user
from extensions import cache



app = Flask(__name__)

# configure my cache
app.config['CACHE_TYPE'] = 'SimpleCache'


# init cache
cache.init_app(app)



## import your blueprints here and register
app.register_blueprint(user.user_bp) 
app.register_blueprint(predict.predict_bp)


if __name__ == '__main__':
    app.run(debug=True)