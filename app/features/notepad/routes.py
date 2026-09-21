from flask import abort, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from splent_framework.utils.form_helpers import form_error, form_success

from app.features.notepad import notepad_bp
from app.features.notepad.forms import NotepadForm
from app.features.notepad.services import NotepadService

notepad_service = NotepadService()

'''
READ ALL
'''
@notepad_bp.route('/notepad', methods=['GET'])
@login_required
def index():
    form = NotepadForm()
    notepads = notepad_service.get_all_by_user(current_user.id)
    return render_template('notepad/index.html', notepads=notepads, form=form)


