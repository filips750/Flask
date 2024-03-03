from flask import request, Blueprint
from DB_wrappers.models import Menus
from app import app, db
from items_driver import get_items

menus = Blueprint('menus', __name__, template_folder='API_parts')


@menus.route('/menu')
@menus.get("/menu")
def get_menu():
    if request.args.get('id'):
        menu = Menus.query.filter_by(id=request.args.get('id')).first()
        return menu.to_dict()


@menus.get("/menu/items")
def get_menu_and_items():
    if request.args.get("id"):
        menu = Menus.query.filter_by(id=request.args.get('id')).first()
        return {
            "menu": menu,
            "items": get_items(menu.id)
        }


@menus.post("/menu")
def post_menu():
    if request.is_json:
        menu_to_add = request.get_json()
        if not (menu_to_add.get("restaurant_id")):
            return None

        with app.app_context():
            menu = Menus(restaurant_id=menu_to_add.get("restaurant_id"))
            db.session.add(menu)
            db.session.commit()
