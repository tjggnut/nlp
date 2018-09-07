import re
s = "网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。"
s2 = "文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中有用的信息。爬去的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。"

regex = "爬虫"
ss = s.split('。')
for string in ss:
    if re.search(regex,string) is not None:
        print(string)

#regex2 = "文本"
regex2 = "文."
ss2 = s2.split('。')
for line in ss2:
    if re.search(regex2,line) is not None:
        print(line)

regex3 = "用户."
ss3 = s2.split("。")
for line in ss3:
    if re.search(regex3, line) is not None:
        print(re.search(regex3, line))
        print(line)

print("____________ regex4 ____________")

regex4 = "^文本"
ss4 = s2.split("。")
for line in ss4:
    if re.search(regex4, line) is not None:
        # print(re.search(regex3, line))
        print(line)

print("____________ regex5 ____________")
regex5 = "爬.$"
ss5 = s2.split("。")
for line in ss5:
    if re.search(regex5, line) is not None:
        # print(re.search(regex3, line))
        print(line)

text_string = ['[重要的]今年第七号台风23日登陆',
'上海发布车库销售监管通知',
'[紧要的]中国对印连发强硬信息，印度急切需要结束对峙']

#错误版本： p = "^\\[[重要的|紧要的]\\]"
p = "^\\[[重紧]要的\\]"
# p = "^\[[重紧]..\]"

for text in text_string:
    if re.search(p,text) is not None:
        print(text)

if re.search("\\\\","nee\dle"):
    print("match")

if re.search(r"\\","nee\dle"):
    print("match")

print("_______ regex num _________")

year_strings = ['year 2018','year 9876','year 1024']
#匹配1000-2999年
year_re = '[1-2][0-9]{3}'
for year in year_strings:
    if re.search(year_re,year):
        print(year)

strr = " ".join(year_strings)
result = re.findall(year_re,strr)
print(type(result))