from esg_vehicles.data_collections.brand_multilanguage import BRANDS_ENG, MODELS_ENG
from esg_vehicles.data_collections.categories_vehicles import VEHICLE_CATEGORY_MAPPING
from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.brand_model_processor import extract_brand, brand_model
from esg_vehicles.processors.category_processor import classify_by_weight
from esg_vehicles.processors.data_helpers import text_normalization
from esg_vehicles.processors.fuel_check import  check_for_fuel_rev
from esg_vehicles.processors.weight_processor import weight_normalization


def process_records(records:list[ESGRecord]):
    count = 0
    data_ex = {}

    for record in records:
    #nasty one...
        field_list = [
                    record.equipment,
                    record.brand,
                    record.model,
                    record.fuel_type,
                    record.emissions,
                    record.seats,
                    record.equipment_type,
                    record.vin,
                    record.registration,
                    record.weight,
                    record.weight_measure,
        ]

        [
            equipment,
            brand,
            model,
            type_fuel,
            emisions,
            eq_seats,
            eq_type,
            eq_vin,
            eq_reg,
            weight,
            weight_measure
         ] = [text_normalization(x) for x in field_list]

    #weight:
        record.detected_weight= weight_normalization(weight,weight_measure)
        record.weight_measure_update = "kg"

    #brands and models
        if not brand or not model:
            description_brand_model = [equipment, brand, model]
            [new_brand, new_model] = brand_model(description_brand_model)
            if new_brand:
                record.detected_brand = new_brand
            if new_model:
                record.detected_model = new_model
        else:
            record.detected_brand = BRANDS_ENG.get(record.brand, record.brand)
            record.detected_model = MODELS_ENG.get(record.model, record.model)
    #categories

        if record.detected_weight:
            record.detected_category = classify_by_weight(record.detected_weight)
        # if record.detected_category!="-":
        #     record.reg_category = VEHICLE_CATEGORY_MAPPING[record.asset_type.lower()]



        current_fuel_equipment = [record.fuel_type, record.equipment]
        updated_fuel_cat = check_for_fuel_rev(current_fuel_equipment)
        record.detected_fuel = updated_fuel_cat



if __name__ == '__main__':
    pass