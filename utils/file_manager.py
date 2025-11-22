import json
import os

file_name = "data/data.json"

def import_previous_data():
    if not os.path.exists(file_name):
        data = {
            "accounts": [],
            "categories": [],
            "transactions": []
        }
        return data
    try:
        with open(file_name, 'r', encoding = "utf-8") as f:
            return json.load(f)
    except:
        print("File is Empty or Corrupted..\n")
        data = {
            "accounts": [],
            "categories": [],
            "transactions": []
        }
        return data
        

def save_data_to_file(data):
    try:
        with open(file_name, 'w', encoding= "utf-8") as f:
            json.dump(data, f, indent= 4)
    
    except:
        with open(file_name, 'a', encoding= "utf-8") as f:
            json.dump(data, f, indent= 4)