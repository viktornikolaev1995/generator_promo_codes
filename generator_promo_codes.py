import argparse
import json
import os
from json import JSONDecodeError
from pathlib import Path
import requests

parser = argparse.ArgumentParser(description='Generating promo codes')
parser.add_argument('-a', dest='amount', type=int, required=False)
parser.add_argument('-g', dest='group', type=str or int, required=False)

args = parser.parse_args()

amount_from_command_line = args.amount
group_from_command_line = args.group

path = Path(__file__).resolve().parent


def gen_promo_codes(name, amount, partial_update: bool = False):
    data = {
        'name': name,
        'amount': amount
    }
    if not partial_update:
        response = requests.post(url='http://127.0.0.1:8000/api-promo-codes/create-retrieve-groups/', data=data)
    else:
        response = requests.post(url='http://127.0.0.1:8000/api-promo-codes/partial-update-groups/', data=data)
    res = json.loads(response.text)
    res_group = res['name']
    res_promo_codes = res['promo_codes']
    return res_group, res_promo_codes


def inserting_data_in_jsonfile(file: str = 'promo_codes.json', group_name: str = group_from_command_line,
                               amount: str = amount_from_command_line):
    if file not in os.listdir(path=path):
        with open(file, 'w') as jsonfile:
            res = gen_promo_codes(name=group_name, amount=amount)
            group, promo_codes = res
            promo_codes_data = {
                group: {
                    'promo_codes': promo_codes
                }
            }
            json.dump(promo_codes_data, jsonfile, ensure_ascii=False)
        print(promo_codes_data)
    else:
        data_from_jsonfile = None
        with open(file, 'r') as jsonfile:
            try:
                data_from_jsonfile = json.load(jsonfile)
                print(data_from_jsonfile)
            except JSONDecodeError:
                pass

        with open(file, 'w') as jsonfile:
            if group_name in data_from_jsonfile.keys():
                res = gen_promo_codes(name=group_name, amount=amount, partial_update=True)
                group, promo_codes = res
                data_from_jsonfile[group]['promo_codes'] = promo_codes
            else:
                res = gen_promo_codes(name=group_name, amount=amount)
                group, promo_codes = res
                data_from_jsonfile[group] = {'promo_codes': promo_codes}
            json.dump(data_from_jsonfile, jsonfile, ensure_ascii=False)
        print(data_from_jsonfile)


if __name__ == "__main__":
    inserting_data_in_jsonfile(group_name=group_from_command_line, amount=amount_from_command_line)