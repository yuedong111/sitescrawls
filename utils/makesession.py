# -*- coding: utf-8 -*-
import requests
from selenium import webdriver


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
        "Cookie": "s_ViewType=10; _lxsdk_cuid=1669f024259c8-01b23fa6ddc2be-333b5602-13c680-1669f02425ac8; _lxsdk=1669f024259c8-01b23fa6ddc2be-333b5602-13c680-1669f02425ac8; _hc.v=8520d5eb-a905-7705-dc26-50d098a0ecfc.1540266017; cy=9; cye=chongqing; _tr.u=Ur2LDLfgtz8L2Lhg; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic",
    }
    return s


def create_51session():
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
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://ehire.51job.com/Candidate/SearchResumeIndexNew.aspx",
        "Cookie": "guid=52d15567324650e89d79e262c709d1e2; EhireGuid=54c76091e58047dabe15d706b95b1add; LangType=Lang=&Flag=1; RememberLoginInfo=member_name=5215542FA2FE9B7D6C611B66AB9BA5DD&user_name=D9AD803B6EA1BAF1; slife=loginwarning%3D1%26%7C%26lowbrowser%3Dnot%26%7C%26; 51job=cenglish%3D0%26%7C%26; adv=adsnew%3D0%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Fsc.Kf0000jA5uApXoP2P-SnO2C-dhhwFY-16b6BG6UuvHk5mFoDnPsRZ7LsigWWLpPXu-DYTwe_DLFArp0EZhr1_6abfeAPIKQ6MKvCwD54_P6uQbIPH1tGJLK1Zq5DMbGJ4SaLEJ-Wag5rw1r2rUoi54z_P04excOAMhA3BENtDVHzLdYUnf.Db_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_IrS8z81J1-k_nOEOlecxLO3MHSEwECntx135zOCxgvg45E6OeAHxfOgkOdkxo3O-CLOWEWEzgxwOsr5Oml5dlpoQOvSajSw7OVxwxS9yOO_xVYXveqElqEgVmvfdG_H3en-dvHFIjxvuQVOB-MFb8lRq5uEtN2s1f_NvI5WbR0.U1Yk0ZDq1VeHksKspynqnfKY5TeXYtT0pyYqnWcd0ATqmhNsT1D0Iybqmh7GuZR0TA-b5Hnz0APGujYzrj00UgfqnH0krNtknjDLg1DsPjwxn1msnfKopHYs0ZFY5H63n0K-pyfqnHfdnNtznH0LrNtzPWndn7tzP1RsrfKBpHYznjf0UynqnH0snNtLrHTsn1czn1NxnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYzPjf1P1mdPjf0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1YkPj01PW6krj0snHnzPWfznjmdPfKzug7Y5HDdPjDkPHm1nW0zPjD0Tv-b5yDvPWTLryFbnj0snjfsm160mLPV5Rm3wWbvPWb4fbDkwDPafWn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1KxnH0YP-ts0Aw9UMNBuNqsUA78pyw15HKxn7t1nHcvrjbkg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YYnHT3nf%2526winfo%253D%25408632812943%2540%2526ck%253D4704.1.132.230.154.230.144.430%2526shh%253Dwww.baidu.com%2526sht%253Dbaidu%2526us%253D1.0.1.0.1.301.0%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526oq%253Dpycharm%252525E6%2525259B%252525BF%252525E6%2525258D%252525A2%2526rqlang%253Dcn%2526inputT%253D1240%2526bc%253D110101%26%7C%26adsnum%3D691010; ASP.NET_SessionId=zz5krlczaagidigqhrunznss; AccessKey=cd87a72b80a1426; HRUSERINFO=CtmID=257960&DBID=1&MType=06&HRUID=1964508&UserAUTHORITY=1000110010&IsCtmLevle=0&UserName=rdbjwx&IsStandard=1&LoginTime=11%2f06%2f2018+18%3a22%3a58&ExpireTime=11%2f06%2f2018+18%3a32%3a58&CtmAuthen=0000011000000001000111010000000011100011&BIsAgreed=true&IsResetPwd=0&CtmLiscense=10&AccessKey=1ffa8c03175035fe&source=0; KWD=SEARCH=",
    }
    return s


