import json


def map_by_year(json_data):
    years = {}
    for obj in json_data:
        key_year = str(obj['year'])
        key_state = obj['state']
        value = obj['value']
        if key_year not in years.keys():
            years[key_year] = {
                key_state: value
            }
    for obj in json_data:
        key_year = str(obj['year'])
        key_state = obj['state']
        value = obj['value']
        if key_state not in years[key_year].keys():
            years[key_year][key_state] = value

    return years


def map_by_state(json_data):
    states = {}
    for obj in json_data:
        key_year = str(obj['year'])
        key_state = obj['state']
        value = obj['value']
        if key_state not in states.keys():
            states[key_state] = {
                key_year: value
            }
    for obj in json_data:
        key_year = str(obj['year'])
        key_state = obj['state']
        value = obj['value']
        if key_year not in states[key_state].keys():
            states[key_state][key_year] = value

    return states
