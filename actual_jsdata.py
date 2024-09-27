# Get the absolute path of the current dir and add the parent dir to sys.path
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


import re

from random import uniform, choice, randint, choices
from time import time

from dd.real_data import (
    PHONES, APP_UA_TEMP, ANDROID_VERSION_BUILD_IDS, CHROME_VERSIONS,
    APP_VERSIONS, PHONE_LANGS, CHROME_UA)


EVENT_KEYS_IN_JS_DATA = (
    'm_fmi', 'tbce', 'es_sigmdn', 'es_mumdn', 'es_distmdn', 'es_angsmdn',
    'es_angemdn', 'k_hA', 'k_hSD', 'k_pA', 'k_pSD', 'k_rA', 'k_rSD', 'k_ikA',
    'k_ikSD', 'k_kdc', 'k_kuc', 'm_s_c', 'm_m_c', 'm_c_c', 'm_cm_r', 'm_ms_r')
POSSIBLE_MISSING_KEYS = (
    'opts', 'xhr_opts', 'cokys', 'dcok', 'log2', 'wwl', 'cfpfe', 'stcfp')
JS_DATA = {
    'opts': (
        '{"sessionByHeader":true,"ajaxListenerPath":[{"host":"lacentrale.fr'
        '"},{"host":"carboatservices.fr"},{"host":"espacevo.fr"}]}'),
    'xhr_opts': '',
    'ttst': ...,  # possible script execution time??
    'ifov': False,  # camera enabled
    'hc': ...,  # HardwareConcurrency (CPU cores)
    'br_oh': ...,  # browser outer height (JS: window.outerHeight)
    'br_ow': ...,  # browser outer width (JS: window.outerWidth)
    'ua': ...,  # user-agent
    'wbd': False,  # webdriver
    'tagpu': ...,
    'wdif': False,
    'wdifrm': False,
    'npmtm': False,
    'br_h': ...,  # equal br_oh
    'br_w': ...,  # equal br_ow
    'isf': True,
    'nddc': ...,
    'rs_h': ...,  # window height (JS: window.screen.height)
    'rs_w': ...,  # window width (JS: window.screen.width)
    'rs_cd': ...,  # JS:window.screen.colorDepth
    'phe': False,
    'nm': False,
    'jsf': False,
    'lg': ...,  # language (JS: navigator.language)
    'pr': ...,  # JS: window.devicePixelRatio
    'ars_h': ...,  # JS: screen.availHeight
    'ars_w': ...,  # JS: screen.availWidth
    'tz': ...,  # JS: new Date().getTimezoneOffset()
    'str_ss': True,  # session storage exists
    'str_ls': True,  # local storage exists
    'str_idb': True,  # indexed db exists
    'str_odb': False,  # open database exists
    'plgod': False,
    'plg': 0,
    'plgne': 'NA',
    'plgre': 'NA',
    'plgof': 'NA',
    'plggt': 'NA',
    'pltod': False,
    'hcovdr': False,
    'plovdr': False,
    'ftsovdr': False,
    'hcovdr2': False,
    'plovdr2': False,
    'ftsovdr2': False,
    'lb': False,
    'eva': 33,  # JS: eval.toString().length
    'lo': False,
    'ts_mtp': 5,  # JS: navigator.maxTouchPoints
    'ts_tec': True,
    'ts_tsa': True,
    'vnd': 'Google Inc.',  # JS: window.navigator.vendor
    'bid': 'NA',  # JS: window.navigator.buildID
    'mmt': 'empty',
    'plu': 'empty',
    'hdn': False,  # JS: document.hidden
    'awe': False,
    'geb': False,
    'dat': False,
    'med': 'defined',
    'aco': 'probably',
    'acots': False,
    'acmp': 'probably',
    'acmpts': True,
    'acw': 'probably',
    'acwts': False,
    'acma': 'maybe',
    'acmats': False,
    'acaa': 'probably',
    'acaats': True,
    'ac3': '',
    'ac3ts': False,
    'acf': 'probably',
    'acfts': False,
    'acmp4': 'maybe',
    'acmp4ts': False,
    'acmp3': 'probably',
    'acmp3ts': False,
    'acwm': 'maybe',
    'acwmts': False,
    'ocpt': False,
    'vco': '',
    'vcots': False,
    'vch': 'probably',
    'vchts': True,
    'vcw': 'probably',
    'vcwts': True,
    'vc3': 'maybe',
    'vc3ts': False,
    'vcmp': '',
    'vcmpts': False,
    'vcq': '',
    'vcqts': False,
    'vc1': 'probably',
    'vc1ts': True,
    'dvm': ...,  # navigator.deviceMemory
    'sqt': False,
    'so': 'portrait-primary',  # window.screen.orientation
    'wdw': ...,
    'cokys': 'bG9hZFRpbWVzY3NpL=',
    'ecpc': False,
    'lgs': True,
    'lgsod': False,
    'psn': ...,
    'edp': False,
    'addt': True,
    'wsdc': True,
    'ccsr': True,
    'nuad': True,
    'bcda': True,
    'idn': True,
    'capi': False,
    'svde': False,
    'vpbq': True,
    'ucdv': False,
    'spwn': False,
    'emt': False,
    'bfr': False,
    'dbov': False,
    'cfpfe': '',  # any errors
    'stcfp': '',  # any errors
    'ckwa': True,
    'emd': 'k:ai,vi,ao',
    'glvd': ...,
    'glrd': ...,
    'wwl': False,
    'log2': True,
    'jset': ...,
    'dcok': '.lacentrale.fr',
    'm_fmi': False,
    'tbce': 0,
    'es_sigmdn': None,
    'es_mumdn': None,
    'es_distmdn': None,
    'es_angsmdn': None,
    'es_angemdn': None,
    # keys below starting with “k_” are keyboard related
    'k_hA': None,
    'k_hSD': None,
    'k_pA': None,
    'k_pSD': None,
    'k_rA': None,
    'k_rSD': None,
    'k_ikA': None,
    'k_ikSD': None,
    'k_kdc': 0,  # key down count
    'k_kuc': 0,  # key up count
    'm_s_c': 0,  # mouse scroll count
    'm_m_c': 0,  # mouse move count
    'm_c_c': 0,  # mouse click count
    'm_cm_r': 0,  # mouse click-move ratio
    'm_ms_r': 0,  # mouse move-scroll ratio
}


