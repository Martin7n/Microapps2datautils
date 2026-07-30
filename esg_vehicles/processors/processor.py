from esg_vehicles.data_collections.brand_multilanguage import BRANDS_ENG, MODELS_ENG
from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.brand_model import brand_model
from esg_vehicles.processors.category_check import  category_handler
from esg_vehicles.processors.fuel_check import  check_for_fuel_rev



def process_records(records:list[ESGRecord]):
    count = 0
    data_ex = {}

    for record in records:

        record.detected_weight = category_handler(record)
        record.weight_measure_update = "kg"

        if not record.brand or not record.model:
            description_brand_model = [record.equipment, record.brand, record.model]
            [new_brand, new_model] = brand_model(description_brand_model)
            if new_brand:
                record.detected_brand = new_brand
            if new_model:
                record.detected_model = new_model
        else:
            record.detected_brand = BRANDS_ENG.get(record.brand, record.brand)
            record.detected_model = MODELS_ENG.get(record.model, record.model)

        current_fuel_equipment = [record.fuel_type, record.equipment]
        updated_fuel_cat = check_for_fuel_rev(current_fuel_equipment)
        record.detected_fuel = updated_fuel_cat



if __name__ == '__main__':
    pass