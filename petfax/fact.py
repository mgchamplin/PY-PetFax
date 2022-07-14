from flask import (Blueprint, render_template, request, redirect)
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def fact_page():
    print("ADD A FACT ") 
    return render_template("facts/facts.html") 

@bp.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == "POST"):
        print(request)
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect("/facts")

    # Do in case of GET or POST
    results = models.Fact.query.all()

    return render_template("facts/index.html", facts=results)