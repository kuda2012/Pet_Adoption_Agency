from flask import Flask, request, render_template,  redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, validate_species, EditPetForm


app = Flask(__name__)

# # db.drop_all()
# db.create_all()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config["WTF_CSRF_ENABLED"] = True
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def list_pets():
    """Shows all pets"""
    pets = Pet.query.all()
    return render_template("list_pets.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pets():
    """Adds pet to the database if inputs meet requirments"""
    form = AddPetForm()
    if form.validate_on_submit() and validate_species(form):
        name = form.name.data
        species = form.species.data
        url = form.photo_url.data
        if url == "":
            url = "data:image/png;base64,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"
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species,
                      photo_url=url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added!")
        return redirect(url_for("list_pets"))
    else:
        if validate_species(form) == False and request.method == "POST":
            form.species.errors = "Invalid input: species must be a dog, cat, or porcupine"
        return render_template("add_pet.html", form=form)


@app.route("/<pet_id>", methods=["GET", "POST"])
def show_pet(pet_id):
    """Display details about given pet and give option to edit details"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    form.available.data = bool(form.available.data)
    if form.validate_on_submit():
        if form.photo_url.data != "":
            pet.photo_url = form.photo_url.data
        if form.notes.data != "":
            pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for("list_pets"))
    else:
        return render_template("show_pet.html", pet=pet, form=form)
