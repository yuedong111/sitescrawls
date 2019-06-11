import requests
import json
import time
import base64
from apscheduler.schedulers.background import BackgroundScheduler

login = "https://ceshi.bikuex.io/tools/ajax.ashx?action=user_login&username={}&password={}&dx=&Ticket=t02tmQyK--OzAyI8nxfAwjd2-eaAd7oE33r89JE7LKbj3oR_e7H6c1L3-qt_NsDDVFME84Q1MgQhH1HrWah0K7EDV9PS9lSZBVd0OEwY6R_9tFNEqx-jnzfBw**&Randstr=@JHT"
recent_transactions = "https://api.huobi.pro/market/trade?symbol={}"
id_url = "https://bikuex.io/tools/ajax.ashx?action=get_trade_info"
transaction = "https://ceshi.bikuex.io/tools/ajax.ashx?action=tradeCoin&id={}&num={}&price={}&payPassword=&mold={}"
data_split_url = "https://www.huobi.co/-/x/pro/v2/beta/common/symbols?r=qlnzoo"


def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config


def query_data():
    search_data = load_config().get("huobi").get("recent_tranction")
    result = []
    for item in search_data:
        data = item.get("key")
        r = requests.get(recent_transactions.format(data), timeout=3)
        for tem in r.json().get("tick").get("data"):
            res = {}
            res["num"] = tem.get("amount")
            res["price"] = tem.get("price")
            flag = 1 if tem["direction"] == "sell" else 0
            res["mold"] = flag
            res["query_data"] = item.get("value")
            result.append(res)
    return result


def get_token():
    data = load_config()
    username = data.get("username")
    passwd = data.get("passwd")
    logurl = login.format(username, passwd)
    r = requests.get(logurl)
    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    return r.json().get("token"), cookies


def get_id(data):
    # r = requests.get(data_split_url, timeout=3)
    # for item in r.json().get("data"):
    #     if data == item["symbol_code"]:
    #         temp = item.get("display_name").split("/")
    #         d1 = temp[0].strip().lower()
    #         d2 = temp[1].strip().lower()
    #         break
    # else:
    #     return None
    temp = data.split("/")
    d1 = temp[0].strip().lower()
    d2 = temp[1].strip().lower()
    r = requests.get(id_url, timeout=3)
    for item in r.json().get("tradeList"):
        if item.get("name").lower() == d1 and item.get("tradename").lower() == d2:
            return item.get("id")
    return None


def create_session():
    s = requests.Session()
    token, cookies = get_token()
    s.headers = {"Authorization": "c " + token, "Origin": "http://47.244.40.222"}
    s.headers.update(cookies)
    return s


def post_data():
    datas = query_data()
    for data in datas:
        id = get_id(data["query_data"])
        if id:
            tranurl = transaction.format(id, data["num"], data["price"], data["mold"])
            if data["num"] * data["price"] > 2:
                session = create_session()
                try:
                    r = session.get(tranurl)
                    print(r.text)
                except Exception as e:
                    print(e)
            else:
                print("num is too small")


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_data, "interval", minutes=1)
    scheduler.start()
    try:
        while True:
            time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
