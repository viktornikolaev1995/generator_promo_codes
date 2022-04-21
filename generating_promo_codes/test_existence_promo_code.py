import json
import unittest
from unittest import TestCase
from existence_promo_code import check_if_promo_code_is_exists


class TestExistencePromoCode(TestCase):

    def test_existence_promo_code(self):
        with open('promo_codes_test.json', 'r') as jsonfile:
            self.assertEqual(jsonfile.readable(), True)
            data_from_jsonfile = json.load(jsonfile)

        promo_code = list(data_from_jsonfile.items())[0][1]['promo_codes'][0]
        res = check_if_promo_code_is_exists(promo_code=promo_code)
        self.assertEqual('код существует группа' in res, True)

        promo_code = list(data_from_jsonfile.items())[1][1]['promo_codes'][0]
        res = check_if_promo_code_is_exists(promo_code=promo_code)
        self.assertEqual('код существует группа' in res, True)

        promo_code = list(data_from_jsonfile.items())[2][1]['promo_codes'][0]
        res = check_if_promo_code_is_exists(promo_code=promo_code)
        self.assertEqual('код существует группа' in res, True)

    def test_not_existence_promo_code(self):
        promo_code = '5efb1613-de39-4d68-99eb-3f7c5d06ce078'
        res = check_if_promo_code_is_exists(promo_code=promo_code)
        self.assertEqual('код не существует' == res, True)


if __name__ == '__main__':
    unittest.main()