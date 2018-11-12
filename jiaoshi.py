# -*- coding: utf-8 -*-
# @Time : 2018/11/2 13:49
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : jiaoshi.py
from bs4 import BeautifulSoup
from utils.makesession import create_jiaoshisession
from utils.mongomodel import JiaoShi, JiaoShiId
from requests.exceptions import ConnectionError

session = create_jiaoshisession()
home = "http://www.jiaoshi.com.cn"
begin = "http://www.jiaoshi.com.cn/resume/resume_list/page/{}.html"


def parse_begin(url1):
    count = 0
    while count < 4:
        try:
            r = session.get(url1, timeout=5)
            break
        except ConnectionError:
            count = count + 1
            continue
    soup = BeautifulSoup(r.text, "lxml")
    divs = soup.find_all('div', {'class': 'J_resumeList yli'})
    for item in divs:
        res = {}
        div = item.find('div', {'class': 'td2 link_blue substring link_visited'})
        a = div.find('a')
        if a:
            res['name'] = a.text
            url = a['href']
            try:
                resu = parse_de(url)
                res['uid'] = url.split('/')[-1][:-5]
                res.update(resu)
            except:
                continue
            jsi = JiaoShiId.objects.filter(uid=res['uid']).first()
            if jsi:
                continue
        else:
            continue
        div = item.find('div', {'class': 'td3 substring'})
        ab = div.text.split('|')
        res['gender'] = ab[0]
        res['age'] = ab[1]
        res['edu'] = ab[2]
        res['work_years'] = ab[3]
        expect_job = item.find('div', {'class': 'td4 substring'})
        res['expect_job'] = expect_job.text
        expect_place = item.find('div', {'class': 'td5 substring'})
        res['expect_place'] = expect_place.text
        tem = item.find('div', {'class': 'txt font_gray6'})
        res['about'] = tem.text
        div = item.find('div', {'class': 'dlabs'})
        res['introduce'] = div.text.strip()
        img = item.find('img')
        res['img'] = home + img['src']
        JiaoShiId(uid=res['uid']).save()
        JiaoShi(**res).save()
        print(res)


def parse_de(url):
    res = {}
    r = session.get(url, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    de = soup.find('div', {'class': 'l'})
    edu = soup.find('div', {'class': 'edu'})
    edu = edu.find('div', {'class': 'td2 font_blue'})
    res['detail'] = de.text.strip()
    if edu:
        res['school'] = edu.text.strip()
    else:
        res['school'] = "未填写"
    return res


def crawl():
    i = 675
    while i < 1335:
        url = begin.format(i)
        print(url)
        parse_begin(url)
        i = i+1


crawl()