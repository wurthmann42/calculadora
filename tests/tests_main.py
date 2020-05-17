import pytest
from Calculator.calculator import Calculador

class TestCalculator:

	@pytest.fixture
	def calculator(self):
		return Calculador()

	def test_soma1(self, calculator):
		assert calculator.soma(1) == 1

	def test_soma2(self, calculator):
		assert calculator.soma(1, 2) == 3

	def test_soma3(self, calculator):
		assert calculator.soma(1, 10, 101) == 112

	def test_soma4(self, calculator):
		assert calculator.soma(101, 584, 295, 13462) == 14442

	def test_subtrai1(self, calculator):
		assert calculator.subtrai(1) == 1

	def test_subtrai2(self, calculator):
		assert calculator.subtrai(1, 2) == -1

	def test_subtrai3(self, calculator):
		assert calculator.subtrai(1, 2, 0) == -1

	def test_subtrai4(self, calculator):
		assert calculator.subtrai(65, 14, 15, 22) == 14

	def test_multiplica1(self, calculator):
		assert calculator.multiplica(1) == 1

	def test_multiplica2(self, calculator):
		assert calculator.multiplica(1, 2) == 2

	def test_multiplica3(self, calculator):
		assert calculator.multiplica(-1, 2, 3) == -6

	def test_multiplica4(self, calculator):
		assert calculator.multiplica(0, 1, 4, 20) == 0

	def test_divide1(self, calculator):
		assert calculator.divide(1) == 1

	def test_divide2(self, calculator):
		assert calculator.divide(2, 0) == 'Not a number'

	def test_divide3(self, calculator):
		assert calculator.divide(6, 4, 2) == 0.75

	def test_divide4(self, calculator):
		assert calculator.divide(6, 10, 0, 1) == 'Not a number'