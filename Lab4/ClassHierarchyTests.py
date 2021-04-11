import unittest
from Lab3.enums.Category import Category
from Lab3.enums.Country import Country
from Lab3.enums.Purpose import Purpose
from Lab3.enums.Shape import Shape
from Lab3.enums.Size import Size
from Lab3.enums.SortOrder import SortOrder
from Lab3.Fork import Fork
from Lab3.Material import Material
from Lab3.Plate import Plate
from Lab3.ShopManager import ShopManager


class TestShopManager(unittest.TestCase):
    def setUp(self):
        self.wood = Material("BukovynaWood", "wood")
        self.metal = Material("DniproAluminium", "Aluminium")
        self.ceramics = Material("SeoulCeramics", "Ceramics")
        self.fork1 = Fork(12.50, 120, Country.CN, "OG International", 34543675467, "ForkFun", Category.DT, Size.L,
                          Purpose.MAIN_COURSE)
        self.fork2 = Fork(17.50, 90, Country.DE, "Kids tableware", 86754957038, "Medium fork", Category.DT, Size.M,
                          Purpose.DESSERTS)
        self.plate1 = Plate(10.25, 300, Country.US, "Fantastic plates", 72485076934, "Oblong Plate", Category.BU,
                            [self.ceramics], Shape.OBLONG, 350, "ultramarine blue")
        self.plate2 = Plate(100.00, 150, Country.CN, "Wooden plates", 564783453453, "Wooden plate", Category.DT,
                            [self.wood, self.metal], Shape.ROUND, 400, "wooden")

        self.ShopManager = ShopManager([self.fork1, self.plate1, self.fork2, self.plate2])

    def tearDown(self):
        pass

    def test_search_by_country(self):
        self.assertEqual(self.ShopManager.search_by_country(Country.CN), [self.fork1, self.plate2])

    def test_sort_by_country(self):
        self.assertEqual(self.ShopManager.sort_by_country(SortOrder.ASCENDING),
                         [self.fork1, self.plate2, self.fork2, self.plate1])

        self.assertEqual(self.ShopManager.sort_by_country(SortOrder.DESCENDING),
                         [self.plate1, self.fork2, self.fork1, self.plate2])

    def test_sort_by_category(self):
        self.assertEqual(self.ShopManager.sort_by_category(SortOrder.ASCENDING),
                         [self.plate1, self.fork1, self.fork2, self.plate2])

        self.assertEqual(self.ShopManager.sort_by_category(SortOrder.DESCENDING),
                         [self.fork1, self.fork2, self.plate2, self.plate1])


if __name__ == '__main__':
    unittest.main()
