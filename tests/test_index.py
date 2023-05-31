from krxreader.index import StockIndex
from krxreader.index import BondIndex


def test_index_price():
    index = StockIndex('20230519')
    data = index.index_price()

    assert data[1][0] == 'KRX 300'
    assert data[1][1] == '1533.13'


def test_index_price_change():
    index = StockIndex('20230519', start='20230511', end='20230519')
    data = index.index_price_change()

    assert data[1][0] == 'KRX 300'
    assert data[1][2] == '1533.13'


class TestBondIndex:
    def test_maintenance(self):
        index = BondIndex()
        data = index.index_price()

        assert len(data) == 4
        assert len(data[0]) == 14

    def test_index_price(self):
        index = BondIndex('20230526')
        data = index.index_price()

        assert data[1][0] == 'KRX 채권지수'
        assert data[1][1] == '180.37'

    def test_price_by_index(self):
        index = BondIndex(start='20230519', end='20230526')
        data = index.price_by_index('국고채프라임지수')

        assert data[1][0] == '2023/05/26'
        assert data[1][1] == '181.05'
