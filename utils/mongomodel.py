# -*- coding: utf-8 -*-
# @Time : 2018/10/23 18:10
# @Author : chenpeng
# @Site : pengguoko@163.com
# @File : mongomodel.py
from mongoengine import Document, StringField, connect


connect("chenpeng", host="192.168.110.51", port=27017)


class DianPing(Document):
    name = StringField(required=True)
    phonenumber = StringField()
    address = StringField()
    star_rank = StringField()
    review_num = StringField()
    mean_price = StringField()


class DianPingUrl(Document):
    url = StringField(required=True)


class ZhiLianID(Document):
    zhilianid = StringField(required=True)


class ZhiLian(Document):
    name = StringField(required=True)
    userName = StringField()
    jobTitle = StringField()
    eduLevel = StringField()
    gender = StringField()
    isFemale = StringField()
    age = StringField()
    city = StringField()
    cityId = StringField()
    modifyDate = StringField()
    desiredSalary = StringField()
    careerStatus = StringField()
    workYears = StringField()
    school = StringField()
    employment = StringField()
    jobType = StringField()
    desireCity = StringField()
    major = StringField()
    zhilianid = StringField()
    label = StringField()
    labelNum = StringField()
    lastJobDetail = StringField()
    schoolDetail = StringField()
    portrait = StringField()
    havePhoto = StringField()
    t = StringField()
    k = StringField()
    version = StringField()
    language = StringField()
    hasRead = StringField()


class WuYou(Document):
    uid = StringField()
    age = StringField()
    work_years = StringField()
    gender = StringField()
    address = StringField()
    job_category = StringField()
    edu = StringField()
    updated = StringField()
    major = StringField()
    school = StringField()
    detail = StringField()
    img = StringField()


class WuYouId(Document):
    uid = StringField()


class TongChengId(Document):
    uid = StringField()


class TongCheng(Document):
    uid = StringField()
    img = StringField()
    name = StringField()
    detail = StringField()
    expect_job = StringField()
    expect_place = StringField()


class GanJi(Document):
    uid = StringField()
    name = StringField()
    img = StringField()
    gender = StringField()
    age = StringField()
    edu = StringField()
    work_years = StringField()
    expect_place = StringField()
    expect_salary = StringField()
    detail = StringField()


class GanJiId(Document):
    uid = StringField()


class JiaoShi(Document):
    uid = StringField()
    age = StringField()
    work_years = StringField()
    gender = StringField()
    expect_place = StringField()
    about = StringField()
    edu = StringField()
    detail = StringField()
    img = StringField()
    name = StringField()
    expect_job = StringField()
    introduce = StringField()
    school = StringField()



class JiaoShiId(Document):
    uid = StringField()