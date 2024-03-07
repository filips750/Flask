from flask import request, Blueprint
from DB_wrappers.models import Items
from app import app, db

items = Blueprint('items', __name__, template_folder='API_parts')


def get_all_items_of_menu(menu_id: int):
    items = Items.query() \
        .filter_by(menu_id=menu_id) \
        .all()
    return items


@items.post("/item")
def post_item():
    if request.is_json:
        item = request.get_json()
        if not (item.get("menu_id") and
                item.get("price") and
                item.get("name_of_item") and
                item.get("description_of_item")):
            return {"error": "Request doesn't have all necessary fields"}, 406

        with app.app_context():
            item_to_add = Items(
                menu_id=item.get("menu_id"),
                price=item.get("price"),
                name_of_item=item.get("name_of_item"),
                description_of_item=item.get("description_of_item")
                )
            db.session.add(item_to_add)
            db.session.commit()
