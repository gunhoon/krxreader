import pandas as pd

from .fetch import get_json_data


class KrxStock:
    def __init__(self, date, market='ALL', share='1', money='1'):
        self.date = date.strftime('%Y%m%d')
        self.market = market  # 'ALL': 전체, 'STK': KOSPI, 'KSQ': KOSDAQ, 'KNX': KONEX
        self.share = share  # '1':주, '2':천주, '3':백만주
        self.money = money  # '1':원, '2':천원, '3':백만원, '4':십억원

        self.locale = 'ko_KR'
        self.csvxls_is_no = 'false'

    @staticmethod
    def get_output(params):
        dic = get_json_data(params)

        return pd.DataFrame(dic['OutBlock_1'])

    def screen_12001(self):
        """[12001] 전종목 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT01501&locale=ko_KR&mktId=ALL&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT01501'

        params = {
            'bld': bld,
            'locale': self.locale,
            'mktId': self.market,
            'trdDd': self.date,
            'share': self.share,
            'money': self.money,
            'csvxls_isNo': self.csvxls_is_no
        }
        df = self.get_output(params)

        return df

    def screen_12002(self):
        """[12002] 전종목 등락률

        bld=dbms/MDC/STAT/standard/MDCSTAT01602&locale=ko_KR&mktId=ALL&strtDd=20220818&endDd=20220826&adjStkPrc_check=Y&adjStkPrc=2&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12003(self):
        """[12003] 개별종목 시세 추이

        bld=dbms/MDC/STAT/standard/MDCSTAT01701&locale=ko_KR&tboxisuCd_finder_stkisu0_30=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_30=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_30=ALL&strtDd=20220818&endDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12004(self):
        """[12004] 종목 시세 추이(월/연도)

        bld=dbms/MDC/STAT/standard/MDCSTAT01802&locale=ko_KR&mktSelect=mkt&mktId=STK&tboxisuCd_finder_stkisu0_31=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_31=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_31=ALL&dateSel=mm&strtYy=2022&strtMm=07&endYy=2022&endMm=08&strtYymm=202207&endYymm=202208&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12005(self):
        """[12005] 전종목 기본정보

        bld=dbms/MDC/STAT/standard/MDCSTAT01901&locale=ko_KR&mktId=ALL&share=1&csvxls_isNo=fals
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT01901'

        params = {
            'bld': bld,
            'locale': self.locale,
            'mktId': self.market,
            'share': self.share,
            'csvxls_isNo': self.csvxls_is_no
        }
        df = self.get_output(params)

        return df

    def screen_12006(self):
        """[12006] 전종목 지정내역

        bld=dbms/MDC/STAT/standard/MDCSTAT02001&locale=ko_KR&mktId=ALL&csvxls_isNo=false
        """
        pass

    def screen_12007(self):
        """[12007] 개별종목 종합정보

        bld=dbms/MDC/STAT/standard/MDCSTAT02105&locale=ko_KR&tboxisuCd_finder_stkisu0_35=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_35=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_35=ALL&csvxls_isNo=false
        bld=dbms/MDC/STAT/standard/MDCSTAT02105&locale=ko_KR&tboxisuCd_finder_stkisu0_35=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_35=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_35=ALL&csvxls_isNo=false
        bld=dbms/MDC/STAT/standard/MDCSTAT02101&locale=ko_KR&tboxisuCd_finder_stkisu0_35=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_35=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_35=ALL&csvxls_isNo=false
        bld=dbms/MDC/STAT/standard/MDCSTAT02102&locale=ko_KR&tboxisuCd_finder_stkisu0_35=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_35=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_35=ALL&csvxls_isNo=false
        bld=dbms/MDC/STAT/standard/MDCSTAT02103&locale=ko_KR&tboxisuCd_finder_stkisu0_35=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_35=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_35=ALL&csvxls_isNo=false
        bld=dbms/MDC/STAT/standard/MDCSTAT02104&locale=ko_KR&tboxisuCd_finder_stkisu0_35=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_35=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_35=ALL&csvxls_isNo=false
        """
        pass

    def screen_12008(self):
        """[12008] 투자자별 거래실적

        bld=dbms/MDC/STAT/standard/MDCSTAT02201&locale=ko_KR&inqTpCd=1&trdVolVal=2&askBid=3&mktId=ALL&strtDd=20220819&endDd=20220826&share=2&money=3&csvxls_isNo=false
        """
        pass

    def screen_12009(self):
        """[12009] 투자자별 거래실적(개별종목)

        bld=dbms/MDC/STAT/standard/MDCSTAT02301&locale=ko_KR&inqTpCd=1&trdVolVal=2&askBid=3&tboxisuCd_finder_stkisu0_37=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_37=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_37=ALL&strtDd=20220819&endDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12010(self):
        """[12010] 투자자별 순매수상위종목

        bld=dbms/MDC/STAT/standard/MDCSTAT02401&locale=ko_KR&mktId=ALL&invstTpCd=1000&strtDd=20220819&endDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12011(self):
        """[12011] 대량매매(전일)

        bld=dbms/MDC/STAT/standard/MDCSTAT02501&locale=ko_KR&mktId=ALL&share=1&csvxls_isNo=false
        """
        pass

    def screen_12012(self):
        """[12012] 프로그램매매

        bld=dbms/MDC/STAT/standard/MDCSTAT02601&locale=ko_KR&mktId=ALL&strtDd=20220819&endDd=20220826&share=2&money=3&csvxls_isNo=false
        """
        pass

    def screen_12013(self):
        """[12013] REITs 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT02701&locale=ko_KR&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12014(self):
        """[12014] 뮤추얼펀드 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT02801&locale=ko_KR&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12015(self):
        """[12015] 선박투자회사 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT02901&locale=ko_KR&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12016(self):
        """[12016] 인프라투융자회사 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT03001&locale=ko_KR&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12017(self):
        """[12017] 수익증권 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT03101&locale=ko_KR&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12018(self):
        """[12018] 신주인수권증권 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT03201&locale=ko_KR&mktId=ALL&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12019(self):
        """[12019] 신주인수권증서 시세

        bld=dbms/MDC/STAT/standard/MDCSTAT03301&locale=ko_KR&mktId=ALL&trdDd=20220826&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12020(self):
        """[12020] 상장회사 상세검색

        bld=dbms/MDC/STAT/standard/MDCSTAT03402&locale=ko_KR&mktTpCd=0&tboxisuSrtCd_finder_listisu0_48=%EC%A0%84%EC%B2%B4&isuSrtCd=ALL&isuSrtCd2=ALL&codeNmisuSrtCd_finder_listisu0_48=&param1isuSrtCd_finder_listisu0_48=&sortType=A&stdIndCd=ALL&sectTpCd=ALL&parval=ALL&mktcap=ALL&acntclsMm=ALL&tboxmktpartcNo_finder_designadvser0_48=&mktpartcNo=&mktpartcNo2=&codeNmmktpartcNo_finder_designadvser0_48=&param1mktpartcNo_finder_designadvser0_48=&condListShrs=1&listshrs=&listshrs2=&condCap=1&cap=&cap2=&share=1&money=1&csvxls_isNo=false
        bld=dbms/MDC/STAT/standard/MDCSTAT03401&locale=ko_KR&mktTpCd=0&tboxisuSrtCd_finder_listisu0_48=%EC%A0%84%EC%B2%B4&isuSrtCd=ALL&isuSrtCd2=ALL&codeNmisuSrtCd_finder_listisu0_48=&param1isuSrtCd_finder_listisu0_48=&sortType=A&stdIndCd=ALL&sectTpCd=ALL&parval=ALL&mktcap=ALL&acntclsMm=ALL&tboxmktpartcNo_finder_designadvser0_48=&mktpartcNo=&mktpartcNo2=&codeNmmktpartcNo_finder_designadvser0_48=&param1mktpartcNo_finder_designadvser0_48=&condListShrs=1&listshrs=&listshrs2=&condCap=1&cap=&cap2=&share=1&money=1&csvxls_isNo=false
        """
        pass

    def screen_12021(self):
        """[12021] PER/PBR/배당수익률(개별종목)

        bld=dbms/MDC/STAT/standard/MDCSTAT03501&locale=ko_KR&searchType=1&mktId=ALL&trdDd=20220826&tboxisuCd_finder_stkisu0_50=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_50=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_50=ALL&strtDd=20220819&endDd=20220826&csvxls_isNo=false
        """
        pass

    def screen_12022(self):
        """[12022] 외국인보유량 추이

        bld=dbms/MDC/STAT/standard/MDCSTAT03601&locale=ko_KR&mktId=ALL&strtDd=20220819&endDd=20220826&share=2&money=3&csvxls_isNo=false
        """
        pass

    def screen_12023(self):
        """[12023] 외국인보유량(개별종목)

        bld=dbms/MDC/STAT/standard/MDCSTAT03701&locale=ko_KR&searchType=1&mktId=ALL&trdDd=20220826&tboxisuCd_finder_stkisu0_52=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_52=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_52=ALL&strtDd=20220819&endDd=20220826&share=1&csvxls_isNo=false
        """
        pass

    def screen_12024(self):
        """[12024] 업종별 분포

        bld=dbms/MDC/STAT/standard/MDCSTAT03801&locale=ko_KR&searchType=1&mktId=STK&trdDd=20220826&idxIndCd=005&strtDd=20220819&endDd=20220826&share=2&money=3&csvxls_isNo=false
        """
        pass

    def screen_12025(self):
        """[12025] 업종분류 현황

        bld=dbms/MDC/STAT/standard/MDCSTAT03901&locale=ko_KR&mktId=STK&trdDd=20220826&money=1&csvxls_isNo=false
        """
        pass

    def screen_12026(self):
        """[12026] 주식 대용가

        bld=dbms/MDC/STAT/standard/MDCSTAT04001&locale=ko_KR&searchType=1&mktId=ALL&trdDd=20220826&tboxisuCd_finder_stkisu0_55=005930%2F%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&isuCd=KR7005930003&isuCd2=KR7005930003&codeNmisuCd_finder_stkisu0_55=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&param1isuCd_finder_stkisu0_55=ALL&strtDd=20220819&endDd=20220826&csvxls_isNo=false
        """
        pass

    def screen_12027(self):
        """[12027] 수익증권 대용가

        bld=dbms/MDC/STAT/standard/MDCSTAT04101&locale=ko_KR&strtYy=2022&strtMm=08&searchType=1&strtYyBox1=2022&strtMmBox1=08&comNm=&isuNm=&strtYyBox2=2022&strtMmBox2=08&endYy=2022&endMm=08&csvxls_isNo=false
        """
        pass

    def screen_12028(self):
        """[12028] 뮤추얼펀드 대용가

        bld=dbms/MDC/STAT/standard/MDCSTAT04201&locale=ko_KR&strtYy=2022&strtMm=08&searchType=1&strtYyBox1=2022&strtMmBox1=08&comNm=&isuNm=&strtYyBox2=2022&strtMmBox2=08&endYy=2022&endMm=08&csvxls_isNo=false
        """
        pass
