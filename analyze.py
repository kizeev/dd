# Get the absolute path of the current dir and add the parent dir to sys.path
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


import json

from base64 import b64decode
from collections import defaultdict
from pprint import pprint
from urllib.parse import parse_qs, unquote

from dd.actual_jsdata import (
    JS_DATA, EVENT_KEYS_IN_JS_DATA, POSSIBLE_MISSING_KEYS)


EVENTS = [
    'mousemove', 'click', 'scroll', 'touchstart', 'touchend', 'touchmove',
    'keydown', 'keyup']
EDITED_JS_DATA_KEYS = {}


def prepare_raw_line(line):
    quoted_keys = ['Referer', 'request']
    res = {}
    for k, v in parse_qs(line).items():
        v = v[0]
        if k == 'jsData': 
            v = handle_js_data(v)
        if k == 'eventCounters':
            v = json.loads(v)
        if k in quoted_keys:
            v = unquote(v)
        res[k] = v
    return res


def handle_js_data(raw_js):
    base64_keys = ['cfpfe', 'stcfp']
    res = {}
    for k, v in json.loads(raw_js).items():
        if k in base64_keys:
            v = b64decode(v).decode()
        res[k] = v
    return res


def get_values_from_dict(dicts_list):
    result_dict = defaultdict(dict)
    for dictionary in dicts_list:
        for k in EDITED_JS_DATA_KEYS:
            v = dictionary['jsData'].get(k, '*')
            result_dict[k][v] = result_dict[k].get(v, 0) + 1
    return dict(result_dict)


def get_values_from_events(dicts_list):
    result_dict = defaultdict(dict)
    for dictionary in dicts_list:
        for k in EVENTS:
            v = dictionary[k]
            result_dict[k][v] = result_dict[k].get(v, 0) + 1
    return dict(result_dict)


def prepare_raw_file(requests_file):
    result = {}
    with open(requests_file) as f:
        lines = f.readlines()
        for num, line in enumerate(lines):
            res = prepare_raw_line(line.rstrip())
            result[num] = res
    return result


def check_jsdata_keys(new_jsdata):
    actual_keys = set(JS_DATA.keys())
    actual_event_keys = set(EVENT_KEYS_IN_JS_DATA)
    possible_missing_actual_keys = actual_event_keys | set(
        POSSIBLE_MISSING_KEYS)

    new_keys = [set(i.keys()) for i in new_jsdata]
    for keys in new_keys:
        actual_not_in_new = keys - actual_keys
        # print(actual_not_in_new)

        new_not_in_actual = actual_keys - keys
        # pprint(new_not_in_actual)

        new_not_in_actual_without_event = new_not_in_actual - actual_event_keys
        # pprint(new_not_in_actual_without_event)

        new_not_in_actual_without_missing = (
            new_not_in_actual - possible_missing_actual_keys)
        # pprint(new_not_in_actual_without_missing)


def main(requests_file):
    requests = prepare_raw_file(requests_file)

    jsdata = [i['jsData'] for i in requests.values()]
    check_jsdata_keys(jsdata)
    # print(jsdata)
    return

    # pprint(requests, sort_dicts=False)
    # if res['cid'] != 'null':
    #     continue
    # js_dicts.append(res)
    # for k in {'cokys'}:
    #     print(f'{k}={res['jsData'].get(k, '*')}')
    # print('\n')
    # if res['eventCounters']:
    #     js_dicts.append(res['eventCounters'])
        # print(res['eventCounters']['mousemove'])
    # print(f'eventCounters={res['eventCounters']}')
    # print(f'jsType={res['jsType']}')
    # print(f'cid={res['cid']}')
    # print(f'Referer={res['Referer']}\n')
    # print(num, res['jsData'].keys())
    # print(len(res['jsData'].keys()))
    # break

    # a = get_values_from_dict(js_dicts)
    # a = get_values_from_events(js_dicts)
    # pprint(a)
    # print(js_dicts)
    # pprint(sorted(list(len(str(i)) for i in a['tagpu'].keys())))


if __name__ == '__main__':
    requests_file = 'versions/4.35.0/requests.txt'
    main(requests_file)
