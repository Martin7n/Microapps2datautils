

VEHICLE_WEIGHT_CLASSES = {
    "motorcycle": (50, 500),
    "car": (800, 2500),
    "large_car_suv": (1500, 3500),
    "lcv": (1800, 4500),          # vans, pickups, light commercial
    "medium_duty": (3500, 12000), # trucks, box trucks, small rigids
    "heavy_duty": (12000, 40000),  # heavy trucks, articulated tractors
    "extra_heavy": (40000, 90000)  # special trucks, dumpers, etc.
}



VEHICLE_CATEGORY_MAPPING = {
    "Motorcycle": ["L3e", "L4e", "L5e"],
    "Car": ["M1", "M1G"],
    "LgtComrclVeh": ["N1"],
    "Trailer": ["O1", "O2", "O3", "O4"],
    "MedDutyTruck": ["N2"],
    "HvyDutyTruck": ["N3"],
}


VEHICLE_CATEGORY_MAPPING =  {
    k.lower(): v
    for k, v in VEHICLE_CATEGORY_MAPPING.items()
}

V_W_CAT = VEHICLE_CATEGORIES = {
    # L category
    "L3e": (50, 500),        # Motorcycle
    # M category
    "M1": (800, 3500),       # Passenger car
    "M1G": (800, 3500),      # Off-road passenger car
    # N category
    "N1": (1800, 3500),      # Light commercial vehicle
    "N2": (3500, 12000),     # Medium truck
    "N3": (12000, 40000),    # Heavy truck
    # O category (trailers)
    "O1": (0, 750),
    "O2": (750, 3500),
    "O3": (3500, 10000),
    "O4": (10000, 40000),
}


MAIN_CATEGORIES = {
"Motorcycle":"Motorcycle",
"Car":"Car",
"LgtComrclVeh":"LgtComrclVeh",
"Trailer":"Trailer",
"MedDutyTruck":"MedDutyTruck",
"HvyDutyTruck":"HvyDutyTruck",
"Other":"Other"
    }


CATEGORIES_BY_SOURCE_BG = {
    # M1 - passenger cars
    "лекотоварен": "N1",
    "Лек с 6 + 1 места / 7 м": "M1",
    "Лек с 4 + 1 места / 5 м": "M1",
    "Лек с 1 + 1 места / 2 м": "M1",
    "Лек с 3 + 1 места / 4 м": "M1",
    "Лек с 8 + 1 места / 9 м": "M1",
    "Лек с 7 + 1 места / 8 м": "M1",
    "Лек с 5 + 1 места / 6 м": "M1",
    "Лек с 2 + 1 места / 3 м": "M1",
    "ЛЕК": "M1",
    "Лек": "M1",

    # N1/N2/N3 - goods vehicles
    "Товарен 6 + 1": "N1",
    "Товарен 4 + 1 места / 5 м": "N1",
    "Товарен 1 + 1 места / 2 м": "N1",
    "Товарен 2 + 1 места / 3 м": "N1",
    "Товарен 3 + 1 места / 4 м": "N1",
    "Товарен 5 + 1 места / 6 м": "N1",
    "Товарен": "N1",
    "Товарен фургон": "N1",
    "Товарен до 5 т. Товароносимост": "N2",
    "Товарен до 10 т. Товароносимост": "N2",
    "Товарен до 15 т. Товароносимост": "N3",
    "ТОВАРЕН БОРДОВИ": "N1",
    "товарен до 12т": "N2",
    "Товарен автомобил - хладилник": "N1",
    "Товарен - хладилник": "N1",
    "Товарен автомобил - цистерна": "N2",
    "Товарен контейнеровоз": "N2",
    "Бетоновоз": "N2",
    "Самосвал": "N2",
    "Автовоз": "N2",
    "СПЕЦИАЛЕН ТОВАРЕН АВТОМОБИЛ": "N2",
    "Специален товарен автомобил - Мултилифт": "N2",

    # Tractor units
    "Седлови влекач": "N3",
    "ВЛЕКАЧ": "N3",
    "ВЛЕКАЧ ТЕГЛЕНЕ НА ПОЛУРЕМАРКЕ": "N3",

    # Trailers - O category
    "Ремарке": "O1/O2",
    "РЕМАРКЕ ТОВАРЕН": "O2",
    "РЕМАРКЕ ЗА ТОВАРЕН АВТОМОБИЛ": "O2",
    "Ремарке за лек": "O1",
    "Ремарке за лек - къмпинг": "O1",
    "Полуремарке": "O3/O4",
    "ПОЛУРЕМАРКЕ ТОВАРЕН": "O3",
    "ПОЛУРЕМАРКЕ БОРДОВИ": "O3",
    "ПОЛУРЕМАРКЕ ФУРГОН": "O3",
    "Полуремарке Хладилник": "O3",
    "Полуремарке Цистерна": "O3",
    "ПОЛУРЕМАРКЕ САМОСВАЛ": "O3",
    "Тракторно ремарке": "O2",
    "Специализирано товарно ремарке - контейнеровоз": "O3",
    "Специализирано ремарке": "O2",
    "РЕМАРКЕ ЦИСТЕРНА": "O3",

    # L category
    "Мотоциклет": "L3e",
    "мотопед": "L1e",
    "Четириколесно ПС": "L7e",

    # Bus
    "Автобус": "M2/M3",

    # Agricultural machinery
    "Земеделска техника": "other",
    "Земеделска и горска транспортна техника": "other",
    "КОЛЕСЕН ТРАКТОР": "other",
    "Трактори": "other",
    "Верижен трактор": "other",

    # Construction / special purpose vehicles
    "Специализирани строителни машини": "other",
    "Багер": "other",
    "Колесен багер": "other",
    "Мини багер": "other",
    "Компактен багер": "other",
    "Верижен багер": "other",
    "Комбиниран багер-товарач": "other",
    "Багер товарач": "other",
    "САМОХОДНА МАШИНА - БАГЕР": "other",
    "Колесен товарач": "other",
    "Челен товарач": "other",
    "Колесен челен товарач": "other",
    "Верижен товарач": "other",
    "МИНИ ЧЕЛЕН ТОВАРАЧ": "other",
    "Дъмпер": "SPV",
    "Автокран": "SPV",
    "Бетон помпа": "SPV",
    "БЕТОН-ПОМПА": "SPV",
    "БЕТОНОБЪРКАЧКА": "SPV",
    "Асфалтополагаща машина": "other",
    "Верижен асфалтополагач": "other",
    "Колесен асфалторазстилач": "other",
    "Грейдер": "other",
    "Пътна фреза": "other",
    "Компактор": "other",
    "Стабилизатор/рециклер": "other",
    "Сонда": "other",
    "Сондажна машина": "other",

    # Other machinery / attachments
    "Телескопичен товарач": "other",
    "телескопичен манипулатор": "other",
    "Телехендлер": "other",
    "Сеялка": "other",
    "Сламопреса": "other",
    "Пръскачка": "other",
    "Комбайн": "other",
    "Зърнокомбайн": "other",
    "Гроздокомбайн": "other",
    "доматокомбайн": "other",
    "Косачка": "other",
    "Плуг": "other",
    "Култиватор": "other",
    "Дискова брана": "other",
    "Хедер": "other",
    "Адаптер за царевица": "other",
    "Адаптер за слънчоглед": "other",

    # Water/air vehicles
    "Моторна яхта": "other",
    "Плавателно средство - ПС": "other",
    "Самолет": "other",
    "Хеликоптер": "other",
}

