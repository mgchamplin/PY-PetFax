from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return ', PetFax!!'

    #Register
    from . import pet
    from . import fact

    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app