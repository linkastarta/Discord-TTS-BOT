import csv
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
from matplotlib import pyplot


yf.pdr_override()

stock = input("Enter a stock: ")

startyear = 2020
startmonth = 1
startday = 1

start = dt.datetime(startyear, startmonth, startday)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, period="60d", interval="15m")



df.to_csv(r"stocks.csv")

timecollection = [[] for _ in range(26)]
datacollection = []
lstart = []
lend = []
temp = dt.datetime(1, 1, 1, 9, 30)


for i in range(26):
    timecollection[i].append(temp.strftime("%Y-%m-%d %H:%M:%S")[11:19])
    temp += dt.timedelta(minutes=15)




with open("stocks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tempdate = row["Datetime"][11:19]
        for list in timecollection:
            if tempdate == list[0]:
                list.append(row)
                break

for i in range(len(timecollection)):
    for j in range(len(timecollection)):
        higher = 0
        higherave = 0
        total = 0
        if  i < j:
            for start in timecollection[i][1 :]:
                for end in timecollection[j][1 :]:
                    if start["Datetime"][0 : 10] == end["Datetime"][0 : 10]:
                        total += 1
                        if start["Low"] < end["Adj Close"]:
                            higher += 1
                            higherave += float(end["Adj Close"]) - float(start["Low"])
                        break
            higherave = higherave/higher
            higher = higher/total
            datacollection.append([timecollection[i][0] + "-" + timecollection[j][0], higher, higherave])
x = []
y = []
y2 = []


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li

datacollection = Sort(datacollection)
for data in datacollection:
    x.append(data[0])
    y.append(data[1])
    y2.append(data[2])


pyplot.xticks(rotation=90)
plot1 = pyplot.figure(1)
pyplot.plot(x, y)

pyplot.figure((2))
pyplot.xticks(rotation=90)
pyplot.plot(x, y2)

pyplot.show()

