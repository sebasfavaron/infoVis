import collections
from unidecode import unidecode
from sys import exit

unique_names = collections.defaultdict(int)


def clean_name(name):
    name = unidecode(name)
    name = name.title()
    return name


# grab info
with open('nombres-full.csv') as f:
    next(f)
    for line in f:
        parts = line.split(',')
        if(len(parts) != 3):  # algunos tenian una coma en el nombre y pienso ignorarlos
            continue
        names = parts[0].split(' ')
        try:
            amount = int(parts[1])
        except Exception:
            print(parts)
            exit(1)

        year = parts[2][:-1]

        for name in names:
            if(name == ''):
                continue
            name = clean_name(name)
            if(name in unique_names):
                unique_names[name][year] += amount
            else:
                unique_names[name] = collections.defaultdict(int)


def sum_ocurrences(values):
    ocurrences = 0
    for _, value in values.items():
        ocurrences += value
    return ocurrences


# filter uncommon names (with less than 20 ocurrences)
unique_names = {name: values for name, values in unique_names.items()
                if sum_ocurrences(values) > 20}


# clean up
not_names = ['De', 'Del']
for val in not_names:
    unique_names.pop(val, None)


# print all (to use in bash for concatenation)
for name, values in unique_names.items():
    for year, amount in values.items():
        print(F'{name},{year},{amount}')
