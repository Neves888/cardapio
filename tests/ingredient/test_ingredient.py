from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("ovo")
    ingredient_2 = Ingredient("manteiga")

    assert ingredient_1.restrictions == set()
    assert ingredient_1.name == "ovo"
    assert repr(ingredient_1) == "Ingredient('ovo')"

    assert hash(ingredient_1) == hash(ingredient_1)
    assert hash(ingredient_1) != hash(ingredient_2)
