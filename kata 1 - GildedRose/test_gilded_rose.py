# -*- coding: utf-8 -*-
import unittest
import copy

from gilded_rose import Item, GildedRose
from gilded_rose_v2 import GildedRoseV2

items = [
    Item("Backstage passes to a TAFKAL80ETC concert", 10, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
    Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
    Item("Backstage passes to a TAFKAL80ETC concert", 11, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 10, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 6, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 1, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 0, 10),
    Item("Generic Item", 1, 1),
    Item("Generic Item", 0, 0),
    Item("Generic Item", -1, 10),
    Item("Aged Brie", 10, 10),
    Item("Aged Brie", 1, 10),
    Item("Aged Brie", 0, 10),
    Item("Aged Brie", -1, 10),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
    Item("Sulfuras, Hand of Ragnaros", 1, 80),
    Item("Sulfuras, Hand of Ragnaros", -1, 80),
]

expected = [
    Item("Backstage passes to a TAFKAL80ETC concert", 9, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", 9, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", 4, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", 10, 11),
    Item("Backstage passes to a TAFKAL80ETC concert", 9, 12),
    Item("Backstage passes to a TAFKAL80ETC concert", 5, 12),
    Item("Backstage passes to a TAFKAL80ETC concert", 4, 13),
    Item("Backstage passes to a TAFKAL80ETC concert", 0, 13),
    Item("Backstage passes to a TAFKAL80ETC concert", -1, 0),
    Item("Generic Item", 0, 0),
    Item("Generic Item", -1, 0),
    Item("Generic Item", -2, 8),
    Item("Aged Brie", 9, 11),
    Item("Aged Brie", 0, 11),
    Item("Aged Brie", -1, 12),
    Item("Aged Brie", -2, 12),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
    Item("Sulfuras, Hand of Ragnaros", 1, 80),
    Item("Sulfuras, Hand of Ragnaros", -1, 80),
]

items_v2 = copy.deepcopy(items) + [
    Item("Item conjured", 10, 10),
    Item("Conjured item", 0, 1),
]

expected_v2 = copy.deepcopy(expected) + [
    Item("Item conjured", 9, 8),
    Item("Conjured item", -1, 0),
]


class GildedRoseTest(unittest.TestCase):
    def test_update_quality(self):
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(expected, items)

    def test_update_quality_v2(self):
        gilded_rose = GildedRoseV2(items_v2)
        gilded_rose.update_quality()
        self.assertEquals(expected_v2, items_v2)


if __name__ == '__main__':
    unittest.main()
