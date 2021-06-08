import json
import os

folder = "/Users/matt.admin/sites and projects/1. Online Tariff/ott prototype/app/data/cpc/markdown-cpc"
json_file = "/Users/matt.admin/sites and projects/1. Online Tariff/ott prototype/app/data/cpc/cpc-combos.json"

file_array = ["xxxx-conditions.md",
              "xxxx-description.md", "xxxx-restrictions.md"]
exclusions = ["0100", "0101"]
with open(json_file) as json_file_handle:
    data = json.load(json_file_handle)
    for item in data:
        previous_codes = item["previous_codes"]
        for previous_code in previous_codes:
            code = previous_code["code"]
            if code not in exclusions:
                print(code)
                for file in file_array:
                    filename = file.replace("xxxx", code)
                    filepath = os.path.join(folder, filename)
                    f = open(filepath, "w+")
