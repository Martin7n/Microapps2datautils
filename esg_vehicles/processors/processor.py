from esg_vehicles.data_collections.brand_multilanguage import BRANDS_ENG, MODELS_ENG
from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.brand_model_processor import brand_model
from esg_vehicles.processors.category_processor import category_extraction, known_category
from esg_vehicles.processors.data_helpers import text_normalization
from esg_vehicles.processors.fuel_check import  check_for_fuel_rev
from esg_vehicles.processors.weight_processor import weight_normalization


def process_records(records:list[ESGRecord]):
    count = 0
    data_ex = {}

    for record in records:
    #vin:
        if record.vin != "-" and record.vin is not None:
            record.detected_vin = text_normalization(record.vin).upper()

    #weight:
        record.detected_weight= weight_normalization(record.weight,record.weight_measure)
        record.weight_measure_update = "kg"

    #brands and models: not terrible, not great...enough for the skeleton.
        if not record.brand or not record.model:
            description_brand_model = [record.equipment, record.brand, record.model]
            description_brand_model = [text_normalization(x) for x in description_brand_model]
            [new_brand, new_model] = brand_model(description_brand_model)
            if new_brand:
                record.detected_brand = new_brand
            if new_model:
                record.detected_model = new_model
        else:
            record.detected_brand = BRANDS_ENG.get(record.brand, record.brand)
            record.detected_model = MODELS_ENG.get(record.model, record.model)
    #categories
        if record.equipment_type is not None and record.equipment_type != "-":

            record.detected_category = known_category(record.equipment_type)
        else:
            eq_description = text_normalization(record.equipment)
            eq_brand = text_normalization(record.detected_brand)
            eq_model = text_normalization(record.detected_model)
            eq_vin = text_normalization(record.vin)

            record.detected_category = category_extraction(eq_description, eq_brand, eq_model, eq_vin)

            # if record.detected_category!="-":
        #     record.reg_category = VEHICLE_CATEGORY_MAPPING[record.asset_type.lower()]

        current_fuel_equipment = [record.fuel_type, record.equipment]
        updated_fuel_cat = check_for_fuel_rev(current_fuel_equipment)
        record.detected_fuel = updated_fuel_cat

        count += 1
        print(f"Record Number {count} - \033[92m {record.equipment_allocation_id} \033[0m processed")




if __name__ == '__main__':
    pass