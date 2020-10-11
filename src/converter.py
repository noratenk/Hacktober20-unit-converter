import json
import sys
import os


def read_file(json_name):
    json_path = f'units/{json_name}'
    with open(json_path) as f:
        data = json.load(f)
    return data


def parse_units():
    units_dict = {}
    files_list = os.listdir('units/')
    for json_name in files_list:
        units_dict[json_name[:-5]] = read_file(json_name)
    return units_dict


def get_unit_dict(units_dict, unit_in, unit_out):
    unit_dict = {}
    key = ''
    for unit_key in units_dict.keys():
        if (unit_in in list(units_dict[unit_key].keys())) & (unit_out in list(units_dict[unit_key].keys())):
            unit_dict = units_dict[unit_key]
            key = unit_key
    return unit_dict, key


def convert(unit_dict, val, unit_in, unit_out):
    return val*unit_dict[unit_in]/unit_dict[unit_out]


if __name__ == '__main__':
    # get 3 variables value, unit_in, unit_out
    value = sys.argv[1]
    unit_in = sys.argv[2]
    unit_out = sys.argv[3]

    # parse all units
    units_dict = parse_units()
    unit_dict, unit_name = get_unit_dict(units_dict, unit_in, unit_out)

    # convert
    result = convert(unit_dict, float(value), unit_in, unit_out)

    print(f'You are converting {unit_name} units.')
    print(f'{value} {unit_in} = {result} {unit_out}')