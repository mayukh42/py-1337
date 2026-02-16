
from adt.item import Item, ItemJSONEncoder, items_map
import json

def test_item():
    i = Item("a", 23.0, 505)
    print(i)
    print(json.dumps(i, cls=ItemJSONEncoder, indent=4))

    items = [
        Item("b", 2, 300),
        Item("c", 3, 400),
        Item("d", 4, 500)
    ]
    print(items_map(items))


if __name__ == '__main__':
    test_item()