def create_zhilian_session():
    s = requests.Session()
    s.headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                  "image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,"
                           "ja;q=0.2,ru;q=0.2,gl;q=0.2,ko;q=0.2",
        "Pragma": "no-cache",
        "Content-Length": "210",
        "Content-Type": "text/plain",
        "zp-route-meta": "uid=106274073,orgid=14690842",
        "Referer": "https://rd5.zhaopin.com/custom/search/result",
        "Host": "rd5.zhaopin.com",
        "Origin": "https://rd5.zhaopin.com",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "loginName=h3crdhz; sts_deviceid=166a93260d8216-01c3c9de273c0f-5c10301c-1296000-166a93260da692; login_point=14690842; NTKF_T2D_CLIENTID=guestB7D638DC-C542-3924-4C02-A94A81035C31; diagnosis=0; adfbid2=0; urlfrom2=121113803; adfcid2=pzzhubiaoti; urlfrom=121113803; adfcid=pzzhubiaoti; adfbid=0; ZP_OLD_FLAG=false; dywec=95841923; __utmc=269921210; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0gHFI0KqiAsjXMVVU000005WhvNb00000X8A061.THLyktAJ0A3qmh7GuZR0T1dWPj7-m1cznW0snjKWPH7B0ZRqrRm1nRRzPbfvnYwAPbRYPRwjrRndPRcvwj-awjD3nDf0mHdL5iuVmv-b5HnkPj0YrjT1PHmhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh99ULKGUB4WUvYOTv-b5HDznHDkn16snzu1pgw-5gKlXh9dmh-9ULwG0APzm1Yzns%26tpl%3Dtpl_11535_17772_13457%26l%3D1507452664%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3140487356_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D171%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%2599%25BA%25E8%2581%2594%26oq%3D%2525E7%25258C%25258E%2525E8%252581%252598%26rqlang%3Dcn%26inputT%3D1063; _jzqc=1; puid=1016976925; nTalk_CACHE_DATA={uid:kf_9051_ISME9754_14690842,tid:1541121542946168}; rd_resume_srccode=402101; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22106274073%22%2C%22%24device_id%22%3A%22166a9326225582-05934ac76ec14f-5c10301c-1296000-166a93262277d9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0gHFI0KqiAs0vSSKU000005WhvNb00000X8A061.THdlpA-_py780A3qmh7GuZR0T1d9nWDLuhnkmW0snjDvPhc10ZRqrRm1nRRzPbfvnYwAPbRYPRwjrRndPRcvwj-awjD%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22zhilian%22%2C%22%24latest_utm_source%22%3A%22other%22%2C%22%24latest_utm_medium%22%3A%22cnt%22%2C%22%24latest_utm_campaign%22%3A%22121113803%22%7D%2C%22first_id%22%3A%22166a9326225582-05934ac76ec14f-5c10301c-1296000-166a93262277d9%22%7D; dywea=95841923.1322791366820430000.1540436943.1541119718.1541471070.9; dywez=95841923.1541471070.9.7.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=zhilian; __xsptplusUT_30=1; __utmz=269921210.1541471072.10.7.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=zhilian; __utma=269921210.1585427066.1540436943.1541121228.1541471072.10; __utmt=1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1541051507,1541119719,1541121168,1541471072; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1541471072; sts_sid=166e6d5eee7200-04794fd3aa17fb-5c11301c-1296000-166e6d5eee8763; __xsptplus30=30.7.1541471073.1541471073.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23oIK5Fi6j7Lej6cx8GeDuQimCabuX2DkN%23; _jzqa=1.4351786122854446000.1540438889.1541119719.1541471076.5; _jzqy=1.1540774180.1541471076.3.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.jzqsr=baidu|jzqct=zhilian; _jzqckmp=1; _jzqb=1.1.10.1541471076.1; rememberMe=true; at=cfd5a3b632604476a7a6b610422bae77; Token=cfd5a3b632604476a7a6b610422bae77; rt=d009668f17a24d4ea4d775b289c40e9a; RDsUserInfo=386b2e69567146655f700369476d5c6a5d6b4177526f43355275216b246956711f655c705669076d0f6a016b0b775e6f25352775506b7e11ba221a02b12d0e69266d3f6a546b40775e6f32352d75506b5b695f714165567005694d6d5f6a5b6b4a77246f243554755c6b5b69467141654f700469456d516a5b6b44775e6f31352575506b5a69507122652e7008693f6d396a596b4777576f47355d755d6b5d695871436554706069216d566a586b4777556f4b353a75246b57695b714c659; uiioit=3d79306c4d73556554644164033253684d745c70446456645f77263176645579456c447352655d644764093250684b7457702; zp-route-meta=uid=106274073,orgid=14690842; dyweb=95841923.8.6.1541471121040; __utmb=269921210.8.6.1541471121042; rd_resume_actionId=1541471302437106274073; sts_evtseq=8",
    }
    return s