def generate_user_agent_and_lang(random_phone=False):
    test_phone = 'MI 8 Lite'
    phone = choice(list(PHONES.keys())) if random_phone else test_phone
    android_version = choice(PHONES[phone]['android'])
    return (
        APP_UA_TEMP.substitute(dict(
            android_version=android_version,
            phone=phone,
            build_id=choice(ANDROID_VERSION_BUILD_IDS[android_version]),
            chrome_version=choice(CHROME_VERSIONS),
            app_version=choice(APP_VERSIONS),
        )),
        choice(PHONE_LANGS),
    )


def get_ttst_param():
    ttst = float(
        f'{round(uniform(32, 99), 1)}'
        f'{str(choice((0, 9))) * 6}{randint(10000, 9999999):07}')
    return ttst


def get_tagpu_param():
    return round(uniform(1.02, 9.69), 16)


def update_error_keys(js_data, referer, prev_token):
    '''
    I couldn't find the causes of errors, so I made a random generation of the
    most frequently occurring errors.
    '''
    if 'espacevo' in referer:
        del js_data['cfpfe']
        del js_data['stcfp']

    if not prev_token:
        js_data['cfpfe'] = 'ZnVuY3Rpb24oKXt2YXIgbj10LG89ZG9jdW1lbnRbbig1NDgpXShuKDMyMSkpO2lmKG8peyFmdW5jdGlvbiB0KCl7dmFyIGk9bjt0cnl7dmFyIGE9b1snXHg3M1x4NjhceDYxXHg2NFx4NmZceDc3XHg1Mlx4NmZceDZmXHg3NCddWydceDcxXHg3NVx4NjVceDcyXHg3'  # noqa
        js_data['stcfp'] = 'KGh0dHBzOi8vanMuZGF0YWRvbWUuY28vdGFncy5qczoyOjc5NDc3KQogICAgYXQgdC5leHBvcnRzLmRkX2FjIChodHRwczovL2pzLmRhdGFkb21lLmNvL3RhZ3MuanM6Mjo5NzYwMikKICAgIGF0IGh0dHBzOi8vanMuZGF0YWRvbWUuY28vdGFncy5qczoyOjU1MjIw'  # noqa

    errors_exist = choices([True, False], weights=[0.34, 0.66], k=1)[0]
    if not errors_exist:
        try:
            del js_data['cfpfe']
            del js_data['stcfp']
        except KeyError:
            pass
    else:
        possible_errors = [
            ('RXJyb3I6IENhbm5vdCByZWFkIHByb3BlcnRpZXMgb2YgbnVsbA==', 'YmQ5YjhiNDJmMDYuanM6MjoxMzA4MTYpCiAgICBhdCBNZXNzYWdlUG9ydC5UIChodHRwczovL3d3dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1sYy1tb3phcnQtY29tbW9ucy9yZWFjdC1kb20uNmNlNDZjYTE4YmQ5YjhiNDJmMDYuanM6MjoxMzEzNDgp'),  # noqa
            ('RXJyb3I6IENhbm5vdCByZWFkIHByb3BlcnRpZXMgb2YgbnVsbA==', 'dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1tb3phcnQvMi4zLjYtcmVxdWlyZS5qczoyOjEzNDcxCiAgICBhdCBlYWNoIChodHRwczovL3d3dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1tb3phcnQvMi4zLjYtcmVxdWlyZS5qczoyOjEwMjAp'),  # noqa
            ('ZnVuY3Rpb24oKXt2YXIgbj10LG89ZG9jdW1lbnRbbig1NDgpXShuKDMyMSkpO2lmKG8peyFmdW5jdGlvbiB0KCl7dmFyIGk9bjt0cnl7dmFyIGE9b1snXHg3M1x4NjhceDYxXHg2NFx4NmZceDc3XHg1Mlx4NmZceDZmXHg3NCddWydceDcxXHg3NVx4NjVceDcyXHg3', 'KGh0dHBzOi8vanMuZGF0YWRvbWUuY28vdGFncy5qczoyOjc5NDc3KQogICAgYXQgdC5leHBvcnRzLmRkX2FjIChodHRwczovL2pzLmRhdGFkb21lLmNvL3RhZ3MuanM6Mjo5NzYwMikKICAgIGF0IGh0dHBzOi8vanMuZGF0YWRvbWUuY28vdGFncy5qczoyOjU1MjIw'),  # noqa
            ('RXJyb3I6IENhbm5vdCByZWFkIHByb3BlcnRpZXMgb2YgbnVsbA==', 'dCBodHRwczovL3d3dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1zZW50cnkvbGMtc2VudHJ5LmpzOjI6MzA4NzM0CiAgICBhdCBodHRwczovL3d3dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1zZW50cnkvbGMtc2VudHJ5LmpzOjI6MzA4NzM3'),  # noqa
            ('ZnVuY3Rpb24oaCxvLHQsaixhLHIpe2guaGo9aC5oanx8ZnVuY3Rpb24oKXsoaC5oai5xPWguaGoucXx8W10pLnB1c2goYXJndW1lbnRzKX07aC5faGpTZXR0aW5ncz17aGppZDoxMzM5ODQxLGhqc3Y6Nn07YT1vLmdldEVsZW1lbnRzQnlUYWdOYW1lKCdoZWFkJylb', 'NykKICAgIGF0IGh0dHBzOi8vY2RuLnRhZ2NvbW1hbmRlci5jb20vNjUwNS90Y19MYUNlbnRyYWxlX2FwcHNfMjYuanM6NDA3OjQ4MgogICAgYXQgaHR0cHM6Ly9jZG4udGFnY29tbWFuZGVyLmNvbS82NTA1L3RjX0xhQ2VudHJhbGVfYXBwc18yNi5qczo0MDc6NjE5'),  # noqa
            ('ZnVuY3Rpb24odCl7dmFyIG8saSxhLHM9d2luZG93Ll9oakRvY3VtZW50fHxuO2lmKHIuc2VsZWN0b3I9dCxyLmlzV2luZG93KHQpKXJldHVybiB0aGlzWzBdPXdpbmRvdyx0aGlzLmxlbmd0aD0xLHRoaXM7aWYoci5pc0RvY3VtZW50KHQscykpcmV0dXJuIHRoaXNb', 'czovL3NjcmlwdC5ob3RqYXIuY29tL21vZHVsZXMuOGRhMzNhOGY0NjljM2I1ZmZjZWMuanM6MjoxNjQ5NzcpCiAgICBhdCBPYmplY3QuX3J1biAoaHR0cHM6Ly9zY3JpcHQuaG90amFyLmNvbS9tb2R1bGVzLjhkYTMzYThmNDY5YzNiNWZmY2VjLmpzOjI6NDA3MjYp'),  # noqa
            ('RXJyb3I6IENhbm5vdCByZWFkIHByb3BlcnRpZXMgb2YgbnVsbA==', 'LW1vemFydC1jb21tb25zL2xjLXVpLjg5ZTFlYTI1ODNiNTVkYjQyZTkxLmpzOjI6ODg3ODApCiAgICBhdCBIVE1MRGl2RWxlbWVudC5yIChodHRwczovL3d3dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1zZW50cnkvbGMtc2VudHJ5LmpzOjI6NDU1NjYp'),  # noqa
            ('RXJyb3I6IENhbm5vdCByZWFkIHByb3BlcnRpZXMgb2YgbnVsbA==', 'Ly93d3cubGFjZW50cmFsZS5mci9zdGF0aWMvZnJhZ21lbnQtYnVkZ2V0L2J1ZGdldC1lMzBkOGRkMC5qczoxOjk2NDAxCiAgICBhdCByIChodHRwczovL3d3dy5sYWNlbnRyYWxlLmZyL3N0YXRpYy9mcmFnbWVudC1zZW50cnkvbGMtc2VudHJ5LmpzOjI6NDU1NjYp'),  # noqa
            ('RXJyb3I6IENhbm5vdCByZWFkIHByb3BlcnRpZXMgb2YgbnVsbA==', 'stcfp=L3RyYWNraW5nLWZkZTY1Zjk4LmpzOjI6NDg5MjcpCiAgICBhdCBUdC5uZXh0ICg8YW5vbnltb3VzPikKICAgIGF0IHIgKGh0dHBzOi8vd3d3LmxhY2VudHJhbGUuZnIvc3RhdGljL2ZyYWdtZW50LXRyYWNraW5nL3RyYWNraW5nLWZkZTY1Zjk4LmpzOjI6NDkwMDIp'),  # noqa
        ]
        js_data['cfpfe'], js_data['stcfp'] = choice(possible_errors)


