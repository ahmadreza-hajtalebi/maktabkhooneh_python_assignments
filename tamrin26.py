import csv
with open (r"assignment26.products.csv", newline = '' ) as my_csv:
    csv_reader = csv.DictReader(my_csv)
    csv_list = []
    for row in csv_reader:
        row ['Total_Price'] = int(row['Price']) * int(row['Quantity'])
        csv_list.append(row)
    outcsv_header = ["Product Name" , "Price" , "Quantity" , "Total_Price"]
    with open('assignment26.products.new.csv' , 'w', newline='') as new_csv:
        csv_writer = csv.DictWriter(new_csv, fieldnames = outcsv_header)
        csv_writer.writeheader()
        csv_writer.writerows(csv_list)
