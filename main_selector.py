from excel_read_write.excel_parser import data_handler


def transform_files(source, destination, type):
    #additional functionalities and variations => later.
    return data_handler(source,destination, type)



if __name__ == "__main__":
    source = r"C:\drob\sample_fordev_s.xlsx"
    destination = r"C:\drob\upppadded1.xlsx"
    source2 = r"C:\drob\testmask.xlsx"
    destination2 = r"C:\drob\resmask.xlsx"
    type = (input("Choose a type ['i' for datamask, 'e' for esg]"))
    print(transform_files(source,destination, "esg_main"))

    # print(transform_files(source2, destination2, type))