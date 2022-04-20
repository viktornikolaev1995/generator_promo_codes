import argparse
import json
import os
from json import JSONDecodeError
from pathlib import Path
import requests

parser = argparse.ArgumentParser(description='Generating promo codes')
parser.add_argument('-a', dest='amount', type=int, required=True)
parser.add_argument('-g', dest='group', type=str or int, required=True)

args = parser.parse_args()

amount_from_command_line = args.amount
group_from_command_line = args.group

path = Path(__file__).resolve().parent


def gen_promo_codes(name, amount):
    data = {
        'name': name,
        'amount': amount
    }
    response = requests.post(url='http://127.0.0.1:8000/api-promo-codes/groups/', data=data)
    # if response.status_code == 400:
    #     return None
    res = json.loads(response.text)
    print(res)
    res_group = res['name']
    res_promo_codes = res['promo_codes']
    return res_group, res_promo_codes


def inserting_data_in_jsonfile(group_name: str = group_from_command_line, amount: str = amount_from_command_line) -> json:
    if 'promo_codes.json' not in os.listdir(path=path):
        with open('promo_codes.json', 'w') as jsonfile:
            res = gen_promo_codes(name=group_name, amount=amount)
            # if res:
            group, promo_codes = res
            promo_codes_data = {
                group: {
                    'promo_codes': promo_codes
                }
            }
            json.dump(promo_codes_data, jsonfile)
            # else:
            #     print('group с таким именем уже существует')
    else:
        with open('promo_codes.json', 'r') as jsonfile:
            try:
                data_from_jsonfile = json.load(jsonfile)
            except JSONDecodeError:
                pass

        with open('promo_codes.json', 'w') as jsonfile:
            res = gen_promo_codes(name=group_from_command_line, amount=amount_from_command_line)
            # if res:
            group, promo_codes = res
            if jsonfile.readable():
                data_from_jsonfile[group] = {'promo_codes': promo_codes}
                json.dump(data_from_jsonfile, jsonfile)
            else:
                promo_codes_data = {
                    group: {
                        'promo_codes': promo_codes
                    }
                }
                json.dump(promo_codes_data, jsonfile)

            # else:
            #     print('group с таким именем уже существует')


if __name__ == "__main__":
    inserting_data_in_jsonfile(group_name=group_from_command_line, amount=amount_from_command_line)