def update_event_keys(js_data, event_counters):
    '''
    In the jsData dictionary, there are parameters related to keyboard, mouse
    and touchscreen. Analyzing the data obtained when using the application on
    a real smartphone, as well as the tags.js file, the following dependencies
    were obtained.
    '''
    def get_ratio(dividend, divisor):
        if not divisor:
            return -1
        result = dividend / divisor
        if result.is_integer():
            result = int(result)
        return result

    if not event_counters:
        for k in EVENT_KEYS_IN_JS_DATA:
            del js_data[k]
        return

    scroll = event_counters['scroll']
    move = event_counters['mousemove']
    click = event_counters['click']
    js_data['m_s_c'] = scroll
    js_data['m_m_c'] = move
    js_data['m_c_c'] = click
    js_data['m_cm_r'] = get_ratio(click, move)
    js_data['m_ms_r'] = get_ratio(move, scroll)

    if not move and not click or move != click:
        del js_data['tbce']
    if not move:
        del js_data['m_fmi']


def process_js_data(js_data):
    referer = '.espacevo.'
    prev_token = 'test token'
    event_counters = {'scroll': 3, 'mousemove': 4, 'click': 6}

    user_agent, lang = generate_user_agent_and_lang()
    phone = re.findall(r'\d;\s(.+)\sBuild', user_agent)[0]
    assert phone, 'no phone in user-agent'
    phone_specs = PHONES[phone]
    br_h, br_w = phone_specs['browser_size']
    rs_h, rs_w, rs_cd = phone_specs['screen_params']
    gpu_vender, gpu_render = phone_specs['gpu']
    is_app = False if referer.startswith(
        'https://pros.lacentrale') or '.espacevo.' in referer else True

    js_data['ttst'] = get_ttst_param()
    js_data['hc'] = phone_specs['cpu_cores']
    js_data['br_oh'] = br_h
    js_data['br_ow'] = br_w
    js_data['ua'] = user_agent if is_app else CHROME_UA
    js_data['tagpu'] = get_tagpu_param()
    js_data['br_h'] = br_h
    js_data['br_w'] = br_w
    js_data['nddc'] = 1 if prev_token else 0
    js_data['rs_h'] = rs_h
    js_data['rs_w'] = rs_w
    js_data['rs_cd'] = rs_cd
    js_data['lg'] = lang
    js_data['pr'] = phone_specs['pixel_ratio']
    js_data['ars_h'] = rs_h
    js_data['ars_w'] = rs_w
    js_data['tz'] = -120  # set as France
    js_data['dvm'] = phone_specs['device_memory']
    js_data['wdw'] = False if is_app else True
    js_data['psn'] = False if is_app else True
    js_data['glvd'] = gpu_vender
    js_data['glrd'] = gpu_render
    js_data['jset'] = int(time())

    if is_app:
        del js_data['cokys']

    if not referer:
        del js_data['dcok']

    opts_key_exist = choices([True, False], weights=[0.05, 0.95], k=1)[0]
    if not opts_key_exist:
        del js_data['opts']
        del js_data['xhr_opts']

    wwl_key_exist = choices([True, False], weights=[0.75, 0.25], k=1)[0]
    if not wwl_key_exist:
        del js_data['wwl']

    log2_key_exist = choices([True, False], weights=[0.66, 0.34], k=1)[0]
    if not log2_key_exist:
        del js_data['log2']

    update_error_keys(js_data, referer, prev_token)
    update_event_keys(js_data, event_counters)

    return js_data


if __name__ == '__main__':
    jsdata = process_js_data(JS_DATA)
    for k, v in jsdata.items():
        print(f'{k}: {v}')
