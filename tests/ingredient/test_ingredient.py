from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("ovo")
    ingredient_2 = Ingredient("farinha")
    ingredient_3 = Ingredient("massa")

    assert ingredient_1.restrictions == set()
    assert ingredient_1.name == "ovo"
    assert repr(ingredient_1) == "Ingredient('ovo')"

    assert hash(ingredient_2) == hash(ingredient_3)
    assert hash(ingredient_2) != hash(ingredient_1)
