from flask import (Blueprint, render_template)
import json

pets = json.load(open("pets.json"))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    print("MAIN PETS ROUTE")
    return render_template("index.html", pets=pets) 

@bp.route('/<int:pet_id>')
def pet_index(pet_id):
    print("SHOW ONE ROUTE for ",pet_id)
    one_pet = pets[ pet_id - 1] 
    return render_template("one_pet.html", one_pet=one_pet) 