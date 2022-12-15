
all_temperatures = {}
highest_temperature = {}
highest_temperature_month = {}
lowest_temperature = {}
lowest_temperature_month = {}
average_temperature = {}

with open("Weather Data in India from 1901 to 2017.csv", encoding="UTF8") as file:
    next(file)  # Skips first line
    for data in file:
        month = {}
        line = data.strip().split(",")

        # Checks that we have all the information required (from the .txt file)
        if len(line) < 14:
            continue

        # Checks for any possible errors during conversion of string to float
        try:
            month["January"] = float(line[2])
            month["February"] = float(line[3])
            month["March"] = float(line[4])
            month["April"] = float(line[5])
            month["May"] = float(line[6])
            month["June"] = float(line[7])
            month["July"] = float(line[8])
            month["August"] = float(line[9])
            month["September"] = float(line[10])
            month["Oktober"] = float(line[11])
            month["November"] = float(line[12])
            month["December"] = float(line[13])
            all_temperatures[line[1]] = month
        except ValueError:
            continue

        highest_temp = -100
        lowest_temp = 100

        for i in month:
            temperature = month[i]
            # Finds the highest temperature
            if highest_temp < temperature:
                highest_temp = temperature
                highest_temperature[line[1]] = highest_temp
                highest_temperature_month[line[1]] = i

            # Finds the lowest temperature
            if lowest_temp > temperature:
                lowest_temp = temperature
                lowest_temperature[line[1]] = lowest_temp
                lowest_temperature_month[line[1]] = i

        # Find average temperature per year
        sum = 0
        for current_temperature_month in month:
            value = month[current_temperature_month]
            sum += value
        average_temperature[line[1]] = round(sum/12,2)

# Creates file that contains max temp, date, min temp, date, year and average temp that year
with open("clean_file_temperature.txt", "w", encoding="UTF8") as weather_file:
            weather_file.write("Year;Highest temperature;Date;Lowest temperature;Date;Average temperature")
            for year in all_temperatures:
                weather_file.write(f"\n{year};{highest_temperature[year]};{highest_temperature_month[year]};"
                               f"{lowest_temperature[year]};{lowest_temperature_month[year]};{average_temperature[year]}")


