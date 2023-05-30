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

    def fetch_json(self, payload: dict) -> list[dict]:
        logging.debug(payload)

        json = get_json_data(payload)
        keys = list(json.keys())

        key = keys[1] if keys[0] == 'CURRENT_DATETIME' else keys[0]
        logging.info(f'{key}')

        data = json[key]

        return data

    def fetch_data(self, bld: str, params: dict) -> list[list]:
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
