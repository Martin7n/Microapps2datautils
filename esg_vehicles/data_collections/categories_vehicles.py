
VEHICLE_WEIGHT_CLASSES = {
    "motorcycle": (50, 500),
    "car": (800, 2500),
    "large_car_suv": (1500, 3500),
    "lcv": (1800, 4500),          # vans, pickups, light commercial
    "medium_duty": (3500, 12000), # trucks, box trucks, small rigids
    "heavy_duty": (12000, 40000),  # heavy trucks, articulated tractors
    "extra_heavy": (40000, 90000)  # special trucks, dumpers, etc.
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