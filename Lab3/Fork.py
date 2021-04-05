from Cutlery import Cutlery
from Country import Country
from Category import Category
from Size import Size
from Purpose import Purpose


class Fork(Cutlery):
    def __init__(self, price: float, _weight_in_g: float, _country_origin: Country,
                 _brand: str, _code: int, _name: str, _category: Category, _size: Size,
                 _purpose: Purpose):
        super().__init__(price, _weight_in_g, _country_origin, _brand, _code, _name, _category, _size)
        self._purpose = _purpose
