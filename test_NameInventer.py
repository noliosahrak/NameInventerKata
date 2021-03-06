import pytest
from assertpy import assert_that

from NameInverter import NameInverter


class TestNameInverter:

    @pytest.fixture
    def inverter(self):
        self.name_inverter = NameInverter()

    def test_should_raise_exception_when_none_provided(self, inverter):
        assert_that(self.name_inverter.invert).raises(ValueError).when_called_with(None)

    def test_should_return_empty_string_when_empty_string_provided(self, inverter):
        inverted = self.name_inverter.invert("")
        assert_that(inverted).is_equal_to("")

    def test_should_return_empty_string_when_spaces_is_given(self, inverter):
        inverted = self.name_inverter.invert("      ")
        assert_that(inverted).is_equal_to("")

    def test_should_return_inverted_first_and_last_name(self, inverter):
        inverted = self.name_inverter.invert("Jan Kowalski")
        assert_that(inverted).is_equal_to("Kowalski, Jan")

    def test_should_return_inverted_first_and_last_name_without_honorific(self, inverter):
        inverted = self.name_inverter.invert("Pan Jan Kowalski")
        assert_that(inverted).is_equal_to("Kowalski, Jan")

    def test_should_return_inverted_first_and_last_name_without_many_honorific(self, inverter):
        inverted = self.name_inverter.invert("prof dr hab inż Janina Kowalska")
        assert_that(inverted).is_equal_to("Kowalska, Janina")
