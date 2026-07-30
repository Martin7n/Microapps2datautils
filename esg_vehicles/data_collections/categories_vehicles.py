
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
"Motorcycle",
"Car",
"LgtComrclVeh",
"Trailer",
"MedDutyTruck",
"HvyDutyTruck",
"Other"
    }


CATEGORIES_BY_SOURCE_BG = {
    # M1 - passenger cars
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
    "Специализирани строителни машини": "SPV",
    "Багер": "SPV",
    "Колесен багер": "SPV",
    "Мини багер": "SPV",
    "Компактен багер": "SPV",
    "Верижен багер": "SPV",
    "Комбиниран багер-товарач": "SPV",
    "Багер товарач": "SPV",
    "САМОХОДНА МАШИНА - БАГЕР": "SPV",
    "Колесен товарач": "SPV",
    "Челен товарач": "SPV",
    "Колесен челен товарач": "SPV",
    "Верижен товарач": "SPV",
    "МИНИ ЧЕЛЕН ТОВАРАЧ": "SPV",
    "Дъмпер": "SPV",
    "Автокран": "SPV",
    "Бетон помпа": "SPV",
    "БЕТОН-ПОМПА": "SPV",
    "БЕТОНОБЪРКАЧКА": "SPV",
    "Асфалтополагаща машина": "SPV",
    "Верижен асфалтополагач": "SPV",
    "Колесен асфалторазстилач": "SPV",
    "Грейдер": "SPV",
    "Пътна фреза": "SPV",
    "Компактор": "SPV",
    "Стабилизатор/рециклер": "SPV",
    "Сонда": "SPV",
    "Сондажна машина": "SPV",

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
    'плавателно', 'балопреса', 'бордови', 'асфалторазстилач',
    'доматокомбайн', 'сламопреса', 'самоходна', 'фуражосмесител',
    'хеликоптер', 'товарно', 'самолет', 'пръскачка', 'машини',
    'пробивна', 'гроздокомбайн', 'система', 'спредер', 'грейдер',
    'трактори', 'шредер', 'фуражно-разд.', 'тракторно', 'сеялка',
    'стабилизатор/рециклер', 'асфалтополагач', 'трактор', 'тороразпръсквач',
     'багер', 'транспортна', 'пролетница', 'фреза', 'царевица', 'хидравлична',
    'силажокомбайн', 'вентилаторна', 'самоходно', 'адаптер', 'манипулатор',
    'земеделска', 'челен', 'телескопичен', 'компактор', 'комбиниран',
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
    "падащ борд",
    "щора",
    "брезент",
    "мега",
    "контейнеровоз",
    "контейнерно шаси",
    "контейнерно ремарке",
    "шаси",
    "хладилно ремарке",
    "хладилен",
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
    "custom",
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