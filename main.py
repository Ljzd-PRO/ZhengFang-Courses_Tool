import requests
import json

## 在此处设置相关信息

# 超时时间
timeout = 10

# 每次超时后增加的超时时间
time_add = 5

# 最多重试次数
max_retry = 3

# 学号
stu_id = 202112345678

# 以下通过抓包获取
jg_id = "SDFSDFSDFSDFSDF"
zyh_id = "QWEQWEQWEQWEQWE"
xsbj = "12345678"
cookie = "ABCDEFGHIJKLMN"

xkkz_req = {
"url" : "http://172.16.1.205/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su={stu_id}".format(stu_id=stu_id),

"headers" : """Content-Type: application/x-www-form-urlencoded;charset=utf-8
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh-Hans;q=0.9
Accept-Encoding: gzip, deflate
Host: 172.16.1.205
Origin: http://172.16.1.205
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
Connection: keep-alive
Referer: http://172.16.1.205/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su={stu_id}
Content-Length: 157
Cookie: {cookie}
X-Requested-With: XMLHttpRequest""".format(cookie=cookie, stu_id=stu_id),

"data" : """jg_id: {jg_id}
zyh_id: {zyh_id}
njdm_id: 2021
zyfx_id: wfx
bh_id: 21129008
xz: 4
ccdm: 3
xkxnm: 2021
xkxqm: 12
xkly: 0"""
}

query_req = {
"url" : "http://172.16.1.205/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512&su={stu_id}".format(stu_id=stu_id),

"headers" : """Content-Type: application/x-www-form-urlencoded;charset=utf-8
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh-Hans;q=0.9
Accept-Encoding: gzip, deflate
Host: 172.16.1.205
Origin: http://172.16.1.205
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
Connection: keep-alive
Referer: http://172.16.1.205/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su={stu_id}
Content-Length: 498
Cookie: JSESSIONID={cookie}
X-Requested-With: XMLHttpRequest""".format(cookie=cookie, stu_id=stu_id),

"data" : """njdm_id_list[0]: 2021
kclb_id_list[0]: 01
rwlx: 2
xkly: 0
bklx_id: 0
sfkkjyxdxnxq: 0
xqh_id: 1
jg_id: {jg_id}
njdm_id_1: 2021
zyh_id_1: {zyh_id}
zyh_id: {zyh_id}
zyfx_id: wfx
njdm_id: 2021
bh_id: 21129008
xbm: 1
xslbdm: 421
ccdm: 3
xsbj: {xsbj}
sfkknj: 0
sfkkzy: 0
kzybkxy: 0
sfznkx: 0
zdkxms: 0
sfkxq: 0
sfkcfx: 0
kkbk: 0
kkbkdj: 0
sfkgbcx: 0
sfrxtgkcxd: 0
tykczgxdcs: 0
xkxnm: 2021
xkxqm: 12
kklxdm: 10
rlkz: 0
xkzgbj: 0
kspage: 1
jspage: 100
jxbzb: """.format(jg_id=jg_id, zyh_id=zyh_id, xsbj=xsbj)
}

select_req = {
"url" : "http://172.16.1.205/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su={stu_id}".format(stu_id=stu_id),

"headers" : """Content-Type: application/x-www-form-urlencoded;charset=utf-8
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh-Hans;q=0.9
Accept-Encoding: gzip, deflate
Host: 172.16.1.205
Origin: http://172.16.1.205
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
Connection: keep-alive
Referer: http://172.16.1.205/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su={stu_id}
Content-Length: 576
Cookie: JSESSIONID={cookie}
X-Requested-With: XMLHttpRequest""".format(cookie=cookie, stu_id=stu_id),

"data" : """jxb_ids: {jxb_ids}
kch_id: {kch_id}
rwlx: 2
rlkz: 0
rlzlkz: 1
sxbj: 1
xxkbj: {xxkbj}
qz: 0
cxbj: 0
xkkz_id: {xkkz_id}
njdm_id: 2021
zyh_id: {zyh_id}
kklxdm: 10
xklc: 1
xkxnm: 2021
xkxqm: 12"""
}

