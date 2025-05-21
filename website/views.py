from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from csnews import (
    latestupdatetitle, update2title, update3title, update4title,
    latestupdateurl, update2url, update3url, update4url, latestupdatecontent, update2content, update3content, update4content
)


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML
        kda = request.form.get('kda') #Gets the kda from the HTML
        date = request.form.get('date') #Gets the date from the HTML
    
        
        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, kda=kda, gamedate=date, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/csnews', methods=['GET'])
@login_required
def csnews():
    return render_template("csnews.html", user=current_user, latestupdatetitle=latestupdatetitle, update2title=update2title, update3title=update3title, update4title=update4title, latestupdateurl=latestupdateurl, update2url=update2url, update3url=update3url, update4url=update4url, latestupdatecontent=latestupdatecontent, update2content=update2content, update3content=update3content, update4content=update4content)
