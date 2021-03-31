from assertpy import assert_that

from NameInverter import NameInverter


class TestNameInverter:

    def test_should_raise_exception_when_null_provided(self):
        name_inverter = NameInverter()
        assert_that(name_inverter.invert).raises(ValueError).when_called_with("")