info_req = {
"url" : "http://172.16.1.205/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html?gnmkdm=N253512&su={stu_id}".format(stu_id=stu_id),

"headers" : """Content-Type: application/x-www-form-urlencoded;charset=utf-8
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh-Hans;q=0.9
Accept-Encoding: gzip, deflate
Host: 172.16.1.205
Origin: http://172.16.1.205
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
Connection: keep-alive
Referer: http://172.16.1.205/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su={stu_id}
Content-Length: 467
Cookie: JSESSIONID={cookie}
X-Requested-With: XMLHttpRequest""".format(cookie=cookie, stu_id=stu_id),

"data" : """njdm_id_list[0]: 2021
kclb_id_list[0]: 01
rwlx: 2
xkly: 0
bklx_id: 0
sfkkjyxdxnxq: 0
xqh_id: 1
jg_id: {jg_id}
zyh_id: {zyh_id}
zyfx_id: wfx
njdm_id: 2021
bh_id: 21129008
xbm: 1
xslbdm: 421
ccdm: 3
xsbj: {xsbj}
sfkknj: 0
sfkkzy: 0
kzybkxy: 0
sfznkx: 0
zdkxms: 0
sfkxq: 0
sfkcfx: 0
kkbk: 0
kkbkdj: 0
xkxnm: 2021
xkxqm: 12
xkxskcgskg: 1
rlkz: 0
kklxdm: 10
kch_id: {kch_id}
jxbzcxskg: 0
xkkz_id: {xkkz_id}
cxbj: 0
fxbj: 0"""
}

s = requests.Session()

# 将Edge中复制的请求头表格转换为Python字典
def trans_headers(headers_str:str):
    headers = {}
    for line in headers_str.splitlines():
        sp = line.split(": ")
        headers.setdefault(sp[0], sp[1])
    return headers

# 将Edge中复制的请求数据表格转换为x-www-form-urlencoded格式字符串
def trans_data(data_str:str):
    data_str = data_str.replace(": ", "=")
    data_str = data_str.replace("\n", "&")
    data_str = data_str.encode('utf-8')
    return data_str

# 获取 xkkz_id
def xkkz(timeout:int=10) -> str:
    xkkz = s.post(url=xkkz_req["url"], headers=trans_headers(xkkz_req["headers"].format(cookie=cookie)), data=trans_data(xkkz_req["data"].format(jg_id=jg_id, zyh_id=zyh_id)), timeout=timeout)
    xkkz_result = json.loads(xkkz.text)

    for data in xkkz_result:
        if "xkkz_id" in data:
            return data["xkkz_id"]

# 查询课程
def query(timeout:int=10) -> list:
    query = s.post(url=query_req["url"], headers=trans_headers(query_req["headers"]), data=trans_data(query_req["data"]), timeout=timeout)
    query_result = json.loads(query.text)["tmpList"]

    i = 1
    for course_data in query_result:
        print("ID-{ID}: 人数容量：{quota_total} 剩余名额：{quota_surplus} 学分：{course_point} 课程名称：{course_name} ID-{ID}"
        .format(ID=i, quota_total=course_data["yxzrs"], quota_surplus=course_data["blyxrs"], course_point=course_data["xf"], course_name=course_data["kcmc"])
        )

        i += 1

    return query_result

# 查询某课程详情
def info(ID:int, query_result:list, xkkz_id:str, timeout:int=10) -> dict:
    ID -= 1

    info_data = info_req["data"].format(kch_id=query_result[ID]["kch_id"],
    jg_id=jg_id, zyh_id=zyh_id, xsbj=xsbj, xkkz_id=xkkz_id
    )

    info = s.post(url=info_req["url"], headers=trans_headers(info_req["headers"]), data=trans_data(info_data), timeout=timeout)
    info_result = json.loads(info.text)[0]
    print("\n剩余名额：{quota_surplus} 课程归属：{course_category} 课程名称：{course_name}\n"
    .format(quota_surplus=query_result[ID]["blyxrs"], course_category=info_result["kcgsmc"], course_name=query_result[ID]["kcmc"])
    )

    return info_result

