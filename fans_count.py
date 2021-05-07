import urllib.request,json,time

data = urllib.request.urlopen("https://api.bilibili.com/x/web-interface/card?mid=286429414")
xinxi = data.read().decode('utf-8')
dict = json.loads(xinxi)
fans = dict['data']['card']['fans']
t = time.strftime("%Y-%m-%d-%H-%M", time.localtime())

add_info = '\n' + t + ' ' + str(fans) + '\n'

with open('README.md','a') as f:
    f.write(add_info)
