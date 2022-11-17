from time import sleep
import json
import csv
import os

def create_file(out_path):
    isExist = os.path.exists(out_path)
    if not isExist:
        with open(out_path, 'w', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            fields = ['BillId', 'BillDate', 'StoreId', 'BillTotal']
            csvwriter.writerow(fields)


def read_csv(csv_path):
    d = {}
    with open(csv_path, mode='r') as f:
        csv_data = csv.reader(f)
        d = {rows[0]: rows[3] for rows in csv_data}
        return d

def process_dir(json_path,processed_path,product_price):
    for file in os.listdir(json_path):
       if file.endswith('.json'):
          # Create the filepath of particular file
          file_path =f"{json_path}/{file}"
          processed = f"{processed_path}/{file}"
          bills = read_json(file_path,product_price)
          write_data(out_path, bills)
          os.rename(file_path,processed)

def read_json(file_path,product_price):
    json_infile = open(file_path, "r")
    data = json.load(json_infile)
    #product_price = read_csv(csv_path)
    sum = 0
    for row in data["BillDetails"]:
        if row in product_price.keys():
            cal = float(product_price[row]) * int(data["BillDetails"][row])
            sum += cal
    return [data["BillID"], data["BillDate"], data["StoreID"], sum]

def write_data(out_path,bills):
    with open(out_path, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows([bills])


out_path = 'C:\\Users\\bryni\git\\python-training\\billing\\bills.csv'
json_path = "C:\\Users\\bryni\git\\python-training\\billing\\bills"
csv_path = "C:\\Users\\bryni\\git\\python-training\\billing\\masterdata\\products.csv"
processed_path = "C:\\Users\\bryni\\git\\python-training\\billing\\processed"

create_file(out_path)
product_price = read_csv(csv_path)
while True:
    process_dir(json_path,processed_path,product_price)
    sleep(2)




