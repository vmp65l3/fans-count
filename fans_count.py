import urllib.request,json,time

data = urllib.request.urlopen("https://api.bilibili.com/x/web-interface/card?mid=286429414")
xinxi = data.read().decode('utf-8')
dict = json.loads(xinxi)
fans = dict['data']['card']['fans']
t = time.strftime('%Y-%m-%d-%H-%M', time.localtime())

add_info = t + ',' + str(fans) + '\n'

with open('data.csv','a') as f:
    f.write(add_info)
    

from pandas import read_csv
import matplotlib.pyplot as plt

series = read_csv('data.csv',header=0, index_col=0, parse_dates=None, squeeze=True)

series.plot()
plt.show()