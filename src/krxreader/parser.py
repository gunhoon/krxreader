import re

from bs4 import BeautifulSoup


def parse_main_page(html):
    soup = BeautifulSoup(html, 'html.parser')

    gnb_area = soup.find(id='jsGnbArea')
    mdi_menu_tags = gnb_area.find_all(name='a', href=re.compile('/contents/MDC/MDI/mdiLoader/index.cmd[?]menuId='))
    # mdi_menu_tags = gnb_area.find_all(name='a', attrs={'data-depth-menu-id': re.compile('')})

    menu_id_list = []

    for tag in mdi_menu_tags:
        # format : '/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201'
        menu_id = tag['href'].split('?')[1].split('=')[1]

        if menu_id == tag['data-depth-menu-id']:
            menu_id_list.append(menu_id)
            print(tag.string)

    return menu_id_list


def parse_mdi_page(html, menu_id):
    soup = BeautifulSoup(html, 'html.parser')

    mdi_menu = soup.find(id='jsMdiMenu')
    top_menu = mdi_menu.find(name='li', attrs={'data-depth-menu-id': menu_id})
    lnb_root = top_menu.find(name='ul', class_='lnb_tree_root')

    one_depth_tags = lnb_root.find_all(name='li', recursive=False)

    for tag in one_depth_tags:
        title = tag.find(name='a').string
        print(title)
        menu_tags = tag.find_all(name='a', attrs={'data-menu-id': re.compile('')})

        for menu in menu_tags:
            print(menu['data-menu-id'], menu.string)


def parse_screen_page(html):
    soup = BeautifulSoup(html, 'html.parser')

    soup.prettify()