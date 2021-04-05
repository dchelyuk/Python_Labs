from DishwareItem import DishwareItem
from SortOrder import SortOrder
from Country import Country
from typing import List


class ShopManager:
    def __init__(self, goods: list):
        self.goods = goods

    def search_by_country(self, searched_country: Country):
        self.search_result = []
        for i in self.goods:
            if i.country_origin.value == searched_country.value:
                self.search_result.append(i)
        return self.search_result

    def sort_by_country(self, order: SortOrder):
        self.sorted_by_country = sorted(self.goods, key=lambda x: x.country_origin.value, reverse=order.value)
        return self.sorted_by_country

    def sort_by_category(self, order: SortOrder):
        self.sorted_by_category = sorted(self.goods, key=lambda x: x.category.value, reverse=order.value)
        return self.sorted_by_category
