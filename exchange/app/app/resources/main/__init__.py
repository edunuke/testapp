# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from .main import main


def register_blueprints(app):
    app.register_blueprint(main)