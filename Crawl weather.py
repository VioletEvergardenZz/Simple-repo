import requests
import re
url = 'http://www.weather.com.cn/weather1d/101310201.shtml'
resp=requests.get(url)
resp.encoding = 'utf-8'
#print(resp.text)


city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
wd = re.findall('<span class="wd">(.*)</span>',resp.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)

'''
<span class="weather">晴转多云</span>
<span class="wd">27/23℃</span>
<span class="zs">适宜</span>
'''


# print(city)
# print(weather)
# print(wd)
# print(zs)

list = []
for a,b,c,d in zip(city,weather,wd,zs):
    list.append([a,b,c,d])
    # print(list)
for item in list:
    print(item)

