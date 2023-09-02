import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 1) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 3) == 7

    def test_division_success(self):
        assert self.calc.division(self, 20, 10) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 2, 0)

    def teardown(self):
        print("Выполнение метода Teardown")

