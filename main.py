#import pandas

#data = pandas.read_csv("f:/Kushal/Programing/Python Programing/learn/Day 25/weather_data.csv")
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(len(temp_list))

#print(data["temp"].mean())
#print(data["temp"].max())

#Get data in columns
#print(data["condition"])
#print(data.condition)

#Get data in rows
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)

#Create a DataFrame from scratch
#data_dict = {
    #"students": ["Amy", "James", "Angela", "Kushal"],
    #"scores": [76, 56, 65, 89]
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv("f:/Kushal/Programing/Python Programing/learn/Day 25/new_data.csv")

import pandas

data = pandas.read_csv("f:/Kushal/Programing/Python Programing/learn/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels =len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("f:/Kushal/Programing/Python Programing/learn/Day 25/squirrel_count.csv")