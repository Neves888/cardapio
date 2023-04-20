from models.ingredient import Ingredient
from src.models.dish import Dish
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = dict()
        dishes = {}
        read_file = pd.read_csv(source_path)
        for dish, price, ingredient, recipe_amount in read_file.itertuples(
                index=False):
            list = Dish(dish, price)
            ingredient = Ingredient(ingredient)
            if list not in dishes:
                dishes[list] = list
            dishes[list].add_ingredient_dependency(
                ingredient,
                recipe_amount
            )
        self.dishes = set(dishe for dishe in dishes)