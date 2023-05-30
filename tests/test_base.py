import pytest

from krxreader.base import KrxBase


@pytest.fixture
def bld():
    """[12001] 주식 > 종목시세 > 전종목 시세
    :return: str
    """
    return 'dbms/MDC/STAT/standard/MDCSTAT01501'


@pytest.fixture
def params():
    """[12001] 주식 > 종목시세 > 전종목 시세
    :return: dictionary
    """
    return {
        'mktId': 'ALL',
        'trdDd': '20230519',
        'share': '1',
        'money': '1'
    }


def test_fetch_json(bld, params):
    payload = {
        'bld': bld,
        'locale': 'ko_KR'
    }
    payload.update(params)
    payload.update({
        'csvxls_isNo': 'false'
    })

    base = KrxBase()

    data_list = base.fetch_json(payload)
    keys = data_list[0].keys()

    data = [list(item.values()) for item in data_list]
    data.insert(0, list(keys))

    assert data[1][0] == '060310'
    assert data[1][5] == '2,290'


def test_fetch_data(bld, params):
    base = KrxBase()

    data = base.fetch_data(bld, params)

    assert data[1][0] == '060310'
    assert data[1][4] == '2290'
