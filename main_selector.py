from esg_backup_v1.excel_parser import xls_parse_sample_test
from esg_vehicles.excel_parser import data_handler


def transform_files(source, destination, type):

    if type == "i":

        data_handler(source,destination)
    else:
        print("Not implemented")
        # xls_parse_sample_test(r"C:\drob\sample.xlsx")




if __name__ == "__main__":
    source = r"C:\drob\sample_fordev.xlsx"
    destination = r"C:\drob\upppadded1.xlsx"
    type = input("Choose a type [i for cl]")
    transform_files(source,destination, type)