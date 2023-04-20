from src.models.ingredient import Ingredient # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("ovo")
    assert ingredient_1.name == "ovo"
    assert ingredient_1.restrictions == set()
    assert ingredient_1.__repr__() == "Ingredient('ovo')"

    ingredient_2 = Ingredient("farinha")
    assert ingredient_2.name == "farinha"
    assert ingredient_2.restrictions == set()
    assert ingredient_2.__repr__() == "Ingredient('farinha')"

    ingredient_3 = Ingredient("massa")
    assert ingredient_2.__hash__() != ingredient_1.__hash__()
    assert ingredient_2.__eq__(ingredient_3) is True
