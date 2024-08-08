from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    items = MenuItem.objects.all()
    current_url = request.path

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items.filter(parent=parent):
            item.children = build_menu_tree(items, parent=item)
            tree.append(item)
        return tree

    menu_items = build_menu_tree(items)

    def mark_active(item):
        if item.url == current_url:
            item.active = True
        else:
            item.active = False
        for child in item.children:
            mark_active(child)

    mark_active(menu_items)

    return menu_items