def create_58session():
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
        "cookie": """f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; id58=nwrd21vP6eeI8VytctesAA==; mcity=hz; 58tj_uuid=af3f5bff-e157-4ac8-8ef7-bac7c7c5dd5b; 58home=hz; city=hz; wmda_new_uuid=1; wmda_uuid=f9632e0ca637e29fb2a2e3aabb11c6f4; wmda_visited_projects=%3B1731916484865; als=0; param8616=0; param8716kop=1; xxzl_deviceid=OSaCMtOHxLjTHy%2BJHUqg8bp9DSgpY%2BqUCc3q23mko28mGAevjQYq5VXLecFVjpQf; showOrder=1; sessionid=77d171bb-c5cb-4d69-859a-b3fabdcfac70; wmda_session_id_1731916484865=1541127181505-ead14d86-3e0e-ec35; new_uv=5; utm_source=; spm=; init_refer=; new_session=0; PPU="UID=59115994764820&UN=hth5qoq0y&TT=d875623cbe10dba777247113fb29a2a0&PBODY=WW9f4F5F_GwUxLhjBjIZn3ycvKhhOwUO8fjwV2R90PdJW1d_qqL4BLpsL1UuUuQorDc81gvq8O50mNPyklgnPukO4cC2CIQPPv5hCAxcUud1MjnfFmuju2AoLID75_S0fnWOd16xsC3fgJZOFld_xr84a3zX70QSvOc5Zu72usU&VER=1"; www58com="UserID=59115994764820&UserName=hth5qoq0y"; 58cooper="userid=59115994764820&username=hth5qoq0y"; 58uname=hth5qoq0y; ppStore_fingerprint=8B324D3AE3F1B628D3AB427D4FB736A0009C5254912C3A71%EF%BC%BF1541127374557; ljrzfc=1; f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=hz%7C%E6%9D%AD%E5%B7%9E%7C0; xxzl_smartid=a2f4fe7a4d557b3a7906c5c584f2454d; JSESSIONID=D20C8302F4BF513133E96F95226998B3; jl_list_left_banner=3; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1540370494,1541127569; Hm_lpvt_a3013634de7e7a5d307653e15a0584cf=1541127569""",
    }
    return s


def create_ganjisession():
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
        "Cookie": "statistics_clientid=me; ganji_uuid=3848376959766716296216; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A31973882941%7D; ganji_xuuid=b1cfa5c9-696d-436c-9145-5b0d814f1e0a.1541033573904; GANJISESSID=5dbvr1l8kjaofc9lc5pu9aqgp9; lg=1; __utma=32156897.1717435706.1541033583.1541033583.1541033583.1; __utmc=32156897; __utmz=32156897.1541033583.1.1.utmcsr=hz.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; xxzl_deviceid=8Dc6NrRULjBrXIZmg3jSrLUVunCuaMz31A%2FbbGvu%2BOGColzIEwwT4jEWQ%2F1sBbfY; sscode=VPWrTCJMIcyopXMTVPIxaFcE; GanjiUserName=chpeng1; GanjiUserInfo=%7B%22user_id%22%3A802551685%2C%22email%22%3A%22%22%2C%22username%22%3A%22chpeng1%22%2C%22user_name%22%3A%22chpeng1%22%2C%22nickname%22%3A%22%22%7D; bizs=%5B%5D; supercookie=BQNlAGHkAwt1WTAvZmyvAwt3LmV2AmSyZwL3LmtkZTLlZ2LlMJWwBQNmAmqzMJRjZzL%3D; LastLoginTime=118-11-1; xxzl_smartid=793605680a068cc11c4bbf51977276bf; citydomain=hz; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1541033757; ganji_login_act=1541033760548; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1541033761; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1541033761; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1541033761; __utmb=32156897.5.10.1541033583; xzfzqtoken=YHz4dUnaCU9iHRK4zBD5tTK1B0wkiJOq%2FGCklpvG9sq%2BzK%2F0psXD%2BiYYI3in1G65in35brBb%2F%2FeSODvMgkQULA%3D%3D",
    }
    return s


