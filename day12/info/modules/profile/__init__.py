from flask import Blueprint

profile_blu = Blueprint("profile_blu", "__name__")

from . import view
