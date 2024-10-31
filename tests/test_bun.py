from Diplom_1.data import Data1, Data2


class TestBun:
    def test_get_name_bun_successfully(self, mock_bun_1):
        assert mock_bun_1.get_name() == Data1.bun_name

    def test_get_price_bun_successfully(self, mock_bun_2):
        assert mock_bun_2.get_price() == Data2.bun_price
