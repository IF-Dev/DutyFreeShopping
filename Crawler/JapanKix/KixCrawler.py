from requests_html import HTMLSession
import pandas as pd
import numpy as np
import re


session = HTMLSession()
url = 'https://www.kixdutyfree.jp/cn/Item/ItemList.aspx?brd_cd=SK2'
cssSelector = '.column_group_list > .item_box > .item_box_frame > .item_box_name,.item_box_cate,.item_box_txt > .item_box_price > span'
headers = ['品牌','产品名称','价格','货币']

def KIX_crawlingByProduct(url, selector, headers):
    # start the session
    response = session.get(url)
    while True:
		# print the result for the current page
        data = list(map(lambda x: x.text, response.html.find(selector)))
        array = np.array(data).reshape(-1, 4)
        print(array)
	    # check if exist next page
        if KIX_existNextPage(response):
            response = session.post(url, data = KIX_genDoPostbackParams(response))
            continue
        else:
            break

def KIX_genDoPostbackParams(response):
    # get html contains pagination value
    viewstate_html = response.html.find('#__VIEWSTATE', first=True)
    eventvalidation_html = response.html.find('#__EVENTVALIDATION', first=True)
    viewstategenerator_html = response.html.find('#__VIEWSTATEGENERATOR', first=True)
    # regex to take value from html 
    VIEWSTATE = KIX_regexValueFromHtml(viewstate_html)	
    EVENTVALIDATION = KIX_regexValueFromHtml(eventvalidation_html)
    VIEWSTATEGENERATOR = KIX_regexValueFromHtml(viewstategenerator_html)
    nextPageParams = dict(__EVENTTARGET="ctl00$cphMain$ucGoodsList$dpGoodsPage$ctl04$ctl00", __EVENTARGUMENT="", __LASTFOCUS="", __VIEWSTATE=VIEWSTATE, __VIEWSTATEGENERATOR=VIEWSTATEGENERATOR, __EVENTVALIDATION=EVENTVALIDATION)
    return nextPageParams
	
def KIX_existNextPage(response):
    nextPageBtn = response.html.search('ctl00$cphMain$ucGoodsList$dpGoodsPage$ctl04$ctl00')
    print(nextPageBtn)
    if nextPageBtn is not None:
        input("continue to show next page press enter")
        return True
    else:
        input("ooooops, no more pages")
        return False

def KIX_regexValueFromHtml(html):
    value = re.search(r'(?<=value=\').*(?=\'>)', str(html), re.I).group()
    return value
		
KIX_crawlingByProduct(url, cssSelector, headers)

'''
Testing urls:
    KIXDUTYFREE:
    https://www.kixdutyfree.jp/cn/Item/ItemList.aspx?brd_cd=SK2
    https://www.kixdutyfree.jp/cn/Item/ItemList.aspx?brd_cd=SDO
'''
