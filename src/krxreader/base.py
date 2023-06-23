import csv
import datetime
import logging

from .calendar import now
from .calendar import trading_date
from .fetch import get_json_data
from .fetch import download_csv


class KrxBase:
    """Base Class for Stock, Index, Bond, etc.

    :param date: 조회일자
    :param start: 조회기간
    :param end: 조회기간
    """

    def __init__(
            self,
            date: str | None = None,
            start: str | None = None,
            end: str | None = None
    ):
        self._date = date
        self._start = start
        self._end = end

        now_dt = now()

        if self._date is None:
            self._date = trading_date(dt=now_dt)

        if self._end is None:
            self._end = trading_date(dt=now_dt)

        if self._start is None:
            dt = datetime.datetime.strptime(self._end, '%Y%m%d')
            dt = dt - datetime.timedelta(days=8)
            self._start = dt.strftime('%Y%m%d')

        self._locale = 'ko_KR'
        self._csvxls_is_no = 'false'

    def fetch_json(self, bld: str, params: dict) -> list[list]:
        payload = {
            'bld': bld,
            'locale': self._locale
        }
        payload.update(params)
        payload.update({
            'csvxls_isNo': self._csvxls_is_no
        })
        logging.debug(payload)

        dic_lst = get_json_data(payload)
        keys = list(dic_lst[0])

        data = [list(item.values()) for item in dic_lst]
        data.insert(0, keys)

        return data

    def fetch_csv(self, bld: str, params: dict) -> list[list]:
        payload = {
            'locale': self._locale
        }
        payload.update(params)
        payload.update({
            'csvxls_isNo': self._csvxls_is_no,
            'name': 'fileDown',
            'url': bld
        })
        logging.debug(payload)

        csv_str = download_csv(payload)

        reader = csv.reader(csv_str.splitlines())
        data = list(reader)

        return data

    def fetch_data(self, bld: str, params: dict) -> list[list]:
        return self.fetch_json(bld, params)

    def search_item(self, bld: str, params: dict) -> tuple:
        payload = {
            'locale': self._locale
        }
        payload.update(params)
        payload.update({
            'bld': bld
        })
        logging.debug(payload)

        dic_lst = get_json_data(payload)
        first_item = dic_lst[0]

        return (
            first_item['codeName'],
            first_item['short_code'],
            first_item['full_code']
        )
