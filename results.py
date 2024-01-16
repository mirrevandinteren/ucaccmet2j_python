import json
from datetime import datetime

file = open('precipitation.json')
precipitation = json.load(file)

# Create a list with dictionaries of the Seattle measurements and one with the other measurements. 
seattle_precipitation = []
other_precipitation = []
for item in precipitation:
    if item['station'] == 'GHCND:US1WAKG0038':
        seattle_precipitation.append(item)
    else:
        other_precipitation.append(item)    

# Calculate the total monthly precipitation
# First create a variable that stores the month
for item in seattle_precipitation:
    item.update({'date_int' : item['date'].replace('2010-','')})
    item.update({'date_int' : int(item['date_int'][:-3])})
# Create a dictionary that stores the month and the total precipitation
total_monthly_precipitation_dict = {}
for item in seattle_precipitation:
    if item['date_int'] not in total_monthly_precipitation_dict:
        total_monthly_precipitation_dict[item['date_int']] = item['value']
    elif item['date_int'] in total_monthly_precipitation_dict:
        total_monthly_precipitation_dict[item['date_int']] += item['value']
# Turn the dictionary into a list
total_monthly_precipitation = list(total_monthly_precipitation_dict.values())

output_data = {
    "Seattle" : {
        "total_montly_precipitation" : total_monthly_precipitation
    }
}

# Create JSON file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file)

# Question 2
    
# Calculate total yearly precipitation
total_yearly_precipitation = sum(total_monthly_precipitation)

# Calculate relative monthly precipitation
relative_monthly_precipitation = [element/total_yearly_precipitation for element in total_monthly_precipitation]

output_data = {
    "Seattle" : {
        "total_montly_precipitation" : total_monthly_precipitation,
        "total_yearly_precipitation" : total_yearly_precipitation,
        "relative_montly_precipitation" : relative_monthly_precipitation
    }
}

# Create JSON file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file)