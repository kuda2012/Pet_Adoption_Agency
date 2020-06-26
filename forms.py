from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange



class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Name", validators=[InputRequired("Name is required")])
    species = StringField("Species", validators=[
                          InputRequired("Species is required"), AnyOf(["dog","cat","porcupine"], message="Please enter a dog, cat, or porcupine")])
    photo_url = StringField("Photo Url")
    age = IntegerField("Age", validators=[NumberRange(
        min=0, max=30, message="Please enter an age between 0 and 30"), Optional()])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet"""
    photo_url = StringField("Photo Url")
    notes = StringField("Notes")
    available = BooleanField("Available?")