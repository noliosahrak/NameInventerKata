from assertpy import assert_that

from NameInverter import NameInverter


class TestNameInverter:

    def test_should_raise_exception_when_none_provided(self):
        name_inverter = NameInverter()
        assert_that(name_inverter.invert).raises(ValueError).when_called_with(None)

    def test_should_return_empty_string_when_empty_string_provided(self):
        name_inverter = NameInverter()
        inverted = name_inverter.invert("")
        assert_that(inverted).is_equal_to("")
