# he smell of paint, a flask of wine
# And turn those faces all to me
# The blunderbuss and halberd-shaft
# And Dutch respectability

from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound


APP_NAME = "Virtates"


def build_app(blueprints):
    app = Flask(APP_NAME)
    blueprints = build_blueprints()
    for bp in blueprints:
        app.register_blueprints(bp)
    return app


def build_blueprints():
    return [create_main_blueprint()]


def create_main_blueprint():
    main_page = Blueprint("main_page", APP_NAME, template_folder='templates')

    @main_page.route('/', defaults={'page': 'index'})
    @main_page.route('/<page>')
    def show(page):
        try:
            return render_template('pages/%s.html' % page)
        except TemplateNotFound:
            abort(404)

    return main_page