# 进行选课
def select(ID:int, query_result:list, info_result:dict, xkkz_id:str, timeout:int=10) -> int:
    ID -= 1

    select_data = select_req["data"].format(jxb_ids=info_result["do_jxb_id"], kch_id=query_result[ID]["kch_id"], xxkbj=query_result[ID]["xxkbj"],
    xkkz_id=xkkz_id, zyh_id=zyh_id
    )

    select = s.post(url=select_req["url"], headers=trans_headers(select_req["headers"]), data=trans_data(select_data), timeout=timeout)
    select_result = json.loads(select.text)

    select_result_code = int(select_result["flag"])
    if select_result_code == -1:
        print("\n课程已选满({code}) 课程名称：{course_name}\n"
        .format(code=select_result_code, course_name=query_result[ID]["kcmc"])
        )
    elif select_result_code == 0:
        print("\n选课异常({code}) 提示信息：{msg} 课程名称：{course_name}\n"
        .format(code=select_result_code, msg=select_result["msg"], course_name=query_result[ID]["kcmc"])
        )
    else:
        print("\n选课成功！({code}) 课程名称：{course_name}\n"
        .format(code=select_result_code, course_name=query_result[ID]["kcmc"])
        )

    return select_result

if __name__ == "__main__":
    print("程序开始")
    stu_id = str(stu_id)
    timeout_ = timeout
    i = 0

    while True:
        try:
            xkkz_result = xkkz(timeout_)
        except:
            timeout_ += time_add
            i += 1
            print("xkkz_id获取失败，正在重试({0})".format(i))
            continue
        timeout_ = timeout
        i = 0
        break

    while True:
        try:
            query_result = query(timeout_)
        except:
            timeout_ += time_add
            i += 1
            print("查询课程列表失败，正在重试({0})".format(i))
            continue
        timeout_ = timeout
        i = 0
        break

    while True:
        print("\n> 请输入要选的课程ID：")

        try:
            input_ID = int(input())
        except ValueError:
            print("输入错误，请输入ID！")
            continue

        while True:
            try:
                info_result = info(input_ID, query_result, xkkz_result, timeout_)
            except:
                timeout_ += time_add
                i += 1
                if i <= max_retry:
                    print("课程详细信息获取失败，正在重试({0})".format(i))
                    continue
            timeout_ = timeout
            if i <= max_retry:
                i = 0
            break

        if i > max_retry:
            print("课程详情信息获取失败次数过多，放弃查询该课程。")
            i = 0
            continue

        while True:
            print("> 输入 是(1) 否(0/ENTER) 选择此课程：")

            input_confirm = input()
            if input_confirm == "":
                break
            try:
                input_confirm = int(input_confirm)
            except ValueError:
                    print("输入错误，请输入 0/ENTER（不选） 或 1（选）！")
                    continue
            if input_confirm != 1 and input_confirm != 0:
                print("输入错误，请输入 0/ENTER（不选） 或 1（选）！")
                continue

            break

        if input_confirm != "":
            input_confirm = bool(input_confirm)

            if input_confirm == True:
                while True:
                    try:
                        select(input_ID, query_result, info_result, xkkz_result, timeout_)
                    except:
                        timeout_ += time_add
                        i += 1
                        if i <= max_retry:
                            print("选课失败，正在重试({0})".format(i))
                            continue
                    timeout_ = timeout
                    if i <= max_retry:
                        i = 0
                    break

                if i > max_retry:
                    print("选课失败次数过多，放弃该课程。")
                    i = 0
                    continue
