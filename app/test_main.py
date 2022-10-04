from app.main import get_human_age


def test_should_return_proper_age_if_animal_years_are_more_than_14():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_proper_age_if_animal_years_are_more_than_23():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_proper_age_if_cat_age_28_dog_age_29():
    assert get_human_age(28, 29) == [3, 3]
