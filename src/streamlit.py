import json
import sys
import os
import streamlit as st


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

    units_dict = parse_units()
    available_units_list = list(units_dict.keys())

    # choose units
    selected_unit_type = st.sidebar.selectbox(
        'Select conversion unit type:', available_units_list)

    unit_in = st.sidebar.selectbox('Unit in: ', list(units_dict[selected_unit_type].keys()))
    unit_out = st.sidebar.selectbox('Unit out: ', list(units_dict[selected_unit_type].keys()))

    # Title
    st.title('Unit converter')
    st.subheader('Select an unit in the sidebar.')
    st.write(f'You are converting {selected_unit_type} units.')

    # number input
    number = st.number_input(f'Convert {unit_in} to {unit_out}', value=1)

    # get result
    result = convert(units_dict[selected_unit_type], float(number), unit_in, unit_out)
    st.header(f'{number} {unit_in} is {result} {unit_out}')