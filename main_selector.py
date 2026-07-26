from excel_read_write.excel_parser import data_handler

def transform_files(source, destination, type):

    if type == "i":

        data_handler(source,destination)
    else:
        print("Not implemented")
        # xls_parse_sample_test(r"C:\drob\sample.xlsx")


if __name__ == "__main__":
    source = r"C:\drob\sample_fordev.xlsx"
    destination = r"C:\drob\upppadded1.xlsx"
    source2 = r"C:\drob\testmask.xlsx"
    destination2 = r"C:\drob\resmask.xlsx"
    type = input("Choose a type [i for cl, data for data]")
    # transform_files(source,destination, type)

    transform_files(source2, destination2, "i")