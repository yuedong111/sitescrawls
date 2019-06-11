# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import json
import os
from io import UnsupportedOperation
from requests.exceptions import ConnectTimeout


class BiYingSearch(object):

    url = "https://cn.bing.com/search?q={0}&qs=n&sp=-1&pq={0}&sc=8-3&sk=&cvid=292A47B341EE4A78B13A7F6CAD091085&first={1}1&FORM=PERE"

    def __init__(self):
        config = self.load_config()
        self.search_name = config.get("search_name")
        self.search_num = int(config.get("search_num"))
        self.path = config.get("path")
        self.file_name = config.get("file_name")
        self.thread_num = int(config.get("thread_num"))
        self.output = os.path.join(self.path, self.file_name)
        self.unique = set()
        self.next_page = 0
        self.old_num = 0
        self.out = ["gov.com", "gov.cn", "gov.cc", "gov.net", "gov.com.cn"]


    @staticmethod
    def create_session():
        s = requests.Session()
        s.headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                      "image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,"
                               "ja;q=0.2,ru;q=0.2,gl;q=0.2,ko;q=0.2",
            "Pragma": "no-cache",
        }
        r = s.get("https://cn.bing.com/", timeout=3)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        cookie = ""
        for key, value in cookies.items():
            cookie = cookie + str(key) + "=" + str(value) + ";"
        cookie = cookie[0:-1]
        s.headers["cookie"] = cookie
        return s

    @staticmethod
    def load_config():
        with open("config.json", "r") as f:
            config = json.load(f)
        return config

    def crawl(self):
        count= 0
        while True:
            with open(self.output, "w+") as f:
                try:
                    temp = f.readlines()
                    number = len(temp)
                except UnsupportedOperation:
                    number = 0

            if number < self.search_num:
                self.search_num = self.search_num - number
                self.start(self.next_page)
            else:
                break
            if number == self.old_num and count == 3:
                print("已经是最大搜索条数")
                break
            self.old_num = number
            count = count + 1

    def parse_url(self, n):
        n = int(n)
        page = int(self.search_num / 10)
        temp = map(lambda x: (self.url.format(self.search_name, x), 10), range(n, n+page))
        urls = list(temp)
        num = int(self.search_num % 10)
        urls.append((self.url.format(self.search_name, page), num))
        return urls, page

    def search(self, data):
        url, num = data
        session = self.create_session()
        r = session.get(url, timeout=3)
        soup = BeautifulSoup(r.text, "lxml")
        info = soup.find_all("li", {"class": "b_algo"})
        temp = ""
        for item in info[:num]:
            a = item.find("a", {"target": "_blank"})
            try:
                r = requests.get(a["href"], timeout=2)
                if r.status_code == 404:
                    continue
            except ConnectTimeout:
                continue
            if "&" in a["href"]:
                a["href"] = a["href"][0: a["href"].find("&")]
            for out in self.out:
                if out in a["href"]:
                    break
            else:
                self.unique.add(a["href"])
                temp += a["href"] + "\n"
        with open(self.output, "a+") as f:
            f.write(temp)

    def start(self, cishu):
        urls, self.next_page = self.parse_url(cishu)
        pool = ThreadPoolExecutor(max_workers=self.thread_num)
        try:
            list(pool.map(self.search, urls))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    BiYingSearch().crawl()
