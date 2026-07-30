POWERTRAIN_CATEGORIES = {
    # Internal Combustion Engine (ICE)
    "бензин": {
        "powertrain_type": "ICE",
        "energy_source": "PETROL",
    },
    "дизел": {
        "powertrain_type": "ICE",
        "energy_source": "DIESEL",
    },
    "газ": {
        "powertrain_type": "ICE",
        "energy_source": "LPG",
    },
    "бензин/газ": {
        "powertrain_type": "ICE",
        "energy_source": "PETROL_LPG",
    },
    "дизел/биодизел": {
        "powertrain_type": "ICE",
        "energy_source": "DIESEL_BIODIESEL",
    },
    "внг": {
        "powertrain_type": "ICE",
        "energy_source": "CNG",
    },

    # Hybrid Electric Vehicles (HEV)
    "бензин/електричество": {
        "powertrain_type": "HEV",
        "energy_source": "PETROL_ELECTRIC",
    },
    "дизел/електричество": {
        "powertrain_type": "HEV",
        "energy_source": "DIESEL_ELECTRIC",
    },
    "бензин/електричество/внг": {
        "powertrain_type": "HEV",
        "energy_source": "PETROL_ELECTRIC_CNG",
    },

    # Plug-in Hybrid Electric Vehicle
    "PHEV (plug-in) електричество/бензин": {
        "powertrain_type": "PHEV",
        "energy_source": "PETROL_ELECTRIC",
    },

    # Battery Electric Vehicle
    "електродвигател": {
        "powertrain_type": "BEV",
        "energy_source": "ELECTRIC",
    },

    # Future-proof additions
    "водород": {
        "powertrain_type": "FCEV",
        "energy_source": "HYDROGEN",
    },
    "водород/електричество": {
        "powertrain_type": "FCEV",
        "energy_source": "HYDROGEN_ELECTRIC",
    },
}