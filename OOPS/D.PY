 #weekly temperature data
city = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio"]
temperature = []
print("Enter the weekly temperature data for the following cities:")
for day in range(7):
    daily_temps = []
    for city_name in city:
        print(f"Day {day + 1} - {city_name}: ")
        temp = float(input())
        daily_temps.append(temp)
    temperature.append(daily_temps)