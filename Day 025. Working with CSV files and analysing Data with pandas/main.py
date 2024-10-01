# #! /usr/bin/env python3
#
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     tempratures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             tempratures.append(int(row[1]))
# # print(tempratures)
#
import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # 3 ways to get the average temp
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # list_len = len(temp_list)
# # total = 0
# # for temp in temp_list:
# #     total += temp
# #
# # print(f"The average temp is: {total/list_len}")
#
# #2
# #print( sum(temp_list) / len(temp_list))
#
# #3
# # print(data["temp"].mean())
# # ###########
# # print(data["temp"].max())
# # print(data["temp"])
#
# #same
# # print(data.day)
# # print(data["day"])
#
# # Get data in row
# #print(data[data.day == "Monday"])
#
# # pull the hottest day
# #print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# # Celsius to farinheight
# # monday = data[data.day == "Monday"]  # this pulls the row
# # monday_temp = int(monday.temp)
# # print(monday_temp * 9/5 +32)
#
# # Create a 'dataframe' from scratch. (table)
# # data_dict = {
# #     "student": ["Amy", "James", "Angela"],
# #     "score": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# #
# # print(data)
# # data.to_csv("new_data.csv")
#
# #pesky Squirials

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")