from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    bolinho = Dish("bolinho", 3.30)
    salada = Dish("salada", 4.30)
    assert bolinho.name == "bolinho"
    assert bolinho.__repr__() == "Dish('bolinho', R$3.30)"
    assert bolinho.__hash__() != salada.__hash__()
    assert bolinho.__hash__() == bolinho.__hash__()
    assert bolinho.__eq__(bolinho)
    assert not bolinho.__eq__(salada)

    with pytest.raises(TypeError):
        Dish("bolinho", "3.30")

    with pytest.raises(ValueError):
        Dish("bolinho", 0)

    ingredient = Ingredient("presunto")
    bolinho.add_ingredient_dependency(ingredient, 2)

    assert bolinho.get_ingredients() == {ingredient}
    assert bolinho.get_restrictions() == set(ingredient.restrictions)
