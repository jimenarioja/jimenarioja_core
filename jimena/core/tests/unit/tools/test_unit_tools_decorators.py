from unittest import TestCase

from jimena.core.components.data.extractor.core import DataExtractorCore
from jimena.core.components.tools.decorators import ToolsDecorators


@ToolsDecorators().timing
def func_sum(number1: int, number2: int) -> int:
    return number1 + number2


@ToolsDecorators().validator(strict=False)
def func_subtract(number1: int, number2: int) -> int:
    return number1 - number2


@ToolsDecorators().ignore_raise
def func_divide(number1: float, number2: float) -> float:
    try:
        return number1 / number2
    except ZeroDivisionError as e:
        raise e


@ToolsDecorators().extension
def func_print_extension(path: str, extension: str) -> str:
    return path + " has a " + extension + " extension"


class TestUnitToolsDecorators(TestCase):
    """
    Unit tests for the 'Decorators' class.

    This test class is designed to validate the functionality of the 'Decorators' class.
    It contains individual test methods, each focusing on different aspects of the class's behavior.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self) -> None:
        """
        Set up method called before each test case execution.
        """
        super().setUp()
        self.number1 = 10
        self.number2 = 5
        self.path_json = "json_file.json"
        self.path_csv = "csv_file.csv"
        self.path_generic = "generic_file.txt"
        self.invalid_path = "dataset.dat"

    def test_unit_tools_decorators_get_size_sum_valid_number_1_and_valid_number_2(self):
        result = func_sum(number1=self.number1, number2=self.number2)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_unit_tools_decorators_ignore_raise_divide_valid_number_1_and_valid_number_2(
        self,
    ):
        result = func_divide(number1=self.number1, number2=self.number2)
        expected_result = 2
        self.assertIsInstance(result, float)
        self.assertEqual(expected_result, result)

    def test_unit_tools_decorators_ignore_raise_valid_number_1_and_invalid_number_2(
        self,
    ):
        result = func_divide(number1=self.number1, number2=0)
        expected_result = "division by zero"
        self.assertIsInstance(result, str)
        self.assertEqual(expected_result, result)

    def test_unit_tools_decorators_timing_sum_valid_number_1_and_valid_number_2(self):
        result = func_sum(number1=self.number1, number2=self.number2)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

    def test_unit_tools_decorators_validator_subtract_valid_number_1_and_valid_number_2(
        self,
    ):
        result = func_subtract(
            number1=self.number1, number2=self.number2, number3="hola"
        )
        self.assertIsInstance(result, int)
        self.assertEqual(5, result)

    def test_unit_tools_decorators_extension_valid_path_and_valid_extension(self):
        result = func_print_extension(path=self.path_json, extension=".json")
        expected_result = self.path_json + " has a .json extension"
        self.assertIsInstance(result, str)
        self.assertEqual(expected_result, result)

    def test_unit_tools_decorators_extension_valid_path_and_invalid_extension(self):
        with self.assertRaises(Exception):
            DataExtractorCore().generic_extractor(self.invalid_path)
