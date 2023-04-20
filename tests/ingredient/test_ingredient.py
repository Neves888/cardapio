from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("presunto")
    assert ingredient.name == "presunto"
    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
     }
    assert ingredient.__repr__() == "Ingredient('presunto')"
    assert ingredient.__hash__() == hash("presunto")
    assert ingredient.__eq__(ingredient)