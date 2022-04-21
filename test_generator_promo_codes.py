import json
import unittest
from unittest import TestCase
from generator_promo_codes import inserting_data_in_jsonfile


class TestGeneratorPromoCodes(TestCase):

    def test_generator_promo_codes(self):
        file = 'promo_codes_test.json'
        inserting_data_in_jsonfile(file=file, group_name='агенства', amount='10')
        inserting_data_in_jsonfile(file=file, group_name='avtostop', amount='42')
        inserting_data_in_jsonfile(file=file, group_name='1', amount='5')
        inserting_data_in_jsonfile(file=file, group_name='1', amount='1')
        with open(file, 'r') as jsonfile:
            self.assertEqual(jsonfile.readable(), True)
            data_from_jsonfile = json.load(jsonfile)
            self.assertEqual(len(data_from_jsonfile.keys()), 3)
            self.assertEqual(len([promo_code for values in data_from_jsonfile.values() for promo_code in
                                  values['promo_codes']]), 58)


if __name__ == '__main__':
    unittest.main()