from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from splent_framework.utils.form_helpers import form_error, form_success

from app.features.notepad import notepad_bp
from app.features.notepad.forms import NotepadForm
from app.features.notepad.services import NotepadService

notepad_service = NotepadService()

def form_success(endpoint, message, category="success", **url_kwargs):
    flash(message, category)
    return redirect(url_for(endpoint, **url_kwargs))


def form_error(template, form, errors=None, **context):
    for field, messages in (errors or {}).items():
        for msg in messages:
            flash(f"{field}: {msg}", "error")
    return render_template(template, form=form, **context)