CATEGORIES_BY_SOURCE_BG = {
    k.lower(): v
    for k, v in CATEGORIES_BY_SOURCE_BG.items()
}


CATEGORIES_BY_SOURCE = {
        "лек автомобил": "car",
    "товарен автомобил": "",
    "влекач": "",
    'Car, 6+1 seats/7 s': 'car',
    'Car, 4+1 seats/5 s': 'car',
    'Car': 'car',
    'Semi trailer': 'trailer',
    'Truck, 2+1 seats/3 s': 'truck',
    'Truck, 1+1 seats/2 s': 'truck',
    'Truck, 4+1 seats/5 s': 'truck',
    'Four wheel vehicle / ATV': 'atv',
    'Semi truck': 'Truck',
    'Car, 3+1 seats/4 s': 'car',
    'Товарен 6 + 1': 'lcv',
    'Bus': 'bus',
    'TRUCK TRAILER': 'trailer',
    'Special Purpose Vehicle': 'spv',
    'Trailer': 'trailer',
    'Car, 1+1 seats/2 s': 'car',
    'Car, 2+1 seats/3 s': 'car',
    'Truck': 'truck',
    'Truck, 3+1 seats/4 s': 'truck',
    'Car, 8+1 seats/9 s': 'car',
    'Car, 7+1 seats/8 s': 'car',
    'Tracked Asphalt Paver': 'other',
    'Truck, 5+1 seats/6 s': 'truck',
    'Wheel loader': 'other',
    'Car, 5+1 seats/6 s': 'car',
    'Backhoe': 'other',
    'Motor Yacht': 'other',
    'Motorcycle': 'motorcycle',
    'Polivna sistema': 'trailer',
    'Ремарке за лек': 'other',
    'Channeldigger': 'other',
    'Дъмпер': 'other',
    'телескопичен манипулатор': 'other',
    'Телескопичен товарач': 'other',
    'Airplane': 'other',
    'Хедер': 'other',
    'Товарачна уредба': 'other'
    }
CATEGORIES_BY_SOURCE = {
    k.lower(): v
    for k, v in CATEGORIES_BY_SOURCE.items()
}

NONETYPE_KEYWORDS = {
    'плавателно', 'балопреса', 'асфалторазстилач',
    'доматокомбайн', 'сламопреса', 'самоходна', 'фуражосмесител',
    'хеликоптер', 'товарно', 'самолет', 'пръскачка', 'машини',
    'пробивна', 'гроздокомбайн', 'спредер', 'грейдер',
    'трактори', 'шредер', 'фуражно-разд.', 'тракторно', 'сеялка',
    'стабилизатор/рециклер', 'асфалтополагач', 'трактор', 'тороразпръсквач',
     'багер', 'транспортна', 'пролетница', 'фреза', 'царевица', 'хидравлична',
    'силажокомбайн', 'вентилаторна', 'самоходно', 'адаптер', 'манипулатор',
    'земеделска', 'челен', 'телескопичен', 'компактор',
    'сондажна', 'техника', 'азотна', 'брана', 'колесен', 'плуг', 'прикачен',
    'бункер-раздавач', 'палетни', 'чували', 'слънчоглед', 'раздробител',
    'количка', 'течна', 'строителни', 'каналокопател',  'яхта', 'опаковъчна',
    'товарач;', 'поливна', 'ремарке', 'асфалтополагаща', 'колесар', 'машина',
    'зърнокомбайн', 'изпразване', 'горска', 'бетонобъркачка', 'косачка',
    'дъмпер', 'сонда', 'култиватор',  'булдозер', 'товарач', 'мотокар', 'валяк',
    'грейдерно', 'пътна', 'комбайн', 'вилици', 'багер-товарач', 'колесна',
    'пресевна', 'хедер', 'зърно', 'телехендлер', 'верижна', 'верижен'
}



CATEGORIES_BY_SOURCE_2 = {
    # M category - passenger vehicles
    "лекотоварен":"N1",
    "товарен": "N2",
    "лек автомобил": "M1",
    "Car, 6+1 seats/7 s": "M1",
    "Car, 4+1 seats/5 s": "M1",
    "Car": "M1",
    "Car, 3+1 seats/4 s": "M1",
    "Car, 1+1 seats/2 s": "M1",
    "Car, 2+1 seats/3 s": "M1",
    "Car, 8+1 seats/9 s": "M1",
    "Car, 7+1 seats/8 s": "M1",
    "Car, 5+1 seats/6 s": "M1",

    # N category - goods vehicles
    "товарен автомобил": "N1",
    "Товарен 6 + 1": "N1",

    # N2/N3 - trucks
    "Truck, 2+1 seats/3 s": "N2",
    "Truck, 1+1 seats/2 s": "N2",
    "Truck, 4+1 seats/5 s": "N2",
    "Truck, 3+1 seats/4 s": "N2",
    "Truck, 5+1 seats/6 s": "N2",
    "Truck": "N2",
    "Semi truck": "N3",
    "влекач": "N3",

    # O category - trailers
    "Semi trailer": "O3",
    "TRUCK TRAILER": "O3",
    "Trailer": "O1",
    "Polivna sistema": "O1",

    # L category - motorcycles / quadricycles
    "Motorcycle": "L3e",
    "Four wheel vehicle / ATV": "L7e",

    # Other M categories
    "Bus": "M2/M3",

    # Special purpose / other
    "Special Purpose Vehicle": "SPV",
    "Tracked Asphalt Paver": "other",
    "Wheel loader": "other",
    "Backhoe": "other",
    "Motor Yacht": "other",
    "Ремарке за лек": "other",
    "Channeldigger": "other",
    "Дъмпер": "other",
    "телескопичен манипулатор": "other",
    "Телескопичен товарач": "other",
    "Airplane": "other",
    "Хедер": "other",
    "Товарачна уредба": "other",
}



CATEGORIES_BY_SOURCE_TEXT = []




# --- 1. VEHICLE TYPE KEYWORDS ---
# TRAILER_KEYWORDS = [
#     "ремарке",
#     "ремаркета",
#     "полуремарке",
#     # "цистерна",
#     "trailer",
#     "schmitz",
#     "krone",
#     "kogel",
#     "п/рем",
#     "ремарке"
# ]


