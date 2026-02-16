import json, sys
from functools import cmp_to_key, reduce
from dataclasses import dataclass

@dataclass
class Item:
    l: str
    wt: float
    vl: int

    def vw(self) -> float:
        return float(self.vl)/ self.wt
    
    def __repr__(self) -> str:
        return f"{self.l}: {self.wt}w.{self.vl}v{self.vw():.2f}"

# item lambdas
item_vw_az = lambda i1, i2: i1.vw() - i2.vw()
item_vw_za = lambda i1, i2: -item_vw_az(i1, i2)

item_w_az = lambda i1, i2: i1.w - i2.w
item_w_za = lambda i1, i2: -item_w_az(i1, i2)

# functions on array of items
item_sum_wt = lambda items: reduce(lambda x, y: x + y, map(lambda i: i.wt, items), 0)
item_sum_vl = lambda items: reduce(lambda x, y: x + y, map(lambda i: i.vl, items), 0)

item_labels = lambda items: "".join(map(lambda i: i.l, items))
items_map = lambda items: dict(map(lambda i: (i.l, i), items))


class ItemJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return f"{o.l}: {o.wt}w.{o.vl}v{o.vw():.2f}"
        return super().default(o)


@dataclass
class DPTCell:
    vl: int
    xs: []

    def __repr__(self) -> str:
        return f"{self.vl}v{self.xs}"
    
    def add(self, o):
        return DPTCell(self.vl + o.vl, self.xs + o.xs)

