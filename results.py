import json
from datetime import datetime
from csv import DictReader

file = open('precipitation.json')
precipitation = json.load(file)
with open('stations.csv') as file:
    reader = DictReader(file)
    stations = list(reader)  

# Create a list with dictionaries of the Seattle measurements and one with the other measurements. 
# seattle_precipitation = []
# other_precipitation = []
# for item in precipitation:
#     if item['station'] == 'GHCND:US1WAKG0038':
#         seattle_precipitation.append(item)
#     else:
#         other_precipitation.append(item)    

for item in precipitation:
    item.update({'month' : item['date'].replace('2010-','')})
    item.update({'month' : int(item['month'][:-3])})

# Calculate the total monthly precipitation
# First create a variable that stores the month
# for item in seattle_precipitation:
#     item.update({'date_int' : item['date'].replace('2010-','')})
#     item.update({'date_int' : int(item['date_int'][:-3])})

# Create a dictionary that stores the month and the total precipitation
# total_monthly_precipitation_dict = {}
# for item in seattle_precipitation:
#     if item['date_int'] not in total_monthly_precipitation_dict:
#         total_monthly_precipitation_dict[item['date_int']] = item['value']
#     elif item['date_int'] in total_monthly_precipitation_dict:
#         total_monthly_precipitation_dict[item['date_int']] += item['value']
# # Turn the dictionary into a list
# total_monthly_precipitation = list(total_monthly_precipitation_dict.values())


# seattle_precipitation = []
# other_precipitation = []
# for item in precipitation:
#     if item['station'] == 'GHCND:US1WAKG0038':
#         seattle_precipitation.append(item)
#     else:
#         other_precipitation.append(item)  
# for item in precipitation:
#     total_monthly_precipitation_dict = []
#     if item['station'] not in total_monthly_precipitation_dict:
#         total_monthly_precipitation_dict.append(item)
#     elif item['station'] in total_monthly_precipitation_dict:





# total_monthly_precipitation = list(total_monthly_precipitation_dict.values())
# print(total_monthly_precipitation)

# output_data = {
#     "Seattle" : {
#         "total_montly_precipitation" : total_monthly_precipitation
#     }
# }

# Create JSON file
# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(output_data, file)

# Question 2
    
# # Calculate total yearly precipitation
# total_yearly_precipitation = sum(total_monthly_precipitation)

# # Calculate relative monthly precipitation
# relative_monthly_precipitation = [element/total_yearly_precipitation for element in total_monthly_precipitation]

# output_data = {
#     "Seattle" : {
#         "total_montly_precipitation" : total_monthly_precipitation,
#         "total_yearly_precipitation" : total_yearly_precipitation,
#         "relative_montly_precipitation" : relative_monthly_precipitation
#     }
# }

# # Create JSON file
# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(output_data, file)

# Question 3
    
total_dictionary = {}
for station in stations:
    total_monthly_list = []
    for item in precipitation:
        if item['station'] == station['Station']:
            total_monthly_list.append(item)
    station_dictionary = {}
    for item in total_monthly_list:
        if item['month'] not in station_dictionary:
            station_dictionary[item['month']] = item['value']
        elif item['month'] in station_dictionary:
            station_dictionary[item['month']] += item['value']
    station_yearly = sum(list(station_dictionary.values()))
    station_relative = [element/station_yearly for element in list(station_dictionary.values())]

# I was storing the data in one big dictionary, but didn't manage to finish in time.
