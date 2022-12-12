import matplotlib.pyplot as plt


highest_temp = -100
lowest_temp = 100
all_temperatures = []
years_after_1901 = []

# Calculates the average temperature over a year span
def average_temp_year(dict):
    sum = 0
    average_temp = 0
    for i in dict:
        sum += dict[i]
        average_temp = round(sum/len(dict),2)
    return average_temp

def plot_graph(list_x_axis, list_y_axis):
    plt.title("Average temperature in India (from 1901 to 2017)")
    plt.xlabel("Years after 1901")
    plt.ylabel("Average temperature in degrees celcius")
    plt.plot(list_x_axis, list_y_axis, 'r')
    plt.show()

with open("Weather Data in India from 1901 to 2017.csv", encoding="UTF8") as file:
    next(file)  # Skips first line
    for data in file:
        month = {}
        current_temperature = {}
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
            current_temperature[line[1]] = month
            all_temperatures.append(current_temperature)
        except ValueError:
            continue

        # Finds max- and minimum temperature per year
        for i in current_temperature:
            temperature = current_temperature[line[1]].get(i)
            if highest_temp < temperature:
                highest_temp = temperature

            if lowest_temp > temperature:
                lowest_temp = temperature

        print(f"Highest temperature: {highest_temp}")
        print(f"Lowest temperature: {lowest_temp}")






