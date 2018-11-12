# -*- coding: utf-8 -*-
from utils.makesession import create_session
from bs4 import BeautifulSoup
from utils.mongomodel import DianPing, DianPingUrl

session = create_session()
num_map = {
    "gJfn": "3",
    "E0Nm": "5",
    "NGn0": "9",
    "HJ57": "4",
    "RU8P": "0",
    "VWa4": "2",
    "E8Ru": "6",
    "isg2": "8",
    "Pc2y": "7",
}
urls = [
    "http://www.dianping.com/chongqing/ch0/o2p{}",
    "http://www.dianping.com/chongqing/ch0/o3p{}",
    "http://www.dianping.com/chongqing/ch0/p{}",
]


def parse_item(url1):
    result = {}
    r = session.get(url1)
    if r.status_code != 200:
        return
    soup = BeautifulSoup(r.text, "lxml")

    lis = soup.find_all("li")
    for temp in lis:
        a = temp.find("a", {"data-click-name": "shop_title_click"})
        div = temp.find("div", {"class": "comment"})
        if div:
            span = div.find("span")
            xingji = span["title"]
            result["star_rank"] = xingji
            try:
                review_num = div.find("a", {"class": "review-num"}).text
                review_num = review_num.strip().split("\n")[0]
                result["review_num"] = review_num
            except:
                result["review_num"] = '0'
            mean_price = div.find("a", {"class": "mean-price"}).text
            mean_price = mean_price.strip().split("\n")[1]
            result["mean_price"] = mean_price
        span = temp.find("span", {"class": "addr"})
        if span:
            address = span.text
            result["address"] = address
        if a:
            tp = DianPingUrl.objects(url=a["href"])
            if tp:
                continue
            else:
                print('the crawling url is {}'.format(a['href']))
                res = parse_data(a["href"])
                result["name"] = a["title"]
                if res:
                    result.update(res)
                else:
                    result['phonenum'] = '0'
                into_db(result, a["href"])


def parse_data(url):
    result = {}
    r = session.get(url)
    if r.status_code != 200:
        return
    soup = BeautifulSoup(r.text, "lxml")
    info = soup.find("div", {"class": "brief-info"})
    if info:
        xingji = info.find("span")["title"]
        result['star_rank'] = xingji
    phone = soup.find("p", {"class": "expand-info tel"})
    if phone:
        spans = phone.find_all("span")
        tem = str(phone).split("</span>")
        ind = []
        for index, item in enumerate(tem):
            if item.strip().startswith("1"):
                ind.append(index)
        res = ""
        for span in spans:
            if span["class"][0].startswith("ww"):
                num = span["class"][0].split("-")[1]
                res = res + num_map[num]
        times = 0
        for item in ind:
            res = res[: item - 1 + times] + "1" + res[item - 1 + times :]
            times = times + 1
        result["phonenum"] = res
    else:
        span = soup.find('span', {'class': "call-number"})
        if span:
            result["phonenum"] = span.text
        else:
            div = soup.find('div', {"class": "info-value"})
            if div:
                result["phonenum"] = div.text
            else:
                try:
                    span = soup.find('span', {"class": "icon-phone"})
                    result['phonenum'] = span.text
                except:
                    result['phonenum'] = None
        try:
            span = soup.find('span', {'class': "score"})
            result["star_rank"] = span.text
        except:
            pass
    if result is None:
        div = soup.find('div', {"class": "shopinfor"})
        span = div.find('span')
        result["phonenum"] = span.text
    return result


def into_db(res, url):
    d = DianPing(
        name=res["name"],
        phonenumber=res["phonenum"],
        address=res["address"],
        star_rank=res["star_rank"],
        review_num=res["review_num"],
        mean_price=res["mean_price"],
    )
    d.save()
    du = DianPingUrl(url=url)
    du.save()


def crawl_url(url):
    page = 1
    while page < 51:
        url1 = url.format(page)
        print(url1)
        parse_item(url1)
        page = page + 1


def crawl():
    for url in urls:
        crawl_url(url)
    print('done')


if __name__ == '__main__':
    crawl()
