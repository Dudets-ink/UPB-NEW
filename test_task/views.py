from flask import Blueprint, render_template, request


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    return '<h1> Amogus </h1>', 200