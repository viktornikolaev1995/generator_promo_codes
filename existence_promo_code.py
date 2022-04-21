import argparse
import json
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Checking existence promo code in jsonfile')
parser.add_argument('-pc', dest='promo_code', type=str, required=False)
args = parser.parse_args()
promo_code_from_command_line = args.promo_code

path = Path(__file__).resolve().parent


def check_if_promo_code_is_exists(file: str = 'promo_codes.json', promo_code: str = promo_code_from_command_line):
    if file in os.listdir(path=path):
        with open(file, 'r') as jsonfile:
            promo_codes_dict = json.load(jsonfile)
            res = None
            for group, promo_codes_data in promo_codes_dict.items():
                if promo_code in promo_codes_data['promo_codes']:  # there are several codes, need to change
                    res = f'код существует группа = {{{group}}}'
            print('код не существует') if not res else print(res)
            return 'код не существует' if not res else res
    else:
        print('jsonfile не существует')
        return 'jsonfile не существует'


if __name__ == "__main__":
    check_if_promo_code_is_exists(promo_code=promo_code_from_command_line)