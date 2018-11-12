# -*- coding: utf-8 -*-
# @Time : 2018/10/24 14:58
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : wuyou.py
from utils.makesession import create_51session
from bs4 import BeautifulSoup
from utils.mongomodel import WuYou, WuYouId

home = "https://ehire.51job.com"
session = create_51session()


def sto(s):
    d = s.split("_")
    s = "$".join(d)
    return s


def parse_item(payload):
    for key in list(payload.keys()):
        if key != "__VIEWSTATE" and key != "__EVENTTARGET":
            del payload[key]
    payload["send_cycle"] = "1"
    payload["send_time"] = "7"
    payload["send_sum"] = "10"
    payload["ctrlSerach$hidIsRecDisplay"] = "1"
    payload["pagerTopNew$ctl06"] = "10"
    payload["cbxColumns$0"] = "AGE"
    payload["cbxColumns$1"] = "WORKYEAR"
    payload["cbxColumns$2"] = "SEX"
    payload["cbxColumns$3"] = "AREA"
    payload["cbxColumns$4"] = "WORKFUNC"
    payload["cbxColumns$5"] = "TOPDEGREE"
    payload["cbxColumns$6"] = "LASTUPDATE"
    payload["cbxColumns$11"] = "TOPMAJOR"
    payload["cbxColumns$12"] = "TOPSCHOOL"
    payload["hidStrAuthority"] = "0"
    payload["hidDownloadNum"] = "20"
    payload["hidKeywordCookie"] = ""
    payload["ctrlSerach$search_expectsalaryf_input"] = "不限"
    payload["ctrlSerach$search_expectsalaryt_input"] = "不限"
    payload["ctrlSerach$search_wyf_input"] = "不限"
    payload["ctrlSerach$search_wyt_input"] = "不限"
    payload["ctrlSerach$search_df_input"] = "不限"
    payload["ctrlSerach$search_dt_input"] = "不限"
    payload["ctrlSerach$search_cursalaryf_input"] = "不限"
    payload["ctrlSerach$search_cursalaryt_input"] = "不限"
    payload["ctrlSerach$search_age_input"] = "年龄"
    payload["ctrlSerach$search_expjobarea_input"] = "期望工作地"
    payload["ctrlSerach$search_forlang_input"] = "语言"
    payload["ctrlSerach$search_fl_input"] = "不限"
    payload["ctrlSerach$search_fllsabilityll_input"] = "不限"
    payload["ctrlSerach$search_englishlevel_input"] = "英语等级"
    payload["ctrlSerach$search_sex_input"] = "性别"
    payload["ctrlSerach$search_major_input"] = "专业"
    payload["ctrlSerach$search_hukou_input"] = "户口"
    payload["ctrlSerach$search_rsmupdate_input"] = "近1年"
    payload["ctrlSerach$search_jobstatus_input"] = "求职状态"
    payload["pagerTopNew$ctl06"] = "50"
    payload["ctrlSerach$hidIsRecDisplay"] = "1"
    # print(payload)
    r = session.post(
        "https://ehire.51job.com/Candidate/SearchResumeNew.aspx", data=payload
    )
    soup = BeautifulSoup(r.text, "lxml")
    div = soup.find("div", {"class": "Common_list-table"})
    trs = div.find_all("tr")
    for item in trs:
        tds = item.find_all("td")
        if len(tds) == 12:
            res = {}
            unid = WuYouId.objects(uid=tds[1].text)
            if unid:
                w = WuYou.objects.filter(uid=tds[1].text).first()
                if "detail" in w.to_mongo():
                    continue
                else:
                    a = tds[1].find("a")
                    url2 = home + a["href"]
                    try:
                        dd = parse_data(url2)
                        for key in dd.keys():
                            w.key = dd[key]
                        w.save()
                    except Exception as e:
                        print(e)
                        print(url2)
                        pass
            else:
                a = tds[1].find("a")
                url2 = home + a["href"]
                try:
                    dd = parse_data(url2)
                    res.update(dd)
                except Exception as e:
                    print(e)
                    print(url2)
                    pass
                res["uid"] = tds[1].text
                res["age"] = tds[2].text
                res["work_years"] = tds[3].text
                res["gender"] = tds[4].text
                res["address"] = tds[5].text
                res["job_category"] = tds[6].text
                res["edu"] = tds[7].text
                res["updated"] = tds[8].text
                res["major"] = tds[9].text
                res["school"] = tds[10].text
                w = WuYou(**res)
                w.save()
                wid = WuYouId(uid=res["uid"])
                wid.save()
                print("find a new person ", res)
    paydata = {}
    # inputs = soup.find_all('input', {"type": "hidden"})
    inputs = soup.find_all("input")
    for item in inputs:
        try:
            if item["value"]:
                paydata[item["name"]] = item["value"]
            else:
                paydata[item["name"]] = ""
        except:
            pass
    div = soup.find("div", {"class": "Search_page-numble"})
    manya = div.find_all("a")
    current_page = 0
    for item in manya:
        try:
            if item["class"] and item["class"][0] == "active":
                current_page = int(item["title"])
        except:
            pass
        try:
            if current_page:
                if item["title"] == str(current_page + 1):
                    paydata["__EVENTTARGET"] = sto(item["id"])
        except:
            pass
    return paydata, current_page


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


def next_page():
    r = session.get("https://ehire.51job.com/Candidate/SearchResumeNew.aspx")
    soup = BeautifulSoup(r.text, "lxml")
    # inputs = soup.find_all('input', {"type": "hidden"})
    inputs = soup.find_all("input")
    paydata = {}
    for item in inputs:
        try:
            if item["value"]:
                paydata[item["name"]] = item["value"]
            else:
                paydata[item["name"]] = ""
        except:
            pass
    div = soup.find("div", {"class": "Search_page-numble"})
    manya = div.find_all("a")
    current_page = 0
    for item in manya:
        try:
            if item["class"] and item["class"][0] == "active":
                current_page = int(item["title"])
        except:
            pass
        try:
            if current_page != 0:
                if item["title"] == str(current_page + 1):
                    paydata["__EVENTTARGET"] = sto(item["id"])
        except:
            pass
    return paydata, current_page


def crawl():
    payload, current_page = next_page()
    while current_page < 101:
        payload1, current_page1 = parse_item(payload)
        payload = payload1
        current_page = int(current_page1)
        print("the parse page is ", current_page)


crawl()
