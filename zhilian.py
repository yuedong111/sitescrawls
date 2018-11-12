# -*- coding: utf-8 -*-
# @Time : 2018/10/25 8:52
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : zhilian.py
from utils.makesession import create_zhilian_session
import time
from utils.mongomodel import ZhiLian, ZhiLianID


session = create_zhilian_session()


def parse_item(page):
    d = str(time.time())
    d = d.split(".")
    now = d[0] + d[1][0:3]
    payload = {
        "start": page,
        "rows": 30,
        "S_DISCLOSURE_LEVEL": 2,
        "S_EXCLUSIVE_COMPANY": "新华三技术有限公司",
        "S_DATE_MODIFIED": "180425,181025",
        "S_CURRENT_CITY": "653",
        "S_ENGLISH_RESUME": "1",
        "isrepeat": 1,
        "sort": "complex_v15",
    }
    url = "https://rd5.zhaopin.com/api/custom/search/resumeList?_={}".format(now)
    r = session.post(url, json=payload)
    return r.json()


def parse_data():
    i = 0
    while i < 134:
        r = parse_item(i)
        for item in r["data"]["dataList"]:
            for key in item.keys():
                item[key] = str(item[key])
            tp = ZhiLianID.objects(zhilianid=item['id'])
            if tp:
                continue
            else:
                z = ZhiLian(
                    name=item["name"],
                    userName=item["userName"],
                    jobTitle=item["jobTitle"],
                    eduLevel=item["eduLevel"],
                    gender=item["gender"],
                    isFemale=item["isFemale"],
                    age=item["age"],
                    city=item["city"],
                    cityId=item["cityId"],
                    modifyDate=item["modifyDate"],
                    desiredSalary=item["desiredSalary"],
                    careerStatus=item["careerStatus"],
                    workYears=item["workYears"],
                    school=item["school"],
                    employment=item["employment"],
                    jobType=item["jobType"],
                    desireCity=item["desireCity"],
                    major=item["major"],
                    zhilianid=item["id"],
                    label=item["label"],
                    labelNum=item["labelNum"],
                    lastJobDetail=item["lastJobDetail"],
                    schoolDetail=item["schoolDetail"],
                    portrait=item["portrait"],
                    havePhoto=item["havePhoto"],
                    t=item["t"],
                    k=item["k"],
                    version=item["version"],
                    language=item["language"],
                    hasRead=item["hasRead"],
                )
                z.save()
                print('find a new item: ', item)
                u = ZhiLianID(zhilianid=item['id'])
                u.save()
        i = i + 1


parse_data()
