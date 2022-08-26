from datetime import datetime

import requests


def get_main_page():
    """MAIN 페이지

    :return: str
        html document
    """
    url = 'http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd'

    res = requests.get(url=url)
    html = res.text

    return html


def get_mdi_page(menu_id):
    """MDI 통계 화면 페이지

    :param:
    menu_id: str
        'MDC0201': 통계 > 기본 통계
        'MDC0202': 통계 > 이슈 통계
        'MDC0203': 통계 > 공매도 통계
        'MDC0204': 통계 > 통계DB 정보
        'MDC0301': 쉽계 보는 통계 > 주요 통계
        'MDC0302': 쉽계 보는 통계 > 순위 통계

    :return: str
        html document
    """
    url = f'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId={menu_id}'

    res = requests.get(url=url)
    html = res.text

    return html


def get_menu_info(menu_id):
    """메뉴 정보

    :param:
    menu_id: str
        'MDC0201010101': 지수 > 주가지수 > 전체지수 시세
        'MDC0201010102': 지수 > 주가지수 > 전체지수 등락률
        'MDC0201020101': 주식 > 종목시세 > 전종목 시세
        ......

    :return: dictionary
        {
            "controller":"menuLoader",
            "dir":"comm/menu",
            "title":"전체지수 시세",
            "url":"/contents/MDC/STAT/standard/MDCSTAT001.jsp",
            "screenId":"MDCSTAT001",
            "isMdi":"true",
            "screenNo":"11001",
            "cmd":"getMenuInfo",
            "id":"MDC0201010101"
        }
    """
    epoch = int(datetime.now().timestamp() * 1000)
    url = f'http://data.krx.co.kr/comm/menu/menuLoader/getMenuInfo.cmd?menuId={menu_id}&_={epoch}'

    res = requests.get(url=url)
    dic = res.json()

    return dic


def get_screen_page(screen_id):
    seq = 0  # TODO: 일단 0
    epoch = int(datetime.now().timestamp() * 1000)
    url = f'http://data.krx.co.kr/contents/MDC/STAT/standard/{screen_id}.jsp?viewSequence={seq}&_={epoch}'

    res = requests.get(url=url)
    html = res.text

    return html


def get_json_data(data):
    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    res = requests.post(url=url, data=data)
    dic = res.json()

    return dic


def download_csv(data):
    # 1. Generate OTP
    generate_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

    res = requests.post(url=generate_url, data=data)
    otp = {
        'code': res.text
    }

    # 2. Download CSV
    download_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'

    res = requests.post(url=download_url, data=otp)
    csv = res.content.decode(encoding='euc_kr')

    return csv
