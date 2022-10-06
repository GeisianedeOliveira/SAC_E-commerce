from flask import Blueprint
from Controllers.message_controllers import index, create, home


message_bp = Blueprint('message_bp', __name__)
message_bp.route('/', methods=['GET'])(home)
message_bp.route('/all', methods=['GET'])(index)
message_bp.route('/sac', methods=['POST'])(create)
