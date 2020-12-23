from flask import Blueprint

bp = Blueprint('bands', __name__, url_prefix='/bands')
from . import routes
