# with open("weather_data.csv") as weater_data:
#     weater = weater_data.readlines()
#     print(weater)

# import csv
# # help tabular data
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
#     print(temperatures)

# more data
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data['temp'].to_list()
# print(data_list)
# print(data['temp'].mean()) # average
#
# print(max(data_list))
# data['temp'].max()
#
# # data in columns
# print(data['temp'])
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/6 + 23
# print(monday_temp_f)

# create a dataframe from scratch
data_dict = {
    "students":["amy", "James", "angela"],
    "scores":[76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
