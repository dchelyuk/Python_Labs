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
        for i in self.search_result:
            i.get_info()
        return self.search_result

    def sort_by_country(self, order: SortOrder):
        self.sorted_by_country = sorted(self.goods, key=lambda x: x.country_origin.value, reverse=order.value)
        for i in self.sorted_by_country:
            i.get_info()
        return self.sorted_by_country

    def sort_by_category(self, order: SortOrder):
        self.sorted_by_category = sorted(self.goods, key=lambda x: x.category.value, reverse=order.value)
        for i in self.sorted_by_country:
            i.get_info()
        return self.sorted_by_category
