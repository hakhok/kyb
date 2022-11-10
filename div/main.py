the_string = "This is the string"
# print(the_string.split())
# print(the_string.split(" "))

def hanoi(n):
    if n==1:
        return n
    else:
        n = 2*hanoi(n-1)
    return n
results = hanoi(4)
# print(results)

def fileToList(filename):
    names = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            names.append(line[2:].split('\n')[0])
    return names

# print(fileToList("students.txt"))

def create_username_list(name_list):
    usernames = []
    for name in name_list:
        first_name, last_name = name.lower().split(" ")
        username = ""
        if len(first_name)>6:
            username += first_name[:6] + last_name[0:3]
        else:
            username += first_name + last_name[0:3]
        usernames.append(username)
    return usernames

print(create_username_list(["Ola Nordmann", "Kari Jensen", "Alexander Re"]))

def fix_duplicates(usernames):
    un_list = []
    for username in usernames:
        if not username in un_list:
            un_list.append(username)
        else:
            un_list.append(username + 'a')
    return un_list

print(fix_duplicates(["olanor", "karijen", "olanor", "alexanre", "karijen"]))

def createLookUpTable(namesList, usernamesList):
    user_dict = {}
    for name, username in zip(namesList, usernamesList):
        user_dict[name] = username
    return user_dict

namesList = ["Ola Nordmann", "Kari Olsen", "Roger Jensen"]
usernamesList = ["olanor", "kariols", "rogerjen"]
print(createLookUpTable(namesList, usernamesList))

import numpy as np
from matplotlib import pyplot as plt

def plot_cos():
    k_list = [1, 2, 3]
    x = np.linspace(0, np.pi*2, 100)
    for k in k_list:
        plt.plot(x, np.cos(x*k), label = f"k = {k}")
    plt.xlabel("x")
    plt.ylabel("cos(kx)")
    plt.title("cosines with different wave numbers")
    plt.legend()
    plt.show()

# plot_cos()

import random

def createGroups(name_list):
    groups = []
    number_of_groups = len(name_list)//4
    print(number_of_groups)
    for group_number in range(number_of_groups):
        group = ()
        while len(group)<4:
            name = random.choice(name_list)
            group+=(name,)
            name_list.pop(name_list.index(name))
        groups.append(group)
    if len(name_list) < 3:
        for i in range(len(name_list)):
            groups[i]+=(name_list[i],)
    else:
        last_group = ()
        for name in name_list:
            last_group+=(name,)
        groups.append(last_group)
    return groups
    

print(createGroups(["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10","name11","name12"]))
