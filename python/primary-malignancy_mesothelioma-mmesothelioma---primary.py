# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"BBP5.00","system":"readv2"},{"code":"BBP3.11","system":"readv2"},{"code":"BBP7.00","system":"readv2"},{"code":"BBP1.00","system":"readv2"},{"code":"104720.0","system":"readv2"},{"code":"47734.0","system":"readv2"},{"code":"86820.0","system":"readv2"},{"code":"27509.0","system":"readv2"},{"code":"C45","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_mesothelioma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_mesothelioma-mmesothelioma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_mesothelioma-mmesothelioma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_mesothelioma-mmesothelioma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
