import csv

from .fetch import get_json_data
from .fetch import download_csv


class KrxBase:
    def __init__(self):
        self._locale = 'ko_KR'
        self._csvxls_is_no = 'false'

    def fetch_json(self, params):
        params['csvxls_isNo'] = self._csvxls_is_no

        dic = get_json_data(params)

        return dic

    def fetch_data(self, params):
        print(params)
        bld = params.pop('bld')
        params['csvxls_isNo'] = self._csvxls_is_no
        params['name'] = 'fileDown'
        params['url'] = bld
        print(params)

        csv_str = download_csv(params)

        reader = csv.reader(csv_str.splitlines())
        data = list(reader)

        return data
