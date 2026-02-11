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

class ItemJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return f"{o.l}: {o.wt}w.{o.vl}v{o.vw():.2f}"
        return super().default(o)
