from flask import (Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def fact_page():
    print("ADD A FACT ") 
    return render_template("facts.html") 