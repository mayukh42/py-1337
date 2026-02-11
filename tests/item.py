
from adt.item import Item, ItemJSONEncoder
import json

def test_item():
    i = Item("a", 23.0, 505)
    print(i)
    print(json.dumps(i, cls=ItemJSONEncoder, indent=4))


if __name__ == '__main__':
    test_item()
