import datetime

import pytest

from krxreader.base import _trading_date
from krxreader.base import KrxBase
from krxfetch.calendar import is_closing_day
from krxfetch.calendar import now


def test__trading_date():
    # 토요일
    dt1 = datetime.datetime.fromisoformat('2023-05-20 08:59:59.501235+09:00')
    dt2 = datetime.datetime.fromisoformat('2023-05-20 09:00:00.501235+09:00')
    dt3 = datetime.datetime.fromisoformat('2023-05-20 23:59:59.501235+09:00')

    assert _trading_date(dt1) == '20230519'
    assert _trading_date(dt2) == '20230519'
    assert _trading_date(dt3) == '20230519'
    assert _trading_date(dt1, base_hour=9) == '20230519'
    assert _trading_date(dt2, base_hour=9) == '20230519'
    assert _trading_date(dt3, base_hour=9) == '20230519'
    assert _trading_date(dt1, base_hour=24) == '20230519'
    assert _trading_date(dt2, base_hour=24) == '20230519'
    assert _trading_date(dt3, base_hour=24) == '20230519'

    # 일요일
    dt4 = datetime.datetime.fromisoformat('2023-05-21 08:59:59.501235+09:00')
    dt5 = datetime.datetime.fromisoformat('2023-05-21 09:00:00.501235+09:00')
    dt6 = datetime.datetime.fromisoformat('2023-05-21 23:59:59.501235+09:00')

    assert _trading_date(dt4) == '20230519'
    assert _trading_date(dt5) == '20230519'
    assert _trading_date(dt6) == '20230519'
    assert _trading_date(dt4, base_hour=9) == '20230519'
    assert _trading_date(dt5, base_hour=9) == '20230519'
    assert _trading_date(dt6, base_hour=9) == '20230519'
    assert _trading_date(dt4, base_hour=24) == '20230519'
    assert _trading_date(dt5, base_hour=24) == '20230519'
    assert _trading_date(dt6, base_hour=24) == '20230519'

    # 월요일
    dt7 = datetime.datetime.fromisoformat('2023-05-22 08:59:59.501235+09:00')
    dt8 = datetime.datetime.fromisoformat('2023-05-22 09:00:00.501235+09:00')
    dt9 = datetime.datetime.fromisoformat('2023-05-22 23:59:59.501235+09:00')

    assert _trading_date(dt7) == '20230522'
    assert _trading_date(dt8) == '20230522'
    assert _trading_date(dt9) == '20230522'
    assert _trading_date(dt7, base_hour=9) == '20230519'
    assert _trading_date(dt8, base_hour=9) == '20230522'
    assert _trading_date(dt9, base_hour=9) == '20230522'
    assert _trading_date(dt7, base_hour=24) == '20230519'
    assert _trading_date(dt8, base_hour=24) == '20230519'
    assert _trading_date(dt9, base_hour=24) == '20230519'


def test_date():
    base = KrxBase(end='20230623')
    assert base._start == '20230615'

    base = KrxBase(end='20230607')
    assert base._start == '20230530'

    base = KrxBase(end='20230605')
    assert base._start == '20230526'

    base = KrxBase(end='20230602')
    assert base._start == '20230525'

    base = KrxBase(end='20230601')
    assert base._start == '20230524'


def test_date_now():
    dt = now()

    if dt.hour < 9:
        dt = dt - datetime.timedelta(days=1)
    while is_closing_day(dt):
        dt = dt - datetime.timedelta(days=1)

    date = dt.strftime('%Y%m%d')

    dt = dt - datetime.timedelta(days=8)
    while is_closing_day(dt):
        dt = dt - datetime.timedelta(days=1)

    start = dt.strftime('%Y%m%d')

    print(f'{start} ~ {date}')

    base = KrxBase()
    assert base._date == date
    assert base._end == date
    assert base._start == start


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


@pytest.mark.skipif(False, reason='requires http request')
def test_fetch_json(bld, params):
    base = KrxBase()

    data = base.fetch_json(bld, params)

    assert data[1][0] == '060310'
    assert data[1][5] == '2,875'


@pytest.mark.skipif(False, reason='requires http request')
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
