from flask import Blueprint
from config import BASE_DIR

main = Blueprint('main', __name__, template_folder= BASE_DIR + "/templates")

from . import views