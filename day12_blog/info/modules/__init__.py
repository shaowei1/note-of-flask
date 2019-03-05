from flask import Blueprint

blog_blu = Blueprint("blog_blu", __name__)

from . import view
