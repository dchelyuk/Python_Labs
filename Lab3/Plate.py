from enums.Country import Country
from enums.Category import Category
from enums.Shape import Shape
from Dish import Dish
from Material import Material
from typing import List


class Plate(Dish):
    def __init__(self, price: float, _weight_in_g: float, _country_origin: Country,
                 _brand: str, _code: int, _name: str, _category: Category, _materials: List[Material],
                 _shape: Shape, _diameter_in_mm: int, _colour: str):
        super().__init__(price, _weight_in_g, _country_origin, _brand, _code, _name, _category, _materials)
        self._shape = _shape
        self._diameter_in_mm = _diameter_in_mm
        self._colour = _colour
