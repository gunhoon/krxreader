from .base import KrxBase


class Stock(KrxBase):
    """통계 > 기본 통계 > 주식

    :param date: 조회일자
    :param start: 조회기간
    :param end: 조회기간
    :param market: 'ALL': 전체, 'STK': KOSPI, 'KSQ': KOSDAQ, 'KNX': KONEX
    :param share: '1': 주, '2': 천주, '3': 백만주
    :param money: '1': 원, '2': 천원, '3': 백만원, '4': 십억원
    :param adjusted_price: 수정주가 적용
    """

    def __init__(
            self,
            date: str | None = None,
            start: str | None = None,
            end: str | None = None,
            market: str = 'ALL',
            share: str = '1',
            money: str = '1',
            adjusted_price: bool = True
    ):
        super().__init__(date, start, end)

        self._market = market
        self._share = share
        self._money = money
        self._adjusted_price = adjusted_price

    def stock_price(self) -> list[list]:
        """[12001] 통계 > 기본 통계 > 주식 > 종목시세 > 전종목 시세"""

        bld = 'dbms/MDC/STAT/standard/MDCSTAT01501'
        params = {
            'mktId': self._market,
            'trdDd': self._date,
            'share': self._share,
            'money': self._money
        }

        return self.fetch_data(bld, params)

    def stock_price_change(self) -> list[list]:
        """[12002] 통계 > 기본 통계 > 주식 > 종목시세 > 전종목 등락률"""

        bld = 'dbms/MDC/STAT/standard/MDCSTAT01602'
        params = {
            'mktId': self._market,
            'strtDd': self._start,
            'endDd': self._end
        }

        if self._adjusted_price is True:
            params.update({
                'adjStkPrc_check': 'Y',
                'adjStkPrc': '2'
            })
        else:
            params.update({
                'adjStkPrc': '1'
            })

        params.update({
            'share': self._share,
            'money': self._money
        })

        return self.fetch_data(bld, params)

    def price_by_issue(self, issue_code: str) -> list[list]:
        """[12003] 통계 > 기본 통계 > 주식 > 종목시세 > 개별종목 시세 추이"""

        (item_name, item_code, full_code) = self.search_item('stock', issue_code)

        bld = 'dbms/MDC/STAT/standard/MDCSTAT01701'
        params = {
            'tboxisuCd_finder_stkisu0_0': item_code + '/' + item_name,
            'isuCd': full_code,
            'isuCd2': 'KR7005930003',
            'codeNmisuCd_finder_stkisu0_0': item_name,
            'param1isuCd_finder_stkisu0_0': 'ALL',
            'strtDd': self._start,
            'endDd': self._end
        }

        if self._adjusted_price is True:
            params.update({
                'adjStkPrc_check': 'Y',
                'adjStkPrc': '2'
            })
        else:
            params.update({
                'adjStkPrc': '1'
            })

        params.update({
            'share': self._share,
            'money': self._money
        })

        return self.fetch_data(bld, params)

    def all_listed_issues(self) -> list[list]:
        """[12005] 통계 > 기본 통계 > 주식 > 종목정보 > 전종목 기본정보"""

        bld = 'dbms/MDC/STAT/standard/MDCSTAT01901'
        params = {
            'mktId': self._market,
            'share': self._share
        }

        return self.fetch_data(bld, params)
