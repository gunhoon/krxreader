from krxreader.stock import Stock


def test_stock_price_all():
    stock = Stock('20230519', market='ALL')
    data = stock.stock_price()

    assert data[1][0] == '060310'
    assert data[1][4] == '2290'


def test_stock_price_stk():
    stock = Stock('20230519', market='STK')
    data = stock.stock_price()

    assert data[1][0] == '095570'
    assert data[1][2] == '4445'


def test_stock_price_ksq():
    stock = Stock('20230519', market='KSQ')
    data = stock.stock_price()

    assert data[1][0] == '060310'
    assert data[1][3] == '2290'


def test_stock_price_knx():
    stock = Stock('20230519', market='KNX')
    data = stock.stock_price()

    assert data[1][0] == '278990'
    assert data[1][3] == '6800'


def test_stock_price_change_adjusted():
    stock = Stock(start='20230517', end='20230525')
    data = stock.stock_price_change()

    assert data[1975][0] == '417500'
    assert data[1975][2] == '5252'


def test_stock_price_change_no_adjusted():
    stock = Stock(start='20230517', end='20230525', adjusted_price=False)
    data = stock.stock_price_change()

    assert data[1975][0] == '417500'
    assert data[1975][2] == '21000'


def test_all_listed_issues():
    stock = Stock('20230519')
    data = stock.all_listed_issues()

    assert data[1][0] == 'KR7098120009'
    assert data[1][11] == '8312766'
