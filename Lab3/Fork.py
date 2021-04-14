from Lab3.enums.Country import Country
from Lab3.enums.Category import Category
from Lab3.enums.Size import Size
from Lab3.enums.Purpose import Purpose
from Lab3.Cutlery import Cutlery


class Fork(Cutlery):
    def __init__(self, price: float, _weight_in_g: float, _country_origin: Country,
                 _brand: str, _code: int, _name: str, _category: Category, _size: Size,
                 _purpose: Purpose):
        super().__init__(price, _weight_in_g, _country_origin, _brand, _code, _name, _category, _size)
        self._purpose = _purpose
