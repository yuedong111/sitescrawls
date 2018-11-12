# -*- coding: utf-8 -*-
# @Time : 2018/10/31 14:22
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : ganji.py
from bs4 import BeautifulSoup
from utils.makesession import create_ganjisession
from utils.mongomodel import GanJi, GanJiId

session = create_ganjisession()
home = "http://anshan.ganji.com"
begin = False


class YanZhengException(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)


def parse_city():
    r = session.get("http://www.ganji.com/index.htm", timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    citys = soup.find_all('div', {'class': 'all-city'})
    dd = citys[1].find_all('dd')
    for item in dd:
        aa = item.find_all('a')
        if aa:
            for a in aa:
                yield a['href']


def parse_jobs():
    global begin
    for url in parse_city():
        tem = url.split('.')
        city = tem[0][7:].strip()
        if city != "dingxi":
            continue
        else:
            begin = True
        if begin:
            url1 = url + 'qiuzhi/'
            count = 0
            while count < 5:
                try:
                    r = session.get(url1, timeout=10)
                    break
                except:
                    count = count + 1
                    continue
            soup = BeautifulSoup(r.text, "lxml")
            div = soup.find('div', {'class': 'f-all-news'})
            try:
                dts = div.find_all('dt')
            except:
                continue
            for item in dts:
                a = item.find('a')
                if a:
                    url2 = url + a['href'][1:]
                    while True:
                        try:
                            parse_resume(url2)
                            break
                        except YanZhengException as e:
                            print('error:',url2)
                            print(e)
                        except:
                            break


def parse_resume(url):
    r = session.get(url, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    check = soup.find('div', {'class': 'seltion-cont'})
    if check is None:
        raise YanZhengException("需要验证!")
    div = soup.find('div', {'class': 'qz-resume-list'})
    dls = div.find_all('dl', {'class': 'list-noimg job-j-list clearfix job-new-list'})
    for dl in dls:
        res = {}
        img = dl.find('img')
        if img['src'].startswith('//'):
            img['src'] = 'http:' + img['src']
        res['img'] = img['src']
        name = dl.find('span', {'class': 'name'})
        res['name'] = name.text
        spans = dl.find_all('span')
        res['gender'] = spans[1].text
        res['age'] = spans[2].text
        res['edu'] = spans[3].text
        res['work_years'] = spans[4].text
        div = dl.find('div', {'class': 'fl district-salary'})
        district = div.find('p',{"class":'district'})
        res['expect_place'] = district.text.strip()
        salary = div.find('p', {"class": 'salary'})
        res['expect_salary'] = salary.text.strip()
        a = dl.find('a', {'class': 'fl'})
        d = a['href'].split('/')
        res['uid'] = d[-1][:-4]
        chec = GanJiId.objects.filter(uid=res['uid']).first()
        if chec:
            print('find a deplate', res['uid'])
            pass
        else:
            try:
                url = home + a['href']
                resu = parse_de(url)
                if resu:
                    res.update(resu)
            except:
                print('error:',url)
                GanJi(**res).save()
                GanJiId(uid=res['uid']).save()
                continue
            GanJi(**res).save()
            GanJiId(uid=res['uid']).save()


def parse_de(url):
    res = {}
    r = session.get(url, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    div = soup.find('div', {'class': "detail-info"})
    if div:
        res['detail'] = div.text
    return res



parse_jobs()
