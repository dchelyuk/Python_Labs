from DishwareItem import DishwareItem
from Country import Country
from Category import Category
from Material import Material
from typing import List


class Dish(DishwareItem):
    def __init__(self, price: float, _weight_in_g: float, _country_origin: Country, _brand: str, _code: int, _name: str,
                 _category: Category, _materials: List[Material]):
        super().__init__(price, _weight_in_g, _country_origin, _brand, _code, _name, _category)
        self._materials = _materials
