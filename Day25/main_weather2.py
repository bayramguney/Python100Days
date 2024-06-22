import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data['temp']))  # <class 'pandas.core.series.Series'>

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)  # [12, 14, 15, 14, 21, 22, 24]

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

average_temp2 = data['temp'].mean()
print(average_temp2)

max_temp = data['temp'].max()
print(max_temp)

# get data in column
# data_condition = data['condition']
data_condition = data.condition
print(data_condition)

# get data in row
data_monday = data[data.day == 'Monday']
print(data_monday)

data_max_temp = data[data.temp == data.temp.max()]
print(data_max_temp)

monday = data[data.day == 'Monday']
print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Al"],
    "scores": [76, 45, 78]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_csv = data_frame.to_csv("new_data.csv")
