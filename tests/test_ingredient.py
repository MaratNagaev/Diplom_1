from Diplom_1.data import Data1, Data2


class TestIngredient:
    def test_get_name_sauce_successfully(self, mock_sauce_1):
        assert mock_sauce_1.get_name() == Data1.sauce_name

    def test_get_name_filling_successfully(self, mock_filling_1):
        assert mock_filling_1.get_name() == Data1.filling_name

    def test_get_price_sauce_successfully(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == Data2.sauce_price

    def test_get_price_filling_successfully(self, mock_filling_2):
        assert mock_filling_2.get_price() == Data2.filling_price

    def test_get_type_sauce_successfully(self, mock_sauce_1):
        assert mock_sauce_1.get_type() == Data1.sauce_type

    def test_get_type_filling_successfully(self, mock_filling_1):
        assert mock_filling_1.get_type() == Data1.filling_type
