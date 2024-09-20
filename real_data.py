from string import Template


APP_VERSIONS = ('10.4.0',)
ANDROID_VERSION_BUILD_IDS = {
    '10': ('QKQ1.190910.002', 'QP1A.190711.020'),
    '12': (
        'SP1A.210812.016', 'SQ1A.211205.008', 'SP1A.211105.002',
        'SP1A.210812.015'),
    '13': ('TKQ1.221013.002',),
    '14': (
        'AP2A.240705.004', 'AP2A.240805.005', 'AP2A.240605.024',
        'AP1A.240505.005', 'AP1A.240405.002', 'UKQ1.231207.002',
        'UKQ1.230917.001'),
}
CHROME_VERSIONS = (
    '128.0.6613.40',
    '127.0.6533.103',
    '127.0.6533.84',
    '127.0.6533.65',
    '127.0.6533.64',
    '126.0.6478.188',
    '126.0.6478.186',
    '126.0.6478.111',
    '125.0.6422.186',
    '125.0.6422.166',
    '124.0.6367.172',
    '124.0.6367.159',
    '124.0.6367.42',
    '123.0.6312.121',
    '123.0.6312.119',
    '123.0.6312.118',
    '123.0.6312.100',
)
PHONE_LANGS = ('ru-RU', 'en-US', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'pt_PT')
PHONES = {
    'MI 8 Lite': {
        'android': ('10',),
        'browser_size': (696, 393),
        'screen_params': (830, 393, 24),
        'pixel_ratio': 2.75,
        'device_memory': 4,
        'gpu': ('Qualcomm', 'Adreno (TM) 512'),
        'cpu_cores': 8,
    },
    'Pixel 7': {
        'android': ('14',),
        'browser_size': (783, 412),
        'screen_params': (915, 412, 24),
        'pixel_ratio': 2.625,
        'device_memory': 8,
        'gpu': ('ARM', 'Mali-G710'),
        'cpu_cores': 8,
    },
    'Pixel 6a': {
        'android': ('14',),
        'browser_size': (784, 412),
        'screen_params': (915, 412, 24),
        'pixel_ratio': 2.625,
        'device_memory': 6,
        'gpu': ('ARM', 'Mali-G78'),
        'cpu_cores': 8,
    },
    'M1908C3JGG': {
        'android': ('12',),
        'browser_size': (719, 393),
        'screen_params': (851, 393, 24),
        'pixel_ratio': 2.75,
        'device_memory': 4,
        'gpu': ('ARM', 'Mali-G52'),
        'cpu_cores': 8,
    },
    '2107113SG': {
        'android': ('14',),
        'browser_size': (994, 393),
        'screen_params': (873, 393, 24),
        'pixel_ratio': 2.75,
        'device_memory': 8,
        'gpu': ('Qualcomm', 'Adreno (TM) 660'),
        'cpu_cores': 8,
    },
    'M2012K11AG': {
        'android': ('14',),
        'browser_size': (1483, 513),
        'screen_params': (1140, 513, 24),
        'pixel_ratio': 2.106250047683716,
        'device_memory': 4,
        'gpu': ('Qualcomm', 'Adreno (TM) 650'),
        'cpu_cores': 8,
    },
    '2201123G': {
        'android': ('14',),
        'browser_size': (738, 393),
        'screen_params': (873, 393, 24),
        'pixel_ratio': 2.75,
        'device_memory': 8,
        'gpu': ('Qualcomm', 'Adreno (TM) 730'),
        'cpu_cores': 8,
    },
    'M2102J20SG': {
        'android': ('13',),
        'browser_size': (667, 360),
        'screen_params': (800, 360, 24),
        'pixel_ratio': 3,
        'device_memory': 4,
        'gpu': ('Qualcomm', 'Adreno (TM) 640'),
        'cpu_cores': 8,
    },
}
CHROME_UA = (
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/127.0.0.0 Mobile Safari/537.36')
APP_UA_TEMP = Template(
    'Mozilla/5.0 (Linux; Android $android_version; $phone '
    'Build/$build_id; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Version/4.0 Chrome/$chrome_version Mobile Safari/537.36 #Android;'
    'android$android_version;$app_version')