def create_jiaoshisession():
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
        "Cookie": "PHPSESSID=q0kc0rn2g6u0a0af9v5ecmima5; think_language=zh-CN; Hm_lvt_a80ca2e71dadaf4eeb7bac424f55db43=1541137497; _subsite_domain=http%3A%2F%2Fwww.jiaoshi.com.cn; _qscms111e6c4d86d3e03bc9141216dd8b7106=think%3A%7B%229871d3a2c554b27151cacf1422eec048%22%3A%22711645%22%2C%225f4dcc3b5aa765d61d8327deb882cf99%22%3A%22afd7a48ec233549c0a03bde6504ac5d3%22%7D; think_template=chqs; Hm_lpvt_a80ca2e71dadaf4eeb7bac424f55db43=1541137812",
    }
    return s


def create_webdriver() -> webdriver.Chrome:
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('window-size=1280,720')
    d = webdriver.Chrome(chrome_options=opt)
    return d


OPTIONS_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "rdapi.zhaopin.com",
    "Origin": "https://rd5.zhaopin.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Cookie": "adfbid=0; adfbid2=0; dywec=95841923; ZP_OLD_FLAG=false; __utmc=269921210; sts_deviceid=166a41a2cf888d-077def58536741-5c10301c-1296000-166a41a2cf97f8; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0gHFI0KqiAsah4TqU000005WhvNb00000X8A061.THLyktAJdIjA80K85yF9pywd0ZnquWnYn1m1mWRsnj0kP1RknsKd5H-An177nWuDPWPDwWu7PjNDf1-jPHNaPbf4fbfkrjKD0ADqI1YhUyPGujY1nHfsPj6Ln1RvFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQMGCmyqspy38mvqV5LPGujYknWDknHn3njnhTv-YuHdsXMGCIyFGmyqYpfKWThnqPHbdnWb%26tpl%3Dtpl_11535_17772_13457%26l%3D1507452664%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3140487356_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D171%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3Dmongodbcollection%2525E5%252588%2525A0%2525E9%252599%2525A4%26rqlang%3Dcn%26inputT%3D6200%26bs%3Dmongodbcollection%25E5%2588%25A0%25E9%2599%25A4; _jzqc=1; _jzqckmp=1; ZP_P_VERSION=v2; firstchannelurl=https%3A//passport.zhaopin.com/login; lastchannelurl=https%3A//ts.zhaopin.com/jump/index_new.html%3Futm_source%3Dother%26utm_medium%3Dcnt%26utm_term%3D%26utm_campaign%3D121113803%26utm_provider%3Dzp%26sid%3D121113803%26site%3Dpzzhubiaoti; qrcodekey=5a02ba4fdf384ca9b8d19e3c3d77b60f; JsNewlogin=2034202397; JSloginnamecookie=17783886899; JSShowname=%E9%99%88%E6%9C%8B; JSsUserInfo=236a2d6b566a5c645f6951755572537346765e695d6b5f6a5f6825693b654f654271416a5e6b536a59645069517553725d7348765369506b3f6a2a6854693df379024871336a246b566a02640b69017500720b7301760f69056b0d6a24685869436541655d71156a066b066a51643b693d75587254734a762b693f6b576a5d684469466552654271476a536b596a5f645369287529725873417651693e6b2b6a59682369386545654b71466a5f6b5c6a5e645e695c7555725e7324763e69566b5b6a5f683a693c654f6543714d6a2; dywem=95841923.y; LastCity=%E9%87%8D%E5%BA%86; LastCity%5Fid=551; index-c=0; _jzqx=1.1540363062.1540368442.2.jzqsr=hao123%2Ecom|jzqct=/link/v3/.jzqsr=hao123%2Ecom|jzqct=/zhaopin/wangzhi; loginName=h3crdhz; rememberMe=true; zp-route-meta=uid=106274073,orgid=14690842; login_point=14690842; NTKF_T2D_CLIENTID=guest1CB3A58A-0CE1-764D-5455-A51E1A88EF81; nTalk_CACHE_DATA={uid:kf_9051_ISME9754_14690842,tid:1540368505480373}; diagnosis=0; rd_resume_srccode=402101; urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti; adfcid2=pzzhubiaoti; dywez=95841923.1540428547.4.4.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; __utmz=269921210.1540428548.4.4.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1540352377,1540363062,1540368442,1540428548; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1540428548; sts_sid=166a8b2484892-082ee10793f64f-5c10301c-1296000-166a8b248491e7; __xsptplus30=30.5.1540428548.1540428548.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23Lo2HYl0h_eTW2wUbY1Xny0y-91To8xFX%23; _jzqa=1.780900254631550600.1540351472.1540368442.1540428549.4; _jzqy=1.1540351472.1540428549.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; at=c0559a9693dc4022b59f8f2a5b3d5a49; Token=c0559a9693dc4022b59f8f2a5b3d5a49; rt=efa5edaf98a442aba303be98fd27db6a; RDsUserInfo=36672168546b5a754177537145654071516357655f69586b4e713b653f7758771965506706681b6b0f7519771f714c6522712b635a657c11ba381816a9384a77367725655e675468526b2975357758714665437153635e655869536b417145654a77247725655e675468596b46754377507157654f715f6352655869506b34713b654c7755774a6536672468546b217523775571416545715263536558695c6b467143654a77307725655e6754685f6b5b754a7736713e654a7155635c651; uiioit=3d672038046a55644764466f5a6753380d6a54644064436f536726387d6a59644664446f5e675d38096a5c644364426f53677; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22106274073%22%2C%22%24device_id%22%3A%22166a41a21c1366-0d8f16071da7e-5c10301c-1296000-166a41a21c265b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22other%22%2C%22%24latest_utm_medium%22%3A%22cnt%22%2C%22%24latest_utm_campaign%22%3A%22121113803%22%7D%2C%22first_id%22%3A%22166a41a21c1366-0d8f16071da7e-5c10301c-1296000-166a41a21c265b%22%7D; ZL_REPORT_GLOBAL={%22//i%22:{%22actionid%22:%22255520c9-15bd-4519-a696-7e5c3c7fa08b-i%22%2C%22funczone%22:%22back_best_for_you%22}%2C%22/resume/new%22:{%22actionid%22:%22f49b181d-83e9-4e2b-bf8f-48df949330e8%22%2C%22funczone%22:%22addrsm_ok_rcm%22}}; dywea=95841923.4206823475521566700.1540351470.1540428547.1540433718.5; __utma=269921210.4866348.1540351470.1540428548.1540433718.5; sts_evtseq=34; dyweb=95841923.4.10.1540433718; __utmt=1; __utmb=269921210.4.10.1540433718; rd_resume_actionId=1540434347234106274073",
    "Host": "rdapi.zhaopin.com",
}

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "265",
    # "Content-Type": "text/plain",
    "Cookie": "adfbid=0; adfbid2=0; dywec=95841923; ZP_OLD_FLAG=false; __utmc=269921210; sts_deviceid=166a41a2cf888d-077def58536741-5c10301c-1296000-166a41a2cf97f8; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0gHFI0KqiAsah4TqU000005WhvNb00000X8A061.THLyktAJdIjA80K85yF9pywd0ZnquWnYn1m1mWRsnj0kP1RknsKd5H-An177nWuDPWPDwWu7PjNDf1-jPHNaPbf4fbfkrjKD0ADqI1YhUyPGujY1nHfsPj6Ln1RvFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQMGCmyqspy38mvqV5LPGujYknWDknHn3njnhTv-YuHdsXMGCIyFGmyqYpfKWThnqPHbdnWb%26tpl%3Dtpl_11535_17772_13457%26l%3D1507452664%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3140487356_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D171%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3Dmongodbcollection%2525E5%252588%2525A0%2525E9%252599%2525A4%26rqlang%3Dcn%26inputT%3D6200%26bs%3Dmongodbcollection%25E5%2588%25A0%25E9%2599%25A4; _jzqc=1; _jzqckmp=1; ZP_P_VERSION=v2; firstchannelurl=https%3A//passport.zhaopin.com/login; lastchannelurl=https%3A//ts.zhaopin.com/jump/index_new.html%3Futm_source%3Dother%26utm_medium%3Dcnt%26utm_term%3D%26utm_campaign%3D121113803%26utm_provider%3Dzp%26sid%3D121113803%26site%3Dpzzhubiaoti; qrcodekey=5a02ba4fdf384ca9b8d19e3c3d77b60f; JsNewlogin=2034202397; JSloginnamecookie=17783886899; JSShowname=%E9%99%88%E6%9C%8B; JSsUserInfo=236a2d6b566a5c645f6951755572537346765e695d6b5f6a5f6825693b654f654271416a5e6b536a59645069517553725d7348765369506b3f6a2a6854693df379024871336a246b566a02640b69017500720b7301760f69056b0d6a24685869436541655d71156a066b066a51643b693d75587254734a762b693f6b576a5d684469466552654271476a536b596a5f645369287529725873417651693e6b2b6a59682369386545654b71466a5f6b5c6a5e645e695c7555725e7324763e69566b5b6a5f683a693c654f6543714d6a2; dywem=95841923.y; LastCity=%E9%87%8D%E5%BA%86; LastCity%5Fid=551; index-c=0; _jzqx=1.1540363062.1540368442.2.jzqsr=hao123%2Ecom|jzqct=/link/v3/.jzqsr=hao123%2Ecom|jzqct=/zhaopin/wangzhi; loginName=h3crdhz; rememberMe=true; zp-route-meta=uid=106274073,orgid=14690842; login_point=14690842; NTKF_T2D_CLIENTID=guest1CB3A58A-0CE1-764D-5455-A51E1A88EF81; nTalk_CACHE_DATA={uid:kf_9051_ISME9754_14690842,tid:1540368505480373}; diagnosis=0; rd_resume_srccode=402101; urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti; adfcid2=pzzhubiaoti; dywez=95841923.1540428547.4.4.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; __utmz=269921210.1540428548.4.4.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1540352377,1540363062,1540368442,1540428548; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1540428548; sts_sid=166a8b2484892-082ee10793f64f-5c10301c-1296000-166a8b248491e7; __xsptplus30=30.5.1540428548.1540428548.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23Lo2HYl0h_eTW2wUbY1Xny0y-91To8xFX%23; _jzqa=1.780900254631550600.1540351472.1540368442.1540428549.4; _jzqy=1.1540351472.1540428549.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; at=c0559a9693dc4022b59f8f2a5b3d5a49; Token=c0559a9693dc4022b59f8f2a5b3d5a49; rt=efa5edaf98a442aba303be98fd27db6a; RDsUserInfo=36672168546b5a754177537145654071516357655f69586b4e713b653f7758771965506706681b6b0f7519771f714c6522712b635a657c11ba381816a9384a77367725655e675468526b2975357758714665437153635e655869536b417145654a77247725655e675468596b46754377507157654f715f6352655869506b34713b654c7755774a6536672468546b217523775571416545715263536558695c6b467143654a77307725655e6754685f6b5b754a7736713e654a7155635c651; uiioit=3d672038046a55644764466f5a6753380d6a54644064436f536726387d6a59644664446f5e675d38096a5c644364426f53677; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22106274073%22%2C%22%24device_id%22%3A%22166a41a21c1366-0d8f16071da7e-5c10301c-1296000-166a41a21c265b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22other%22%2C%22%24latest_utm_medium%22%3A%22cnt%22%2C%22%24latest_utm_campaign%22%3A%22121113803%22%7D%2C%22first_id%22%3A%22166a41a21c1366-0d8f16071da7e-5c10301c-1296000-166a41a21c265b%22%7D; ZL_REPORT_GLOBAL={%22//i%22:{%22actionid%22:%22255520c9-15bd-4519-a696-7e5c3c7fa08b-i%22%2C%22funczone%22:%22back_best_for_you%22}%2C%22/resume/new%22:{%22actionid%22:%22f49b181d-83e9-4e2b-bf8f-48df949330e8%22%2C%22funczone%22:%22addrsm_ok_rcm%22}}; dywea=95841923.4206823475521566700.1540351470.1540428547.1540433718.5; __utma=269921210.4866348.1540351470.1540428548.1540433718.5; sts_evtseq=34; dyweb=95841923.4.10.1540433718; __utmt=1; __utmb=269921210.4.10.1540433718; rd_resume_actionId=1540434347234106274073",
    "Host": "rdapi.zhaopin.com",
    "Origin": "https://rd5.zhaopin.com",
    "Referer": "https://rd5.zhaopin.com/custom/searchv2/result",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "zp-route-meta": "uid=106274073,orgid=14690842",
}
