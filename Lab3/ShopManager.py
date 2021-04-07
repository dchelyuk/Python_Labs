from enums.Country import Country
from enums.SortOrder import SortOrder


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
        return sorted(self.goods, key=lambda x: x.country_origin.value, reverse=order.value)

    def sort_by_category(self, order: SortOrder):
        return sorted(self.goods, key=lambda x: x.category.value, reverse=order.value)
