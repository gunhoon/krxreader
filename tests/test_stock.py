import pytest

from krxreader.stock import Stock


@pytest.mark.skipif(False, reason='requires http request')
def test_search_issue():
    stock = Stock()

    item = stock.search_issue('005930')
    assert item == ('삼성전자', '005930', 'KR7005930003')

    item = stock.search_issue('삼성전자')
    assert item == ('삼성전자', '005930', 'KR7005930003')

    item = stock.search_issue('035420')
    assert item == ('NAVER', '035420', 'KR7035420009')

    item = stock.search_issue('NAVER')
    assert item == ('NAVER', '035420', 'KR7035420009')


@pytest.mark.skipif(False, reason='requires http request')
def test_stock_price():
    stock = Stock('20240123', market='ALL')
    data = stock.stock_price()

    assert data[1][0] == '060310'
    assert data[1][5] == '4,100'

    stock = Stock('20240123', market='STK')
    data = stock.stock_price()

    assert data[1][0] == '095570'
    assert data[1][5] == '4,690'

    stock = Stock('20240123', market='KSQ')
    data = stock.stock_price()

    assert data[1][0] == '060310'
    assert data[1][5] == '4,100'

    stock = Stock('20240123', market='KNX')
    data = stock.stock_price()

    assert data[1][0] == '278990'
    assert data[1][5] == '12,300'


@pytest.mark.skipif(False, reason='requires http request')
def test_stock_price_change():
    stock = Stock(end='20240123')
    data = stock.stock_price_change()

    assert data[598][0] == '192080'  # ISU_SRT_CD (종목코드)
    assert data[598][2] == '43,358'  # BAS_PRC (시작일 기준가)
    assert data[598][3] == '40,450'  # TDD_CLSPRC (종료일 종가)

    stock = Stock(end='20240123', adjusted_price=False)
    data = stock.stock_price_change()

    assert data[598][0] == '192080'
    assert data[598][2] == '51,200'
    assert data[598][3] == '40,450'


@pytest.mark.skipif(False, reason='requires http request')
def test_price_by_issue():
    stock = Stock(end='20240123')
    data = stock.price_by_issue('035420')  # NAVER

    assert data[0][1] == 'TDD_CLSPRC'
    assert data[1][1] == '218,000'
    assert data[7][1] == '229,500'
