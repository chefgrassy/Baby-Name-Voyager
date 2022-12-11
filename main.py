# Project 5 - Baby Name Voyager
# CS 111, Reckinger
# Name: Pablo Vicencio
# Date: 11/1/2022
# Description: This program plots the popularity of baby names that are inputted by the user

import matplotlib.pyplot as plt

# load_data() - Loads the file and converts the .txt file into a dictionary, also converts strings to integers
def load_data(file):
    name_dict = {}
    num_list = []
    data_file = open(file)
    data_list = data_file.readlines()
    data_file.close()

    for string in data_list:
        string = string.strip()
        split_data = string.split()
        num_list = split_data[1:]
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        name_dict[split_data[0]] = num_list

    return name_dict

# clean_data() - Cleans the data by replacing all the zeros with the max of the entire .txt file, which is 1013
def clean_data(data, x):
    for values in data.values():
        for i in range(len(values)):
            if values[i] == 0:
                values[i] = x

    return data

# find_replacement() - finds the max value of the entire dictionary using iteration, the max is 1013
def find_replacement(dict):
    max_val = -1
    for values in dict.values():
        for i in range(len(values)):
            if values[i] > max_val:
                max_val = values[i]

    return max_val

# find_names() - finds the names inputted by the user and returns a dicionary that will be used for plotting those names
def find_names(names):
    names = names.split()
    new_dict = {}
    for name in names:
        if name in name_dict:
            num_list = name_dict[name]
            new_dict[name] = num_list
    return new_dict, names

# plot_names() - most important function used to plot the dictionary values
def plot_names(new_dict, names):
    new_dict, names = find_names(namestring)
    plt.ion()
    for name in names: 
        num_list = name_dict[name]
        plt.plot(num_list, 'o:')
        plt.xlabel("years")
        plt.ylabel("ranking")
        plt.title("Most Popular Baby Names, by decade")
        plt.ylim(1020, -20)
        years_ticks = "1900", "1920", "1940", "1960", "1980", "2000"
        ticks = range(0, len(num_list), 2)
        plt.xticks(ticks, years_ticks)
        plt.legend(names)
    file_name = namestring.replace(" ", "") + ".png"
    plt.savefig(file_name)

if __name__ == '__main__':
    data = load_data("names-data.txt")  # KEEP THIS
    max = find_replacement(data)  # KEEP THIS
    name_dict = clean_data(data, max) # KEEP THIS
    namestring = input("Enter baby names: ")  # KEEP THIS
    new_dict, names = find_names(namestring)
    plot_names(new_dict, names) # Returns new dictionary with the user's selected names