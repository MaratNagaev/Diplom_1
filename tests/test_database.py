import pytest
from Diplom_1.data import DB


class TestDB:
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', DB.database_buns)
    def test_available_buns_db_successfully(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price

    @pytest.mark.parametrize('index_ing, ingredient_type, ingredient_name, ingredient_price',
                             DB.database_ingredients)
    def test_available_ingredients_db_successfully(self, db, index_ing, ingredient_type, ingredient_name, ingredient_price):
        data_ingredients = db.available_ingredients()
        assert (data_ingredients[index_ing].get_name() == ingredient_name and data_ingredients[index_ing].get_type() == ingredient_type and
                data_ingredients[index_ing].get_price() == ingredient_price)



