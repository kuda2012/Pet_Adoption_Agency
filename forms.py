from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange


def validate_species(form):
    """Checks to ensure that entered species is a dog, cat, or porcupine"""
    if form.species.data == None:
        return False
    if form.species.data.lower() not in ["dog", "cat", "porcupine"]:
        return False
    else:
        return True


class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Name", validators=[InputRequired("Name is required")])
    species = StringField("Species", validators=[
                          InputRequired("Species is required")])
    photo_url = StringField("Photo Url")
    age = IntegerField("Age", validators=[NumberRange(
        min=0, max=30, message="Please enter an age between 0 and 30"), Optional()])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet"""
    photo_url = StringField("Photo Url")
    notes = StringField("Notes")
    available = RadioField("Available?", choices=[(True, "Yes"), (False, 'No')], validators=[
                           InputRequired("Please Select True or False")])
