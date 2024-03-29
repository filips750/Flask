from flask import request, Blueprint
from DB_wrappers.models import Menus, Restaurants
from app import app, db
from API_parts.items_driver import get_all_items_of_menu

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
            "items": get_all_items_of_menu(menu.id)
        }


@menus.post("/menu")
def post_menu():
    if request.is_json:
        menu_to_add = request.get_json()
        if not (menu_to_add.get("restaurant_id")):
            return {"error": "Request doesn't have all necessary fields"}, 406
        with app.app_context():
            restaurant = Restaurants.query \
                .filter_by(id=request.args.get('restaurant_id')) \
                .first()
            if not restaurant:
                return {"error": "Restaurant doesn't exist"}, 406
            other_menu = Menus.query \
                .filter_by(restaurant_id=menu_to_add.get("restaurant_id")) \
                .filter_by(isActive=True) \
                .first()
            if other_menu:
                return {"error": f"There is one other active menu. Deactivate the other menu first with id: {other_menu.id}."}
            menu = Menus(restaurant_id=menu_to_add.get("restaurant_id"))
            db.session.add(menu)
            db.session.commit()
            return menu


@menus.put("/menu")
def update_menu():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415
    menu_to_add = request.get_json()
    if not (menu_to_add.get("restaurant_id") and menu_to_add.get("new_state")):
        return {"error": "Request doesn't have all necessary fields"}, 406
    restaurant = Restaurants.query.get(menu_to_add.get("restaurant_id"))
    if not restaurant:
        return {"error": "Restaurant not found"}, 404
    menu = Menus.query \
        .filter_by(restaurant_id=menu_to_add.get("restaurant_id")) \
        .first()
    if not menu:
        return {"error": "Menu not found for the given restaurant"}, 404
    menu.is_active = menu_to_add.get("new_state")
    db.session.commit()
    return {"message": "Menu state updated successfully"}, 200
