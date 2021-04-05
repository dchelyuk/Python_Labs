from Country import Country
from Category import Category


class DishwareItem:
    def __init__(self, price: float, _weight_in_g: float, country_origin: Country, _brand: str, _code: int, _name: str,
                 category: Category):
        self.price = price
        self._weight_in_g = _weight_in_g
        self.country_origin = country_origin
        self._brand = _brand
        self._code = _code
        self._name = _name
        self.category = category