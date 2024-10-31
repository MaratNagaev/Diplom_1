from Diplom_1.practicum.burger import Burger
from Diplom_1.data import Data1, Data2
import pytest


class TestBurger:
    def test_set_buns_successfully(self, mock_bun_1):
        burger = Burger()
        burger.set_buns(mock_bun_1)
        assert burger.bun == mock_bun_1

    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [Data1.sauce_name, Data1.sauce_name],
        [Data1.filling_name, Data1.filling_name],
        [Data2.filling_name, Data2.filling_name]
    ]
                             )
    def test_add_ingredient_successfully(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [Data1.sauce_name, Data1.sauce_name],
        [Data2.filling_name, Data2.filling_name]
    ]
                             )
    def test_remove_ingredient_successfully(self, ingredients, removed_ingredient, mock_filling_1):
        burger = Burger()
        burger.add_ingredient(mock_filling_1)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling_1 in burger.ingredients

    def test_move_ingredient_successfully(self, mock_sauce_1, mock_filling_1):
        burger = Burger()
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling_1 and burger.ingredients[1] == mock_sauce_1

    def test_get_price_burger_successfully(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == Data2.burger_final_cost

    def test_get_receipt_successfully(self, mock_bun_1, mock_sauce_1, mock_filling_1, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_1)
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус Spicy-X =\n'
                                        '= filling Говяжий метеорит (отбивная) =\n'
                                        '= filling Филе Люминесцентного тетраодонтимформа =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')
