from datetime import datetime

from krxreader.calendar import is_closing_day
from krxreader.calendar import is_trading_day
from krxreader.calendar import trading_date


def test_is_closing_day():
    # 토요일
    dt1 = datetime.fromisoformat('2023-05-20 08:59:59.501235+09:00')
    # 일요일
    dt2 = datetime.fromisoformat('2023-05-21 08:59:59.501235+09:00')
    # 월요일
    dt3 = datetime.fromisoformat('2023-05-22 08:59:59.501235+09:00')

    assert is_closing_day(dt1) is True
    assert is_closing_day(dt2) is True
    assert is_closing_day(dt3) is False


def test_is_trading_day():
    # 토요일
    dt1 = datetime.fromisoformat('2023-05-20 08:59:59.501235+09:00')
    # 일요일
    dt2 = datetime.fromisoformat('2023-05-21 08:59:59.501235+09:00')
    # 월요일
    dt3 = datetime.fromisoformat('2023-05-22 08:59:59.501235+09:00')

    assert is_trading_day(dt1) is False
    assert is_trading_day(dt2) is False
    assert is_trading_day(dt3) is True


def test_trading_date():
    # 토요일
    dt1 = datetime.fromisoformat('2023-05-20 08:59:59.501235+09:00')
    dt2 = datetime.fromisoformat('2023-05-20 09:00:00.501235+09:00')
    dt3 = datetime.fromisoformat('2023-05-20 23:59:59.501235+09:00')

    assert trading_date(dt1) == '20230519'
    assert trading_date(dt2) == '20230519'
    assert trading_date(dt3) == '20230519'
    assert trading_date(dt1, open_time=24) == '20230519'
    assert trading_date(dt2, open_time=24) == '20230519'
    assert trading_date(dt3, open_time=24) == '20230519'

    # 일요일
    dt4 = datetime.fromisoformat('2023-05-21 08:59:59.501235+09:00')
    dt5 = datetime.fromisoformat('2023-05-21 09:00:00.501235+09:00')
    dt6 = datetime.fromisoformat('2023-05-21 23:59:59.501235+09:00')

    assert trading_date(dt4) == '20230519'
    assert trading_date(dt5) == '20230519'
    assert trading_date(dt6) == '20230519'
    assert trading_date(dt4, open_time=24) == '20230519'
    assert trading_date(dt5, open_time=24) == '20230519'
    assert trading_date(dt6, open_time=24) == '20230519'

    # 월요일
    dt7 = datetime.fromisoformat('2023-05-22 08:59:59.501235+09:00')
    dt8 = datetime.fromisoformat('2023-05-22 09:00:00.501235+09:00')
    dt9 = datetime.fromisoformat('2023-05-22 23:59:59.501235+09:00')

    assert trading_date(dt7) == '20230519'
    assert trading_date(dt8) == '20230522'
    assert trading_date(dt9) == '20230522'
    assert trading_date(dt7, open_time=24) == '20230519'
    assert trading_date(dt8, open_time=24) == '20230519'
    assert trading_date(dt9, open_time=24) == '20230519'
