# -*- coding: utf-8 -*-
# @Time : 2018/10/26 16:19
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : liepin.py
from PIL import Image, ImageEnhance
# import pytesseract
# img = Image.open('12.png')
# enh = ImageEnhance.Contrast(img)
# contrast = 2
# img_con = enh.enhance(contrast)
# img_con.show()
from utils.makesession import create_51session
from bs4 import BeautifulSoup
from utils.mongomodel import WuYou, WuYouId

home = "https://ehire.51job.com"
session = create_51session()

# text = pytesseract.image_to_string(img_con, lang='chi_sim')
# print(text)

def parse_data(url1):
    res = {}
    r = session.get(url1)
    soup = BeautifulSoup(r.text, "lxml")
    ta = soup.find("table", {"class": "box1"})
    img = ta.find("img")
    if img:
        if img["src"].startswith("//"):
            res["img"] = "https:" + img["src"]
        else:
            res["img"] = home + img["src"].strip()[img["src"].strip().find("/") :]
    else:
        res["img"] = ""
    try:
        div = soup.find("div", {"id": "divResume"})
        ta = div.find("table", {"class": "column"})
        tables = ta.find_all("table")
        resu = ""
        for table in tables:
            resu = resu + table.text
        res["detail"] = resu
    except Exception as e:
        pass
    print(res)
    return res

parse_data("https://ehire.51job.com/Candidate/ResumeView.aspx?hidUserID=183321137&hidEvents=23&pageCode=3&hidKey=d6c31deb7701aa31ce3120d718e2710a")