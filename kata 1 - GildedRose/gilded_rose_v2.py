from gilded_rose import GildedRose


class GildedRoseV2(GildedRose):
    SULFURAS_ITEM_TYPE = "sulfuras"

    BACKSTAGE_ITEM_TYPE = "backstage passes"

    CONJURED_ITEM_TYPE = "conjured"

    AGED_BRIE_ITEM_NAME = "Aged Brie"

    MAX_QUALITY_VALUE = 50

    MIN_QUALITY_VALUE = 0

    @classmethod
    def quality_by_sell_in(cls, quality_value, sell_in):
        if sell_in < 0:
            return quality_value * 2
        else:
            return quality_value

    def update_quality(self):
        for item in self.items:
            if self.SULFURAS_ITEM_TYPE not in item.name.lower():
                item.sell_in = item.sell_in - 1
                if item.name == self.AGED_BRIE_ITEM_NAME:
                    item.quality = item.quality + self.quality_by_sell_in(1, item.sell_in)
                elif self.BACKSTAGE_ITEM_TYPE in item.name.lower():
                    if item.sell_in < 0:
                        item.quality = 0
                    elif item.sell_in < 5:
                        item.quality = item.quality + 3
                    elif item.sell_in < 10:
                        item.quality = item.quality + 2
                    else:
                        item.quality = item.quality + 1
                elif self.CONJURED_ITEM_TYPE in item.name.lower():
                    item.quality = item.quality - self.quality_by_sell_in(2, item.sell_in)
                else:
                    item.quality = item.quality - self.quality_by_sell_in(1, item.sell_in)

                if item.quality < self.MIN_QUALITY_VALUE:
                    item.quality = self.MIN_QUALITY_VALUE
                elif item.quality > self.MAX_QUALITY_VALUE:
                    item.quality = self.MAX_QUALITY_VALUE