TRAILER_KEYWORDS = [
    # Generic
    "trailer",
    "semi trailer",
    "semi-trailer",
    "semi",
    "remorque",
    "anhanger",
    "anhänger",

    # Bulgarian
    "ремарке",
    "ремаркета",
    "полуремарке",
    "полу-ремарке",
    "п/рем",
    "прицеп",

    # Common manufacturers
    "schmitz",
    "schmitz cargobull",
    "krone",
    "kogel",
    "kögel",
    "wielton",
    "berger",
    "schwarzmuller",
    "schwarzmüller",
    "fliegl",
    "fliegel",
    "wabash",
    "chereau",
    "fruehauf",
    "leci trailer",
    "benalu",
    "lecitrailer",
    "samro",
    "sor",
    "sor iberica",
    "burg",
    "van hool",
    "kaessbohrer",
    "kässbohrer",
    "ozgul",
    "ozgul trailer",
    "talson",
    "kassbohrer",
    "mega",
    "novatrail",

    # Trailer body types
    "бордово ремарке",
    "бордово полуремарке",
    "платформа",
    # "падащ борд",
    "щора",
    "брезент",
    "мега",
    "контейнеровоз",
    "контейнерно шаси",
    "контейнерно ремарке",
    "шаси",
    "хладилно ремарке",
    "рефрижератор",
    "реф",
    "изотермично",
    "фургон ремарке",
    "автовоз",
    "нископодов",
    "нискорамно",
    "нискорамен",
    "платформа за техника",
    "самосвално ремарке",
    "самосвално полуремарке",
    "зерновоз",
    "силоз",
    "цистерна",
    "битумовоз",
    "цементовоз",
    "дървовоз",
    "дървен материал",
    "лог трейлър",
    "лог ремарке",
    "лесовозно ремарке",

    # Axles
    "2 оси",
    "3 оси",
    "4 оси",
    "двуосно",
    "триосно",
    "четириосно",

    # Common trailer brands in BG
    "hapert",
    "humbaur",
    "wm meyer",
    "eduard",
    "böckmann",
    "boeckmann",
    "brenderup",
    "saris",
    "variant",
    "barthau",
]

LCV_KEYWORDS = [
    "35c", "35s", "35ц", "35с",
    "daily",
    "314", "316",
    "lcv",
    "бус",
    "фургон",
    "trafic",
    "ducato",
    "460",
    "dokker",
    "n1",

    # Toyota
    "hilux",

    # VW
    "transporter",
    "транспортер",

    # Ford Transit
    "350", "t350", "ft350",
    #"custom",
    "transit",
    "транзит",
    "l3h2",

    # Mercedes Sprinter
    "311", "313", "314", "316", "319",
    "sprinter3",

    # Large vans
    "master", "мастер",
    "boxer", "боксер",
    "jumper", "джъмпер",
    "crafter", "крафтер",
    "movano",
    "interstar",

    # Small/Medium vans
    "caddy", "кади",
    "partner", "партнер",
    "berlingo", "берлинго",
    "kangoo", "канго",
    "fiorino",
    "doblo",
    "scudo",
    "vito", "вито",
    "e-rifter",

    # Generic
    "3.5t",
    "3.5т",
    "3,5t",
    "3,5т",
    "лекотоварен",
    "товарен до 3.5",
    "L1H1", "L2H2", "L3H2", "L3H3", "L4H3",
]


CAR_KEYWORDS = [
    "лекавтомобил",
    "лек автомобил",

    "reev",

    "октавия",
    "скала",
    "шайн",
    "джук",

    "panamera",
    "taycan",
    "corolla",
    "shine",
    "tesla",
    "zr-v",
    "sandero",
    "c-hr",
    "ц-hr",
    "ioniq",
    "ev3",
    "ev6",
    "amg",
    "vitara",
    "swift",
    "forthing",
    "taigo",
    "polo",
    "citiray",
    "car",
    "suv",
    "mpv",
    "седан",
    "хечбек",
    "комби",
    "puma",
    "hr-v",
    "nammi",
    "starray",
    "s800"
]


HGV_KEYWORDS = ["РІР»РµРєР°С‡", "daf","semi truck" "РјР°РЅ", "man",  "РєР°РјРёРѕРЅ", "hgv", "tge", "tga", "actros", "scania", "tgx", "fh16",
                #"iveco", "516", "517", "519", "С‚РѕРІР°СЂРµРЅ Р°РІС‚РѕРјРѕР±РёР»",
                ]



