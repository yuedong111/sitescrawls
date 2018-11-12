# -*- coding: utf-8 -*-
# @Time : 2018/10/29 11:33
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : tongcheng.py

from utils.makesession import create_58session
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urlsplit
import json
from utils.mongomodel import TongCheng, TongChengId
from requests.exceptions import ReadTimeout, ConnectionError

session = create_58session()
city_url = "https://www.58.com/changecity.html"
city_detail = "https://{}.58.com/searchjob.shtml"
begin = False


def parse_item(url1):
    r = session.get(url1, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    div = soup.find("div", {"id": "infolist"})
    lis = div.find_all("li")
    for item in lis:
        dd = item.find("dd", {"class": "fl"})
        if dd:
            res = {}
            name = dd.find("span").text
            h = dd.find("a")
            # print(h['href'])
            url = h["href"]
            dep = {}
            ur = urlparse(url)
            r_i = ur.query.split("&")
            for item in r_i:
                dep[item.split('=')[0]] = item.split('=')[1]
            r_id = dep['dpid']
            # t = TongChengId.objects.filter(uid=r_id).first()
            # if t:
            #     print('!!!find deplicate item !!!', url)
            #     pass
            # else:
            try:
                dd = parse_data(url, r_id)
                res.update(dd)
                t = TongCheng(**res)
                t.save()
                TongChengId(uid=r_id).save()
            except Exception as e:
                print(url1)
                print(url)
                continue
    pageout = soup.find('div', {'class': 'pagerout'})
    aa = pageout.find_all('a')
    for item in aa:
        if 'class' in item.attrs and item['class'][0] == 'next':
            return item['href']
    return None


def parse_data(url, r_id):
    res = {}
    try:
        r = session.get(url, timeout=5)
    except:
        url = 'https:' + url
        r = session.get(url, timeout=5)
    res["uid"] = r_id
    soup = BeautifulSoup(r.content, "lxml")
    div1 = soup.find("div", {"class": "resDetailRight"})
    divs1 = div1.find_all("div")
    div = divs1[0]
    img = div.find("img")
    res["img"] = img["src"]
    name = div.find("span", {"id": "name"})
    res["name"] = name.text
    divs = div.find_all("div", {"class": "title-content"})
    ds = divs[1].find_all("div")
    res['expect_job'] = ds[1].text.strip()
    ds = divs[2].find_all("div")
    res['expect_place'] = ds[1].text.strip()
    t = ""
    for item in divs1[1:]:
        t = t + item.text
    res["detail"] = t
    return res


def parse_city():
    r = session.get(city_url)
    soup = BeautifulSoup(r.text, "lxml")
    head = soup.find("head")
    scs = head.find_all("script")
    paras = scs[2].text.split("var")
    indepent_city = paras[2].strip().split("=")[1]
    city_list = paras[3].strip().split("=")[1]
    indepent_city = json.loads(indepent_city)
    # for key in indepent_city:
    #     if indepent_city[key].split("|")[0].strip() != 'cq':
    #         continue
    #     c_d = city_detail.format(indepent_city[key].split("|")[0])
    #     parse_jobs(c_d)
    city_list = json.loads(city_list)
    for key in city_list:
        if key != "海外" and key != "其他":
            for c_key in city_list[key]:
                c_d = city_detail.format(city_list[key][c_key].split("|")[0])
                parse_jobs(c_d)


def check(url1):
    s = url1.split('.')
    city = s[0].split('//')
    job = s[-1].split('/')[1]
    if city[1] == 'yangchun' and job == 'qzyewu':
        return 'ok'
    r = session.get(url1, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    pageout = soup.find('div', {'class': 'pagerout'})
    aa = pageout.find_all('a')
    for item in aa:
        if 'class' in item.attrs and item['class'][0] == 'next':
            return item['href']
    return None


def jumppage(url1):
    r = session.get(url1, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    pageout = soup.find('div', {'class': 'pagerout'})
    aa = pageout.find_all('a')
    for item in aa:
        if 'class' in item.attrs and item['class'][0] == 'next':
            return item['href']
    return None


def parse_jobs(url):
    global begin
    r = session.get(url, timeout=5)
    soup = BeautifulSoup(r.text, "lxml")
    div = soup.find(
        "div", {"class": "types", "tongji_id": "ZP_searchjob_index_div_alllist"}
    )
    uls = div.find_all("ul")
    url1 = url.split('/')
    url1 = '/'.join(url1[:-1])
    for item in uls[:-1]:
        span = item.find("span")
        a = span.find("a")
        url2 = url1 + a["href"]
        while url2:
            print(url2)
            # save the url
            temp = url2
            if begin is False:
                if url2 == "https://yangchun.58.com/qzyewu":
                    begin = True
                else:
                    try:
                        url2 = check(url2)
                        if url2 != 'ok':
                            break
                        else:
                            url2 = temp
                            # to the destination per page
                            url2 = jumppage(url2)
                    except:
                        continue
                    print('pass:', url2)

            else:
                try:
                    url2 = parse_item(url2)
                except (ReadTimeout,ConnectionError):
                    print('timeout: ',url2)
                    # url2 = url2.split('/')
                    # url2[-2] = url2[-2][0:2] + str(int(url2[-2][2:]) + 1)
                    # url2 = '/'.join(url2)
                    continue


parse_city()
