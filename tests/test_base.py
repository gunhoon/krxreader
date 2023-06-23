import pytest

from krxreader.base import KrxBase


@pytest.fixture
def bld():
    """[12001] 통계 > 기본 통계 > 주식 > 종목시세 > 전종목 시세"""

    return 'dbms/MDC/STAT/standard/MDCSTAT01501'


@pytest.fixture
def params():
    """[12001] 통계 > 기본 통계 > 주식 > 종목시세 > 전종목 시세"""

    return {
        'mktId': 'ALL',
        'trdDd': '20230602',
        'share': '1',
        'money': '1'
    }


@pytest.mark.skipif(True, reason='requires http request')
def test_fetch_json(bld, params):
    base = KrxBase()

    data = base.fetch_json(bld, params)

    assert data[1][0] == '060310'
    assert data[1][5] == '2,875'


@pytest.mark.skipif(True, reason='requires http request')
def test_fetch_csv(bld, params):
    base = KrxBase()

    data = base.fetch_csv(bld, params)

    assert data[1][0] == '060310'
    assert data[1][4] == '2875'


@pytest.mark.skipif(False, reason='requires http request')
def test_search_item():
    base = KrxBase()

    # 주가지수 검색
    bld = 'dbms/comm/finder/finder_equidx'
    params = {
        'mktsel': '1',
        'searchText': 'KRX 300'
    }

    item = base.search_item(bld, params)
    assert item == ('KRX 300', '300', '5')

    # 주식 종목 검색
    bld = 'dbms/comm/finder/finder_stkisu'
    params = {
        'mktsel': 'ALL',
        'typeNo': '0',
        'searchText': '삼성전자'
    }

    item = base.search_item(bld, params)
    assert item == ('삼성전자', '005930', 'KR7005930003')
