# blueprints/characters.py
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from ..models import Character, db
from ..ext.wtf import FlaskForm, StringField, SubmitField #this is probably a dumb way compared to just accessing the library

characters_bp = Blueprint('characters', __name__, url_prefix='/characters')

class CharacterForm(FlaskForm):
    name = StringField('Name')
    race = StringField('Race')
    character_class  = StringField('Class')
    submit = SubmitField('Create')


@characters_bp.route('/', methods=['GET'])
@login_required
def index():
    characters = Character.query.filter_by(user_id=current_user.id).all()
    return render_template('characters/index.html', characters=characters)

@characters_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = CharacterForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data #this needs to match the form, obviously
        character = Character(name=name, description=description, user_id=current_user.id)
        db.session.add(character)
        db.session.commit()
        return redirect(url_for('character.characters'))
    return render_template('characters/new.html', form=form)

@characters_bp.route('/<int:character_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(character_id):
    character = Character.query.filter_by(id=character_id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        character.name = request.form['name']
        db.session.commit()
        return redirect(url_for('characters.index'))

    return render_template('characters/edit.html', character=character)

@characters_bp.route('/<int:character_id>/delete', methods=['POST'])
@login_required
def delete(character_id):
    character = Character.query.filter_by(id=character_id, user_id=current_user.id).first_or_404()
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for('characters.index'))