VEHICLE_TYPES_VIN = {

"лекотоварен": ['VF3YCBP', 'VF37ABH', 'VR7EHHN', 'VR7EUHN', 'W1VVLBE', 'WDB9066', 'VF3YDF6', 'VXEYCF6', 'W1V3MDF', 'VF6MH00', 'W1V5MC3', 'WF0RXXT', 'WF0SXXW', 'W1V3KCF', 'W1VGH2F', 'VF3YD2M', 'VR7ENZK', 'LDFHGT1', 'VR79AZ2', 'VF7VFEH', 'VF7YBAP', 'VF7YAAP', 'VXEVBYH', '7MW4LTR', 'VF1FW50', 'VF6TDB0', 'VF7YDCP', 'VF3YCBN', 'VF3V1ZK', 'VXEYCAP', 'VF7YDBN', 'VF7V1ZK', 'UU18SDX', 'VF3YCAP', 'VF7YCBN', 'W0VEAZK', 'W1V3KBF', 'W0L6ZZA', 'VXEYAE6', 'VXEVFEH', 'W0VENZK', 'WF0DXXT', 'W1VFHBF', 'YARVBYH', 'ZD3TE16', 'YARVLEH', 'WF0WXXT', 'VR3EAZK', 'VF3YAAN', 'VF7VLEH', 'VF3VBYH', 'VF1FW00', 'VF7YBAN', 'VF7YDG6', 'VF7YCAP', 'VR7CHHP', 'VF77DBH', 'VF7VTZK', 'VF3YDCN', 'VXEYDG6', 'W0L4F72', 'VXEVLEH', 'W1V3HCF', 'VXEYDCP', 'W0VF7D6', 'WF04NBE', 'W1V5KDF', 'WMA08VU', 'ZCFC450', 'ZD3E7M9', 'JS1EM12', 'JS1EJ11', 'JH2RH12', 'JH2RH11', 'JH2PC69', '7MW2LTR', 'JS1EM11', 'CXEYCAP', 'NL6A21R', 'SBM22GC', 'TYBFEC7', 'MLHRH15', 'MLHJC92', 'VF37EBH', 'VF7YD2M', 'VF1MD00', 'VF3YABP', 'VF7YB2M', 'VF3YDCP', 'VF6TDAE', 'VF1FW18', 'VF1FW17', 'VFMA000', 'VF17R0J', 'UU18SDR', 'VF3VZKX', 'VF3YCG6', 'VF7VJYH', 'VBKTU74', 'VNVNDA0', 'VF3YC1M', 'VF3YBF6', 'VF3YBE6', 'W0VMR36', 'W0VF7G6', 'VXEYBBP', 'VXEYAAP', 'W1V3MBT', 'VSKYAAM', 'VR7RDYH', 'WF04NCE', 'W1V5MDF', 'W1V5M33', 'WF04N1E', 'W1V4476', 'WF0CXXS', 'WDB9076', 'W1VGHBF', 'W1V5M2F', 'W1V5KCF', 'W1V4206', 'W1V3MCF', 'YAREAZK', 'ZD3E7M4', 'X96A21R', 'ZAPNP6B', 'ZFF96NM', 'YARVFEH', 'YARVFAH', 'ZD3EC16', 'WPOZZZ9', 'ZD3EC18', 'ZFF90HM'],
"влекач": ['XLRTEF5', 'XLRTEH4', 'YV2RT40', 'VF610A3', 'WMA06KZ', 'YV2RTY0', 'WDB9634', 'NM0MKXT', 'VF611A3', 'XLRASF5', 'YS2S4X2', 'NM0KCXT', 'WMA20FZ', 'YS2K6X2', 'YS2K4X2', 'WDF9634', 'WMA06XZ', 'WMA06JZ', 'VF631S3', 'YS2P4X2', 'ZCFM62A', 'NM0LKXT', 'NM0KKXT', 'W1T9630', 'WMA13KZ', 'ZCFJ64C', 'WJMJ4CT', 'WDB9630', 'ZCNH984', 'WMA15FZ', 'YV2XZY0', 'YS2P8X4', 'YV2XTY0', 'YV2RTW0', 'WJMJ64C', 'XLRASM4', 'ZCFA81T', 'в„–...', 'VF611A1', 'XLRASH4', 'ZCFMG2A', 'ZD3TE16', 'WMA39SZ', 'WJMM62A', 'WMA30JZ', 'ZCFC150', 'YS2G4X2', 'NLRTNHK', 'VF620J1', 'VNE6036', 'W1T9640', 'W17T963', 'WEB6283', 'WMA18XZ', 'YV2T0U1', 'ZCFJE4C', 'YS2R6X4', 'YV2XTR0', 'YS2G6X2', 'WMAN14Z', 'ZD3E7M9', 'YV2XT40', 'ZCFD070', 'XLRTGH4', 'WMAN15Z', 'WMA21XZ', 'XLRAEL3', 'ZCFCN50', 'ZCFCD35', 'ZCFCA50', 'LXGDPA6', 'JS1EM12', 'JS1EJ11', 'JH2RH12', 'JH2RH11', 'JH2PC69', 'JS1EM11', 'GLW1511', 'NMC633E', 'NLRTMF1', 'NNAM0B6', 'NM0LTXT', 'NM0KCTP', 'MLHRH15', 'NNAM0BE', 'SUU206U', 'MLHJC92', 'в„–BCN123', 'в„–210800', 'VF610C3', 'VF6VFE0', 'VF621N8', 'UU18SDN', 'VBKTU74', 'W1T9643', 'W119634', 'W1T9834', 'WDB9062', 'WDB9644', 'WDB9642', 'ZD3E7M4', 'WMAN16Z', 'WLFA21C', 'XLRADM4', 'WMA73SZ', 'WMA10XZ', 'WLFA54B', 'ZCFC035', 'WMA49SZ', 'WMA18VU', 'WMA05XZ', 'WLFA42C', 'ZCFC435', 'ZCFC335', 'YV2X9RO', 'WMAN46Z', 'YV2X9J0', 'ZD3EC16', 'WMA82EZ', 'YV2T0W1', 'WMA59SZ', 'YS2R6X2', 'YV2RT60', 'YS2P6X4', 'ZCFC235', 'ZCFCG35', 'WMA10VU', 'WLFA52B', 'ZD3EC18', 'WLFA32A', 'WJMMG2A', 'WJMM1VU', 'WFN2RTL',
            'ZCFA62A', 'ZCFEE2S', 'ZCFE62R'],

"лек": ['VF1RFB0', 'U5YH481', 'VF1RJB0', 'VF1RHN0', 'U5YPV81', 'WAUZZZF', 'VR3USHN', 'WVGZZZC', 'VF1RJL0', 'NMTBA3B', 'JMZKFGW', 'TMAJD81', 'NLHDM51', 'VF3MCYH', 'KNADB51', 'TMAJC81', 'NMTBD3B', 'TMAJE81', 'JMZKH0H', 'NMTK53B', 'JN1T33J', 'WVWZZZ3', 'NMTK33B', 'VF1AG00', 'VXKUSHN', 'SJNTANJ', 'NLHBM51', 'U5YPX81', 'WVGZZZA', 'VR3FPHN', 'TSMLYED', 'VR3UPHN', 'LMXA14A', 'VR3KAHP', 'KNAD681', 'U5YH151', 'WAUZZZG', 'SJNFAAF', 'TMAJB81', 'TSMJYBD', 'U5YPU81', 'VXKUPHN', 'VF7SXHM', 'JSAZCED', 'AHTKB3C', 'W0V7D9E', 'JTDKBAB', 'UU1DBG0', 'JTMD63F', 'WVWZZZC', 'JTPAAAA', 'VF1RCB0', 'WAUZZZ4', 'LGWEE4A', 'YARKBAC', 'SJNFFAJ', 'VSSZZZK', 'JMZDM6W', 'VF3MRHN', 'JTDKGNE', 'JSAAZCA', 'TSMJYAD', 'KNACP81', 'WP1ZZZ9', 'LGWFF6A', 'JTMR63F', 'JMZKL0H', 'JTDAGNA', 'TMBAR8N', 'TMBEK6N', 'KMHK281', 'W0V7H9E', 'VF7SZHM', 'VF1RFE0', 'JN1T33T', 'NLHDN51', 'VXKFPHN', 'JF1BT9L', 'JMZKF6W', 'JTEBR3F', 'JTNB23H', 'SJNTBAJ', 'TSMLYDD', 'TMBEP7N', 'VR3FBYH', 'JMZGL62', 'TSMLYEH', 'TMAK281', 'LVZA53P', 'KMHHB81', 'JTNADAD', 'JTNABAC', 'TMBJR8N', 'TMAH251', 'VR7BAHN', 'VF1R980', 'KNADC51', 'JTDKAAB', 'JHMRT68', '5TDLB3C', 'NLHBN51', 'AHTBA3C', 'JTPABAC', 'TMAH281', 'TMBLN9N', 'VR1J45G', 'LGWFFVA', 'TMBAJ8N', 'NMTBZ3B', 'U5YH5F1', 'JHMRV58', 'KMHKR81', 'KMHK381', 'LVHRS68', 'VR3UPHM', 'VXKUSHP', 'TMBGK6N', 'VF1RZG0', 'KNARH81', 'VF3M45G', 'VNKKG3D', 'U5YH4F1', 'TMBAG8N', 'SB1KB3A', 'U5YH7F1', 'VR3UHZK', 'UU1K522', 'VR3USHP', 'NLHBM81', 'VR7BDHN', 'WF0FXXW', 'LB37622', 'JHMFL48',
            'SB1Z93B', 'VR3FCYH', 'WV2ZZZS', 'JM4BP6S', 'JMZGL69', 'KMHK581', 'JMZDJ6H', 'TMBJJ8N', 'SB1K93B', 'VXKKAHP', 'LGWEFUA', 'KNAB251', 'KMHS581', 'JTDKCAC', 'JTMR43F', '3MVDM6W', 'TMAH881', 'TMAJA81', 'TMBJR7N', 'VR3FRHN', 'VR3UKZK', 'VXKUKZK', 'JTPABAA', 'TSMZB3A', 'VNVK140', 'LGJE1EE', 'JTEAREA', 'TMBEP6N', 'W1N1671', 'TMBER6N', 'SB1ZB3A', 'SJNFCAF', 'W1K2231', 'XP7YGCE', 'LHGRZ48', 'TMBEP6P', 'TMBLN9P', 'VF1RFD0', 'JTME63F', 'NLHB251', 'VF3MJEH', 'VR7BBYH', 'VR7CCHP', 'WBA21EN', 'KMHHC81', 'W1N1679', 'LMXG14D', 'JM4BP6H', 'JTPACAB', 'JF1SKEL', 'TSMJYAH', 'SB1Z53B', 'TMAH351', 'UU1B522', 'VNKKAAC', 'W1NKJ5B', 'WF02XXE', 'JTNACAB', 'TMBLE9N', 'TMBCR9N', 'VR3F3DG', 'W1NFB3D', 'JSAMFH9', 'LGWEEUA', 'TMBEK7N', 'U5YH581', 'VXKUPHM', 'YARKAAC', 'JF1GTEL', 'JMZDMFW', 'LVZZU3P', 'JTMABBB', 'JTNAGAC', 'NLHA751', 'SJNJ12T', 'U5YH2G1', 'VXKUHZK', 'WV2ZZZ7', 'WP0ZZZY', 'KMHC751', 'JTMRW3F', '6FPPXXM', 'KMHYC81', 'VF1ML00', 'W1NKM5B', 'VXKFRHN', 'JHMGR68', 'JTJCKBE', 'JTJDGKC', 'TMBLR9N', 'TMBAM9N', 'TSMLYDH', 'VR7ACYH', 'VNKKBAC', 'W1NDM4E', 'W0VZT6E', 'W0VZCYH', 'W1N1673', 'WBA31CA', 'JF1SLEL', 'JF1GUEL', 'KMHP581', 'JTJCJBG', 'KMHYF81', 'KNAFC81', 'TMBLJ9N', 'NLHBN81', 'TMBLJ8N', 'TMBGK7N', 'VF7SXHN', 'VF3MRHP', 'W1K2060', 'W0VZRHN', 'WBA31EM', 'WBA11EV', 'WVWZZZE', 'KMHP481', 'KMHS481', 'KMHB551', 'JMBXDGL', 'KPT20B1', 'LGWEF6A', 'LVHRS88', 'TMBGR7N', 'VR7ND5G', 'W1NKJ0F', 'W1NWH5A', 'W0VZ45G', 'VYSP010', 'WF0NXXG', 'WBY11CF', 'WBA51EH', 'ZFA5FBB',
            'WVGZZZR', 'WUAZZZF', 'JTMD43F', 'KMHM541', 'JSTGBRF', 'TMAJ381', 'VR3UPHP', 'W1NFB0K', 'W1NFD6B', 'WBA21EJ', 'WBS21CS', 'WBY8P21', 'KMHLN41', 'LGWDB61', 'JTMW53F', 'SAL1A2B', 'TMBAR9N', 'TMBER6P', 'VF72RHN', 'VR1F45G', 'VF3DDYH', 'U5YH251', 'W1NKM4H', 'VXKCSHP', 'WV5ZZZT', 'KNACR81', 'KMHC851', 'JMZDR1W', 'JTJCKBF', 'L6TCX2E', 'JTHU95B', 'TMBJG7N', 'TMBLJ7N', 'SALKABB', 'TMAK381', 'U5YPK81', 'VF3LBYH', 'W1K6G8C', 'WBY8P61', 'WF01NBE', 'WBY21CF', 'WVGZZZE', 'LB3FX1S', 'JTMJ63F', 'KNADD81', 'JSAMFJ9', 'NMTBE3B', 'SB1ZC3C', 'U5YPG81', 'U5YH6G1', 'UU10SDP', 'VR3EZZK', 'U5YH651', 'VR1JCYH', 'W1NFF8H', 'W1NFD0K', 'W1N4M4F', 'W1NFB5K', 'W1K6G7G', 'W1KLF0F', 'WBA41EU', 'WBATB41', 'WF0PXXG', 'WDC1671', 'WF03NAE', 'WBATH41', 'YV1LFH5', 'YV1LFK2', 'JTJCMBH', '3MVDMFW', 'JF1GT3L', 'TMBCJ8N', 'NMTKZ3B', 'TMBAH9N', 'TMBAJ9N', 'TMBJG8N', 'VNKKFAF', 'VR1FRHN', 'VR7NDDG', 'W1NKM0F', 'W0VBD6E', 'W1N2476', 'W1K2938', 'W1NKJ8H', 'W1NFF8F', 'W1KLF5G', 'W1NFD4G', 'W1NKJ4H', 'VSSZZZ5', 'W1K5J8E', 'W1K2130', 'WBA15BZ', 'W1VVNKT', 'WBAJU81', 'WBY61EF', 'WBATA61', 'WBA21EU', 'YARVKEH', 'JTMZ53F', 'JN1TBAF', 'KNAC381', 'KMHKN81', 'JTJBGMC', 'LDP31B9', 'JTHB21B', 'LVPC528', 'SC6GM1D', 'TMBJJ7N', 'TSMJYBH', 'TMBAR7N', 'SHHFK68', 'TMBAA8N', 'TMBJB9P', 'TMBLD9P', 'TMAH381', 'SJNF16F', 'VR3F35G', 'VR7BAHP', 'VR1F4DG', 'W1NYC7G', 'W1N4M5B', 'W1K2230', 'W1N2539', 'W1N9M1C', 'W1N4N4F', 'W1NFF8K', 'WF01XXT', 'WDC2539', 'WBA31EU', 'WBA85BZ', 'WBA21EF', 'WBA21EV', 'YARKFAF',
            'YARERHN', 'AHTKA3C', 'LRW3E7E', 'JTDKGAG', 'KNACT81', 'JN1TDNF', 'KMHS381', '7JRZSL1', 'KMHHA81', 'JHMRU18', 'JSAAZDA', 'SJNFAAZ', 'TMBER7N', 'TMBCR0N', 'TMBEA6P', 'TMBGP6N', 'TMAK581', 'TMBJJ9P', 'TMBLE7N', 'SB1KA3B', 'TMBJW9P', 'TMAH3H1', 'TMBZZZA', 'TMBCP0N', 'VR7BCZK', 'VR3FPHP', 'U5YH781', 'VR7CGHP', 'VNKKD3D', 'W1N9M0J', 'W1NKM5G', 'W1N4632', 'W0VZT8E', 'W1K6G2D', 'W1NFF3B', 'W1NKM8H', 'W0V0XEP', 'WF0LXXT', 'WBY31AW', 'WDD2906', 'WBA41DT', 'WBA11EG', 'WDD1771', 'WBA61CA', 'WBA21FL', 'WBA41EH', 'WBA11EY', 'ZFACF1C', 'ZN6AW82', 'ZAC5JAC', 'LJNTGUC', 'JTJCJBJ', 'JTDKHAE', 'JN1JGAT', 'JHMFL57', 'KMHP381', 'SADCA2B', 'TMBJH9N', 'SB1MS3J', 'TSMZ93B', 'SALKA9B', 'TMBJM9N', 'NMTBN3J', 'SHHFK78', 'SB1BT76', 'VR3UBYH', 'VR1FCYH', 'VR3F45G', 'VR7EAZK', 'W1N2477', 'W1NGM1C', 'W1N4M1F', 'W1NWC1A', 'W1KLF6D', 'W1N2437', 'WBACV61', 'WBA51EG', 'W1V4478', 'WBS81FK', 'WBA11CH', 'WF0MXXT', 'WBA61EE', 'ZN6AU61', 'ZARPAHD', 'KNAC481', 'KNAB351', 'JTMDW3F', 'KNACB81', 'JTHY65B', 'JTHAAAA', 'JHMGR38', 'KNAAE81', 'KMHB151', 'JMZDR6W', 'KMHHE81', 'KPT60A1', 'TMBLG9P', 'SALZA2B', 'TMBJB9N', 'TMAH081', 'SALCA2B', 'TMBJR0N', 'NMTBE3J', 'SJNFGNJ', 'TMBAH8N', 'SALYA2B', 'VR3KCZK', 'U5YPH81', 'VR7BFZK', 'VF7VZZK', 'VR7BDHP', 'VR7ARHN', 'VF3LPHN', 'W1K1183', 'W1KAF0F', 'W1N2533', 'W1KMJ4H', 'W0LPD5E', 'W0VBD8E', 'W1K6G6B', 'W1KLF5F', 'W1NYC5A', 'W1NKJ5G', 'W1N4N5B', 'W1K2971', 'W1KCG2D', 'W1NKJ0H', 'W1N2436', 'W0VPD5E', 'WBA31EF', 'WDD2130', 'WBS31HJ', 'WF03XXT', 'WBS21ET', 'WBA11DT', 'WBA71AV', 'WBA31EX', 'WBAJU41', 'WBAJD11', 'WBA81BZ', 'YV1UZK5', 'ZARNASC', 'WMW11DJ', 'WVGZZZ1', 'YAREBYH', 'YARVEEH', 'ZFF06VT', 'X96A32R', 'WP1ZZZX', 'ZFACF7C', 'JTMAABA', 'JTMDJRE', 'LRWYGCE', 'LVHRS58', 'AHTBE3C', 'JSAAZCC', 'JMBM5WA', '1C4JJXP', 'JTDACCC', 'LRW3E7F', 'JMZDK6W', 'JTHAABB', 'KNAFD81', 'KPT20A1', 'KNACC81', 'JMZKBAC', 'LB3G43S', '3HGRU17', 'JTMW23F', 'JHMRW28', 'KMHKM81', 'NLAFC16', 'TMB1JCN', 'TMBAG7N', 'SHHFK77', 'TMB1GCN', 'TMBCR8N', 'TMBJG9N', 'TMBAH7N', 'NLHDR51', 'SB1ZS3J', 'NLAFC15', 'TMBCP8N', 'TSMLYEA', 'TMBJJ9N', 'SALEA7B', 'TMBAP8N', 'TMAHC51', 'SJNFAAJ', 'SB1K53B', 'TMBGR6N', 'TMBAL8N', 'SB1BG76', 'TMBJP6N', 'VF3VEEH', 'VF15RSN', 'VF1R870', 'VF37NBH', 'VF72CYH', 'VF3LCYH', 'W1KRJ7J', 'W0VBC6E', 'W1NKJ5F', 'W0VZ4DG', 'W1N4M1D', 'W1NKM5F', 'VXEVZZK', 'VXKUPHP', 'W1NFD3D', 'W1NFB2D', 'W1NGM2C', 'W1KAF0H', 'W1NKM0H', 'W1K6G2B', 'W1N9N0J', 'W1NYC6A', 'W1K3G8E', 'W1N9M0C', 'W1KEG2C', 'VXKFBYH', 'W0VZM6E', 'VXKF3DG', 'W1KEG1C', 'W1K8P9A', 'WBA31AA', 'WBACY61', 'WBA4M91', 'WBA11FK', 'WBATX75', 'WF05XXG', 'WDD2221', 'WBAGT81', 'WBA81DP', 'W1VVLGF', 'WBATC61', 'WDC2533', 'WBA61DP', 'WBA11AW', 'WDC1679', 'WBA31DZ', 'W1V9072', 'WDD2220', 'WBA21EM', 'W1VVNLT', 'WBA41EX', 'WBA31AX', 'WBA71GP', 'WBA81CA', 'YV1LFH7', 'YV1UZL1', 'ZD3TE16', 'WV2ZZZE', 'WUAZZZG', 'YV1UZH5', 'WMW21GC', 'YV1UZK2', 'ZACNJEC', 'ZFA3340', 'WVW2ZZZ', 'YV1ZWBF', 'YV1LF06', 'WV2ZZZ2', 'YV12ZEK', 'KPAXA1E', '1GYS48K', '7SAXCCE', 'KMHP281', 'JSAZDED', 'KNAC581', 'LVYPSA3', 'JMZKEN9', '6FPF2CM', 'LMXF18B', '1C4SDJC', 'L6TE310', 'JTJBJRB', 'L6TE21S', 'HESXA2C', 'LDP95C9', '7SVAAAB', 'JMBXTGK', 'KNAE551', 'LDP29H9', '3HGRU18', 'JTDAF4E', '1C6SRFH', 'JTMRJRE', '1C4RJYE', 'JHMRT58', 'KNARM81', 'SB1KT3J', 'TMBAG9N', 'TMBJJ0N', 'SHHFK67', 'TMBEK6P', 'MMCJJKL', 'TMBAN0N', 'TMAH1H1', 'NLHBU51', 'TMBCT8N', 'TMBGK9N', 'TMBAL0N', 'TMBLK9N', 'TMBLR8N', 'TMBNH7N', 'TMBCJ9N', 'TMBJN9N', 'TMBJA8N', 'TNBCJ8N', 'NLHBR81', 'TMBAJ7N', 'TMBJH7N', 'TMBLR0N', 'NLAFC85', 'TMBCE9N', 'TMBJC7N', 'SALEA8B', 'MMCJLKL', 'SALWA2B', 'SALRA2B', 'SHHFK97', 'VR1URHN', 'VR3F4DG', 'VR7A45G', 'VF3PSCF', 'UU14SD8', 'VR3KBDG', 'VR7AJEH', 'VF3M4DG', 'VF3LBBH', 'VF17RBF', 'VF3CUHN', 'VR3FJEH', 'VR3ECYH', 'USYH481', 'VR7A4DG', 'VF1VE00', 'VF3VZZK', 'UU1HSD3', 'VR7ARHP', 'VF3LCBH', 'VR1UJZK', 'W1NWM0A', 'W1K6X7K', 'W1K6X7G', 'VXKUDYH', 'W1N4N8J', 'W1K6G3D', 'W1KVK8B', 'W1NKJ2D', 'W1K3G8H', 'W1N9N0K', 'W1N4N1D', 'W1NFF5K', 'W1K3F8E', 'W1KEG1B', 'W1K2573', 'W1KAF4D', 'W1K2132', 'W1NFF2D', 'W1NKM0K', 'W0LGM5E', 'W1N4633', 'W00V7H9', 'W1K1771', 'W1KMJ5B', 'W1K1770', 'W1NDM2E', 'W1NFD0G', 'W1KLF5B', 'W1KLF2D', 'W1NFB6E', 'VXKCMZY', 'W0VZJEH', 'W1NWH1A', 'W1KAF8H', 'W1NFB5E', 'W1KAF4H', 'VSKCTND', 'W1N0J5D', 'VR7NCHN', 'W0VBF6E', 'W1K7X6B', 'WBY11HG', 'W1VHK0G', 'WDD2132', 'WBAKS61', 'WBA31DT', 'WBAKS41', 'WBS81GV', 'WBAHT91', 'WBS11ET', 'W1V5K2F', 'WF06XXW', 'WBA25DP', 'WBACX61', 'WBSCY01', 'WBACW21', 'WBS41AY', 'WBACW01', 'WAP41EM', 'WBACR61', 'WBS11EC', 'WBA81GM', 'WBY51CF', 'WF0EXXS', 'WBY31FK', 'WBA7S61', 'WBA25DN', 'WDF4478', 'WBSAE01', 'WBS41AZ', 'WBA55DP', 'WBA11EE', 'WDD2573', 'WAUZZZ8', 'WBA48FU', 'WBS11GB', 'WBA48FF', 'W1VVMLE', 'WBA41EG', 'WBS11DM', 'WF02K8H', 'WBAVJ51', 'WBA31FZ', 'WBA31FL', 'WBY51EJ', 'WBA38DY', 'WMW31DK', 'ZFA3560', 'ZN6PMDA', 'YV1UZM1', 'YV1LFM1', 'ZN6RMDE', 'ZN6PMDD', 'ZD3E7M9', 'WMWYU71', 'ZARPAHP', 'ZARPAHE', 'YV1XKED', 'ZARFAHB', 'WVWZZZ1', 'ZAA5AVA', 'ZFABF5B', '3HGRU87', 'LMAXA14', 'JNTACAB', '5XYRGDL', 'KMHMY81', '1C6JJTF', 'KPT80B1', 'LGWEELA', 'KMHWH81', '6FPP2CM', 'JTDKB3F', '5LMJJ2L', 'JTMHX01', 'JTMAA7B', 'JTHABAB', '1C4PJXF', 'JHMRW27', 'JSAGJB7', 'JHMRW17', 'LGWEEFU', 'JN1JFNT', 'JS1EM12', 'JN1GANR', 'KMHKH81', 'JHMRU17', '5TDL33C', 'JTJCBGA', 'JS1EK12', 'JMZND6E', 'JS1EJ11', 'KPT00A1', '1FATP8R', 'JTJYWRB', 'LFVVB9E', 'JHMGK38', '1C4JJXR', 'KMHP681', 'KNAGW41', 'JTHAAAE', 'JTJAABA', 'JH2RH12', 'JTHKPAA', 'JH2RH11', 'JMZGLF9', 'JH2PC69', 'JFISKEL', 'JTMWRRE', 'JTJHY7A', '6FPFXXM', '1C4HJXE', '5YJSA7E', 'JNTB23H', 'KNADE51', 'LDP29C9', '5TDGZRA', 'KNAGW81', 'JS1EM11', 'JF1GT7L', '3MDDJ6H', 'JTMAB7B', 'JN1TCNS', 'JTNB23N', '3GCUDEE', 'JF1BS9L', '1GYS47K', 'JF1AABA', 'JMZDR1M', 'JCAZCED', 'JN1TAAF', 'JNTABAC', '1C4RJXS', '1C4PJDD', 'FV1HJD4', 'JNZKL0H', 'F1HJD20', 'JF1SJ5L', 'LYVUZK9', 'TMBGP7N', 'SD7VUJB', 'TMBAHSN', 'SCFRMFG', 'SCBDJ33', 'SCBCX13', 'SCBCN13', 'TMBLS9N', 'SCBCF13', 'TMBAH0N', 'SCBBS53', 'SJAHB14', 'SCATK21', 'TMBGH7N', 'SCA664S', 'TMB1JBN', 'SCA21HA', 'SMLYDD1', 'SC6GN3D', 'NMTKY3B', 'SC6GN2D', 'TMBEE6P', 'TMB1HCN', 'SJNFDNJ', 'SC6GM1A', 'TMB1GBN', 'TMSLYEH', 'TMB1BBN', 'SHHFK98', 'TSLMYDD', 'TMBARSN', 'TMBAR0N', 'MMCXTA0', 'MLHRH15', 'SB1ME3J', 'SD7VUJD', 'TMBLH9N', 'TMBGF7N', 'TMBEG6N', 'TMBLG7N', 'TMBJP7N', 'TSMJYBA', 'TMBJF7N', 'TMBAP7N', 'TMBCJ0N', 'SB1ET76', 'SJNFEAJ', 'SB1EG76', 'NMT53BX', 'TMBANSN', 'SJNFDAJ', 'TMBAN9N', 'TMBJK8N', 'TMBCR7N', 'TMBJB7N', 'TMBJR9N', 'TMBAGSN', 'TSMLYD0', 'TMBAU8N', 'TMBGE7N', 'TMBGR9N', 'TMBLU9N', 'SJAA514', 'TMBAK9N', 'SIJNTAA', 'TMBJR6N', 'SHSRE57', 'TMAH1HD', 'TMSLYDD', 'SALCA2D', 'NLAFC18', 'TMBEH6N', 'TSMLYDA', 'TMBCK8N', 'TMBLS8N', 'SADHA2B', 'MMCXNA0', 'SADFA2B', 'SHHFK37', 'MLHJC92', 'LXMA14A', 'VR1UCYH', 'VF1RF80', 'UU15SDL', 'VNKKJ0D', 'U5YOV81', 'VF1RB00', 'UU1DJFF', 'VF3MCBH', 'UU10SDT', 'VF3YEBN', 'VR1JJEH', 'VF70BBH', 'VR3KCKZ', 'UU1HSD1', 'VR7CPZY', 'UU1DFJ0', 'VF3YB2M', 'VF1WK00', '-VF1JL0', 'UU17SDK', 'VF3VFAH', 'VGAF1AD', 'VR1RHN0', 'VR7CBZY', 'VF1RFBO', 'VF3FPHN', 'VF3CUBH', 'VFRHN00', 'VF3CCHN', 'VF1AGVY', 'VF3CCHM', 'VR3FHEH', 'VF3FCYH', 'VF7SZYH', 'VF3EDYH', 'VF7VEEH', 'UU15SDM', 'VF3DDBH', 'UU15SD8', 'VF15RBJ', 'UU10SDX', 'VF12R05', 'USYPU81', 'VF12R03', 'USYH151', 'VF12R01', 'VR3SUSH', 'VE7BCZK', 'VCF1EBE', 'VF1RJ00', 'VBKTU74', 'VF7SXYH', 'UUIDJF0', 'VF72CBH', 'UU1L522', 'VF7YCAN', 'VFIRJA0', 'VFIRHN0', 'VR3FRHP', 'VF3CUHM', 'U5Y4F15', 'W1NFB8F', 'W1N4N1F', 'VSKDAAC', 'W0VPE9E', 'W1KLF0E', 'W1V3H6F', 'W0VZS6E', 'W1NFB4G', 'W1KLF0K', 'VXFVLEH', 'W1K3F4F', 'W1N4M8J', 'VXEVAYH', 'W1N0J1F', 'W1NFD6E', 'W1KZH1H', 'W1NDM2D', 'W0VECYH', 'W1K5J1C', 'W1KZF8H', 'W1N4N8E', 'W0VBF8E', 'W1N9N0C', 'W1K2951', 'W1N9N0B', 'W0VBE6E', 'W1KCG4E', 'W1KZF8A', 'W1KZF6B', 'VXEVEEH', 'W1KZF5K', 'W1KAF0K', 'VRUSHNS', 'W1K7X5K', 'W0VZCBH', 'W0V7DEN', 'W1K5J8G', 'W1KZF0E', 'W1K5J8F', 'W1NKJ0K', 'W1K5J4F', 'W1K2906', 'VXKFRHP', 'W0LPC5E', 'VXKFPHP', 'W0LGT5E', 'VXKFMZK', 'W0LGM8E', 'W1KEG3C', 'W0LGM6E', 'W1K6G6K', 'W1NFB8K', 'W0LBE8E', 'W0VZT6G', 'W0LBD8E', 'W1KCG5F', 'W0L7H9E', 'W1KCG3E', 'W1KVK8A', 'W1N9M1D', 'W0L6VZN', 'W0VZS6G', 'W1K2383', 'W1KAF5F', 'W00V7HS', 'W1N4N8H', 'W1K2324', 'W1NGM3C', 'W00V7D9', 'VYSP01H', 'W1K3G4F', 'W1NKM2D', 'W1KMK6B', 'W1KMJ6B', 'W1K3F5B', 'W1NFD2D', 'W1K6F7G', 'W0V7HSE', 'W1KZF0F', 'W1K7X7K', 'WBA11GR', 'WBAKV21', 'WBS21DM', 'WBA6N51', 'WBA61CM', 'WBS31AZ', 'WF0FXXT', 'W1VVNKE', 'WBA61AT', 'WBATY95', 'WBA5V31', 'WBA7U21', 'WBA5U91', 'WBA7R81', 'WBA5P31', 'WBA11AR', 'WBAFY41', 'WBA7C81', 'WBA51GN', 'WBA71BJ', 'WBA51FZ', 'WBA71AM', 'WDB4632', 'WBATX31', 'WDC2923', 'WBA51DP', 'WBA21DP', 'WBA51CM', 'WBA11FJ', 'WBA51BL', 'WBA7L11', 'WBA51AL', 'WBA11BJ', 'WBAKV61', 'WBA11AL', 'WBA4M51', 'WDD2052', 'WBAJY61', 'W1VVNLS', 'WBACW81', 'W1VVMKS', 'WBA41FU', 'WBAYK71', 'WBY81EH', 'WBAYH51', 'WBY7X41', 'WBAUZ31', 'WBY71GM', 'WBAJV61', 'WDD2462', 'W1V5K6F', 'WBA41BX', 'WBA7V81', 'WBA41AS', 'WBAJC51', 'WBA41AP', 'WBA38FS', 'WBS61AY', 'W1V4477', 'WBS41HK', 'WBA7M91', 'WBA7K31', 'WF01XXE', 'WBA11BZ', 'WF0EXXW', 'WDC1660', 'WBA11AM', 'WBY51GM', 'WBS21EC', 'WBABC21', 'WBA7D21', 'WBA85DP', 'WAUC4AF', 'WBY41HD', 'WBA7C61', 'WBY41FK', 'WBA71HB', 'WBAJJ31', 'WBA71FY', 'WDD2383', 'WBAYN91', 'WBA31AM', 'W1VT1JC', 'WBA31AJ', 'WBA31AE', 'WBAVJ91', 'WBA31AD', 'WBAVJ11', 'WDD2229', 'WBAUJ51', 'WBA25GR', 'WF0DXXS', 'WBA81FJ', 'WBA71AB', 'WBAJH71', 'WBATS11', 'WF0RPCE', 'WBA21EY', 'WDC1569', 'WBA65GP', 'WBSJU01', 'WBAGV41', 'WBSDZ01', 'WBA31GW', 'WBA31GP', 'WBA31GG', 'WMW31DH', 'YV1XZEH', 'YV1LFA3', 'YV1PSA8', 'ZD3E7M4', 'ZARPAHB', 'ZFA5FBA', 'ZARNASD', 'ZPBEC3Z', 'WMW41BT', 'ZFANFBB', 'WMW11GD', 'ZARNASB', 'YV1XKER', 'ZARNASA', 'WVZZZZS', 'YV1PZ68', 'ZARFAHL', 'WF0TK3S', 'YARVSZK', 'WMW31GA', 'ZAREAFG', 'YV1ZW25', 'WVWZZZ7', 'YV1XZK8', 'ZAREAFD', 'ZPBEB3Z', 'ZAPNPC2', 'ZN6TU61', 'WVW2Z2Z', 'WVW22ZZ', 'YARECYH', 'ZAMYR56', 'ZAM56YR', 'ZFAEFAC', 'YV1UZBF', 'ZFACF7G', 'WJGZZZC', 'ZAANAVB', 'WVG2ZZZ', 'WMW51BR', 'WMW31GD', 'YAREZZK', 'WMW31BS', 'WMW21BS', 'YARVEAH', 'WMW11GC', 'ZD3EC16', 'WV2ZZ2K', 'YV1XZK7', 'ZFABF5J', 'YV1XZBB', 'YV1LFBM', 'YV1XZA6', 'WUAZZZ4', 'YV1ZZK5', 'YV1ZZA8', 'ZFACF1B', 'YV1FH7V', 'YV1UZH4', 'WOVEDYH', 'YV1UZBM', 'WMWYY91', 'ZD3EC18', 'WMWXR91', 'WMWXP31', 'WMWXJ11', 'YV1PWA8', 'WMWLV31', 'WMW81GC', 'WMW81BR', 'WF0VXXT', 'WMW71DH', 'WMW51GA'],

"товарен до 12т": ['ZCFC660', 'XLRAEL2', 'ZCFC672', 'ZCFC170', 'WDB9700', 'ZCFC670', 'ZCFA75B', 'TYBFEB7', 'TYBFECX', 'ZCFA675', 'ZCFA80D', 'WMA14DZ']
}



VIN_PREFIX_CATEGORY = {
    prefix: CATEGORIES_BY_SOURCE_BG[vehicle_type]
    for vehicle_type, prefixes in VEHICLE_TYPES_VIN.items()
    for prefix in prefixes
}