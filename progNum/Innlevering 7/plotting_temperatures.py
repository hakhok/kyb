# 1: dates
# 2: mean temp
# 3: min temps
# 4: max temps
from matplotlib import pyplot as plt
def get_list(line):
    float_list = line.split(" ")
    for i, number in enumerate(float_list):
        float_list[i] = float(number)
    return float_list

def get_data(file):
    data = file.readlines()
    dates       = data[0].split(' ')
    meantemps   = get_list(data[1])
    mintemps    = get_list(data[2])
    maxtemps    = get_list(data[3])
    return (dates, meantemps, mintemps, maxtemps)

def plot_data(file):
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    dates, meantemps, mintemps, maxtemps = get_data(file)
    plt.plot(dates, mintemps, label="Min temps")
    plt.plot(dates, maxtemps, label="Max temps")
    plt.plot(dates, meantemps, label="Mean temps")
    plt.legend()
    plt.title("Temperatures")
    plt.xlabel("Month")
    plt.ylabel("Temp [C]")
    plt.grid()
    plt.xticks(range(15,365,31),months)
    plt.show()

f = open("Trondheim_temperatures_list.txt", "r")
plot_data(f)
f.close()
