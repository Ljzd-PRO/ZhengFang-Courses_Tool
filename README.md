# 正方教务系统抢课工具

**注意：本脚本只在我自己学校平台测试过，有许多信息还需要更改（例如是哪一级的学生、要查询的课程是公共选修课还是别的类型，需要自行测试分析修改）**

**1⃣️.配置相关信息**

修改`main.py`中的相关代码：
```
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
```

**2⃣️.运行`main.py`**
