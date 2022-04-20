from generator_promo_codes import inserting_data_in_jsonfile


def test_generator_promo_codes():
    inserting_data_in_jsonfile(group_name='агенства', amount=10)


def test_existence_promo_code():
    pass