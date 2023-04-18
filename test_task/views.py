from flask import Blueprint, render_template, request


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'POST':
        note_val = request.form['noteVal']
        
        note = Notes(user_id=current_user.id, text=note_val)
        db.session.add(note)
        db.session.commit()
    elif request.method == 'DELETE':
        note_id = request.form['noteId']
        note = Notes.query.filter_by(id=note_id).first()
        
        db.session.delete(note)
        db.session.commit()
    notes = Notes.query.filter_by(user_id=current_user.id).all() \
            if current_user.is_authenticated else ''
    
    return render_template('index.html', notes=notes)