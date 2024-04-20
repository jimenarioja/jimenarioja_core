from types import NoneType
from unittest import TestCase

from jimena.core.components.data.structure.core import DataStructureCore


class TestUnitDataStructure(TestCase):
    """
    Unit tests for the 'DataStructure' class.

    This test class is designed to validate the functionality of the 'DataStructure' class.
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
        self.data = [
            1,
            2,
            100,
            0.9,
            3,
            True,
            4.5,
            30,
            "data1",
            False,
            "data2",
            None,
            Exception("error1"),
            [2, {}],
            {1: 10},
        ]
        self.invalid_data = 23
        self.invalid_data_type = "aaa"
        self.invalid_lower_limit = "j"
        self.invalid_upper_limit = "m"
        self.dictionary = {
            2: 23,
            3: 4,
            5: "a",
            "b": 7,
            True: False,
            3.5: 1.8,
            "hola": "adios",
            Exception: Exception,
            (1, 3): 6,
        }

    def tearDown(self) -> None:
        """
        Set up method called after each test case execution.
        """
        pass

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_none(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (NoneType).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('NoneType') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [None]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=NoneType
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=NoneType
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_str(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (str).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('str') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = ["data1", "data2"]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=str
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_str(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=str
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_str(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_int(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (int).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('int') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [1, 2, 100, 3, 30]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=int
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_int(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=int
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_int(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_float(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (float).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('float') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [0.9, 4.5]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=float
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_float(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=float
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_float(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_bool(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (bool).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('bool') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [True, False]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=bool
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_bool(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=bool
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_bool(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_list(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (list).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('list') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [[2, {}]]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=list
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_list(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=list
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_list(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_dict(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (dict).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('dict') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [{1: 10}]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=dict
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_dict(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=dict
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_dict(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_valid_type_data_exception(
        self,
    ):
        """
        Test case for the 'filter_by_data_type' function with valid data and a valid data type (Exception).

        This test aims to verify the correct functionality of the 'filter_by_data_type' function when filtering
        data of the specified type ('Exception') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a list, ensuring the function returns a list.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = [Exception("error1")]
        result = DataStructureCore().filter_list_by_data_type(
            data=self.data, type_data=Exception
        )
        self.assertIsInstance(result, list)
        self.assertEqual(str(expected_result), str(result))

    def test_unit_data_structure_filter_list_by_data_type_with_invalid_data_and_valid_type_data_exception(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with invalid data
        (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.invalid_data, type_data=Exception
            )

    def test_unit_data_structure_filter_list_by_data_type_with_valid_data_and_invalid_type_data_exception(
        self,
    ):
        """
        This test block verifies the behavior of the filter_by_data_type function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_by_data_type(
                data=self.data, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_int_lower_limit_and_valid_int_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid integer lower and upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        integer range [1, 4]. The expected result is a list containing integers 1, 2, and 3.

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [1, 2, 3]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=1, upper_limit=4
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_int_lower_limit_and_valid_int_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid integer lower and upper limits) to ensure the function appropriately handles cases of invalid
        input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=1, upper_limit=4
            )

    def test_unit_data_structure_filter_list_data_by_range_invalid_lower_limit_and_valid_int_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with valid data
        and an invalid lower limit (along with a valid integer upper limit) to ensure the function appropriately handles
        cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.data, lower_limit=self.invalid_lower_limit, upper_limit=4
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_int_lower_limit_and_invalid_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with valid data
        and an invalid upper limit (along with a valid integer lower limit) to ensure the function appropriately handles
        cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.data, lower_limit=1, upper_limit=self.invalid_upper_limit
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_float_lower_limit_and_valid_float_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid float lower and upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        float range [3.6, 6.7). The expected result is a list containing float 4.5.

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [4.5]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=3.6, upper_limit=6.7
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_float_lower_limit_and_float_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid float lower and upper limits) to ensure the function appropriately handles cases of invalid
        input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=3.6, upper_limit=6.7
            )

    def test_unit_data_structure_filter_list_data_by_range_invalid_lower_limit_and_valid_float_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with valid data
        and an invalid lower limit (along with a valid float upper limit) to ensure the function appropriately handles
        cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.data, lower_limit=self.invalid_lower_limit, upper_limit=6.7
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_float_lower_limit_and_invalid_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with valid data
        and an invalid upper limit (along with a valid float lower limit) to ensure the function appropriately handles
        cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.data, lower_limit=3.6, upper_limit=self.invalid_upper_limit
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_int_lower_limit_and_valid_float_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid integer lower and float upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        float range [0, 1.5]. The expected result is a list containing 1 and 0.9.

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [0.9, 1]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=0, upper_limit=1.5
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_lower_limit_and_valid_float_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid integer lower and float upper limits) to ensure the function appropriately handles cases of
        invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=0, upper_limit=1.5
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_float_lower_limit_and_valid_int_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid float lower and integer upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        float range [2.7, 6). The expected result is a list containing integers 3 and 4.5.

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [3, 4.5]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=2.7, upper_limit=6
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_float_lower_limit_and_int_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid float lower and integer upper limits) to ensure the function appropriately handles cases of
        invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=2.7, upper_limit=6
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_none_lower_limit_and_valid_int_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid None lower and integer upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        float range [- infinity, 4]. The expected result is a list containing 1, 2, 0.9 and 3.

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [0.9, 1, 2, 3]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=None, upper_limit=4
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_none_lower_limit_and_int_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid None lower and integer upper limits) to ensure the function appropriately handles cases of
        invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=None, upper_limit=6
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_data_none_lower_limit_and_invalid_int_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with valid data
        and an invalid integer upper limit (along with a valid None lower limit) to ensure the function appropriately
        handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.data, lower_limit=None, upper_limit=self.invalid_upper_limit
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_int_lower_limit_and_valid_none_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid integer lower and None upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        float range [4, infinity]. The expected result is a list containing 4.5 and 30

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [4.5, 30, 100]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=4, upper_limit=None
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_int_lower_limit_and_none_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid integer lower and None upper limits) to ensure the function appropriately handles cases of
        invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=4, upper_limit=None
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_data_invalid_lower_limit_and_invalid_none_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with valid data
        but an invalid lower limit and an invalid None upper limit to ensure the function appropriately handles cases
        of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.data, lower_limit=self.invalid_lower_limit, upper_limit=None
            )

    def test_unit_data_structure_filter_list_data_by_range_valid_none_lower_limit_and_valid_none_upper_limit(
        self,
    ):
        """
        Unit test for the 'filter_data_by_range' function with valid None lower and upper limits.

        This test checks if the 'filter_data_by_range' function correctly filters data within the specified
        range. The expected result is a list containing the full list

        Assertions:
        - Checks if the result is an instance of a list.
        - Compares the result with the expected result to verify accurate data filtering.
        """
        expected_result = [0.9, 1, 2, 3, 4.5, 30, 100]
        result = DataStructureCore().filter_list_data_by_data_range(
            data=self.data, lower_limit=None, upper_limit=None
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_list_data_by_range_invalid_data_valid_none_lower_limit_and_none_upper_limit(
        self,
    ):
        """
        This test block verifies the behavior of the filter_data_by_range function when provided with invalid data
        (along with valid None lower and None upper limits) to ensure the function appropriately handles cases of
        invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_list_data_by_data_range(
                data=self.invalid_data, lower_limit=None, upper_limit=None
            )

    def test_unit_data_structure_filter_dict_valid_data_none_key_type_none_key_value_none_item_type_none_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and all parameters set to None.

        This test verifies the behavior of the 'filter_dict' function when all parameters, including key_type,
        key_value, item_type, and item_value, are set to None. The expected result is the same dictionary as the input
        data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function returns the original dictionary when
          all parameters are None.
        """
        expected_result = self.dictionary
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=NoneType,
            key_value=None,
            item_type=NoneType,
            item_value=None,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_int_key_type_none_key_value_none_item_type_none_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and key_type set to int.

        This test verifies the behavior of the 'filter_dict' function when key_type is set to int and all other
        parameters, including key_value, item_type, and item_value, are set to None. The expected result is a dictionary
        containing only the key-value pairs with integer keys from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified key type.
        """
        expected_result = {2: 23, 3: 4, 5: "a"}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=int,
            key_value=None,
            item_type=NoneType,
            item_value=None,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_int_key_type_2_key_value_none_item_type_none_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and key_type set to int and key_value set to 2.

        This test verifies the behavior of the 'filter_dict' function when key_type is set to int and key_value is set
        to 2, while all other parameters, including item_type and item_value, are set to None. The expected result is a
        dictionary containing only the key-value pair with a key of 2 from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified key type and key value.
        """
        expected_result = {2: 23}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=int,
            key_value=2,
            item_type=NoneType,
            item_value=None,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_int_key_type_none_key_value_int_item_type_none_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and key_type set to int and item_type set to int.

        This test verifies the behavior of the 'filter_dict' function when key_type is set to int and item_type is set
        to int, while all other parameters, including key_value and item_value, are set to None. The expected result is
        a dictionary containing only the key-value pairs with integer keys and integer values from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified key and item types.
        """
        expected_result = {2: 23, 3: 4}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=int,
            key_value=None,
            item_type=int,
            item_value=None,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_none_key_type_none_key_value_int_item_type_none_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and item_type set to int.

        This test verifies the behavior of the 'filter_dict' function when key_type is set to None and item_type is set
        to int, while all other parameters, including key_value and item_value, are set to None. The expected result is
        a dictionary containing only the key-value pairs with integer values from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified item type.
        """
        expected_result = {2: 23, 3: 4, "b": 7, (1, 3): 6}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=NoneType,
            key_value=None,
            item_type=int,
            item_value=None,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_none_key_type_none_key_value_int_item_type_23_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and item_type set to int and item_value set to 23.

        This test verifies the behavior of the 'filter_dict' function when key_type and key_value are set to None,
        item_type is set to int, and item_value is set to 23. The expected result is a dictionary containing only the
        key-value pairs with integer values equal to 23 from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified item type and item value.
        """
        expected_result = {2: 23}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=NoneType,
            key_value=None,
            item_type=int,
            item_value=23,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_int_key_type_2_key_value_int_item_type_none_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and key_type set to int, key_value set to 2, and
        item_type set to int.

        This test verifies the behavior of the 'filter_dict' function when key_type is set to int, key_value is set to
        2, and item_type is set to int, while item_value is set to None. The expected result is a dictionary containing
        only the key-value pair with a key of 2 and an integer value from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified key and item types, as well as key and item values.
        """
        expected_result = {2: 23}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=int,
            key_value=2,
            item_type=int,
            item_value=None,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_valid_data_int_key_type_2_key_value_int_item_type_23_item_value(
        self,
    ):
        """
        Test case for the 'filter_dict' function with valid data and key_type set to int, key_value set to 2, item_type
        set to int, and item_value set to 23.

        This test verifies the behavior of the 'filter_dict' function when key_type is set to int, key_value is set to
        2, item_type is set to int, and item_value is set to 23. The expected result is a dictionary containing only the
        key-value pair with a key of 2 and a value of 23 from the input data.

        Assertions:
        - Checks if the result is an instance of a dictionary, ensuring the function returns a dictionary.
        - Compares the result with the expected result to confirm that the function filters the dictionary correctly
          based on the specified key and item types, as well as key and item values.
        """
        expected_result = {2: 23}
        result = DataStructureCore().filter_dict_by_key_and_value_type_and_value(
            data=self.dictionary,
            key_type=int,
            key_value=2,
            item_type=int,
            item_value=23,
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_invalid_data_none_key_type_none_key_value_none_item_type_none_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data
        and all parameters set to None.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data
          and all parameters set to None.
        """
        with self.assertLogs(level="WARNING"):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=NoneType,
                key_value=None,
                item_type=NoneType,
                item_value=None,
            )

    def test_unit_data_structure_filter_dict_invalid_data_int_key_type_none_key_value_none_item_type_none_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data
        and key_type set to int while all other parameters are set to None.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to int, and all other parameters set to None.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=int,
                key_value=None,
                item_type=None,
                item_value=None,
            )

    def test_unit_data_structure_filter_dict_invalid_data_int_key_type_2_key_value_none_item_type_none_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data,
        key_type set to int, key_value set to 2, and item_type set to None while item_value is also set to None.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to int, key_value set to 2, and item_type set to None while item_value is also set to None.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=int,
                key_value=2,
                item_type=None,
                item_value=None,
            )

    def test_unit_data_structure_filter_dict_invalid_data_int_key_type_none_key_value_int_item_type_none_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data,
        key_type set to int, key_value set to None, item_type set to int, and item_value set to None.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to int, key_value set to None, item_type set to int, and item_value set to None.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=int,
                key_value=None,
                item_type=int,
                item_value=None,
            )

    def test_unit_data_structure_filter_dict_invalid_data_none_key_type_none_key_value_int_item_type_none_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data,
        key_type set to None, key_value set to None, item_type set to int, and item_value set to None.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to None, key_value set to None, item_type set to int, and item_value set to None.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=None,
                key_value=None,
                item_type=int,
                item_value=None,
            )

    def test_unit_data_structure_filter_dict_invalid_data_none_key_type_none_key_value_int_item_type_23_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data,
        key_type set to None, key_value set to None, item_type set to int, and item_value set to 23.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to None, key_value set to None, item_type set to int, and item_value set to 23.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=None,
                key_value=None,
                item_type=int,
                item_value=23,
            )

    def test_unit_data_structure_filter_dict_invalid_data_int_key_type_2_key_value_int_item_type_none_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data,
        key_type set to int, key_value set to 2, item_type set to int, and item_value set to None.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to int, key_value set to 2, item_type set to int, and item_value set to None.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data,
                key_type=int,
                key_value=2,
                item_type=int,
                item_value=None,
            )

    def test_unit_data_structure_filter_dict_invalid_data_int_key_type_2_key_value_int_item_type_23_item_value(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict function when provided with invalid data,
        key_type set to int, key_value set to 2, item_type set to int, and item_value set to 23.

        Assertions:
        - Uses assertRaises to check if filter_dict raises a TypeError when provided with invalid data,
          key_type set to int, key_value set to 2, item_type set to int, and item_value set to 23.
        """
        with self.assertRaises(Exception):
            DataStructureCore().filter_dict_by_key_and_value_type_and_value(
                data=self.data, key_type=int, key_value=2, item_type=int, item_value=23
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_valid_dict_and_valid_type_int_key(
        self,
    ):
        expected_result = {2: 23, 3: 4, 5: "a"}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=int
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_valid_dict_and_valid_type_bool_key(
        self,
    ):
        expected_result = {True: False}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=bool
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_valid_dict_and_valid_type_float_key(
        self,
    ):
        expected_result = {3.5: 1.8}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=float
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_valid_dict_and_valid_type_str_key(
        self,
    ):
        expected_result = {"b": 7, "hola": "adios"}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=str
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_valid_dict_and_valid_type_exception_key(
        self,
    ):
        expected_result = {Exception: Exception}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=Exception
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(str(expected_result), str(result))

    def test_unit_data_structure_filter_dict_by_data_type_key_valid_dict_and_valid_type_none_key(
        self,
    ):
        expected_result = {
            2: 23,
            3: 4,
            5: "a",
            "b": 7,
            True: False,
            3.5: 1.8,
            "hola": "adios",
            Exception: Exception,
            (1, 3): 6,
        }
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=NoneType
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_invalid_dict_and_valid_type_int_key(
        self,
    ):
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.data, type_data=int
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_valid_dict_and_valid_type_int_value(
        self,
    ):
        expected_result = {2: 23, 3: 4, "b": 7, (1, 3): 6}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=int
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_valid_dict_and_valid_type_bool_value(
        self,
    ):
        expected_result = {True: False}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=bool
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_valid_dict_and_valid_type_float_value(
        self,
    ):
        expected_result = {3.5: 1.8}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=float
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_valid_dict_and_valid_type_str_value(
        self,
    ):
        expected_result = {5: "a", "hola": "adios"}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=str
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_valid_dict_and_valid_type_exception_value(
        self,
    ):
        expected_result = {Exception: Exception}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=Exception
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_valid_dict_and_valid_type_none_value(
        self,
    ):
        expected_result = {
            2: 23,
            3: 4,
            5: "a",
            "b": 7,
            True: False,
            3.5: 1.8,
            "hola": "adios",
            Exception: Exception,
            (1, 3): 6,
        }
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=NoneType
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_invalid_dict_and_valid_type_int_value(
        self,
    ):
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.data, type_data=int
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_none(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (NoneType).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when filtering
        data of the specified type ('NoneType') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = self.dictionary
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=NoneType
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=NoneType
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_str(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (str).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when filtering
        data of the specified type ('str') from the input data. The expected result is a dict containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {"b": 7, "hola": "adios"}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=str
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_str(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=str
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_str(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_int(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (int).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when filtering
        data of the specified type ('int') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {2: 23, 3: 4, 5: "a"}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=int
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_int(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=int
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_int(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_float(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (float).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when
        filtering data of the specified type ('float') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {3.5: 1.8}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=float
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_float(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=float
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_float(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_bool(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (bool).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when
        filtering data of the specified type ('bool') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {True: False}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=bool
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_bool(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=bool
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_bool(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_list(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (list).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when
        filtering data of the specified type ('list') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=list
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_list(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=list
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_list(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_dict(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (dict).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when
        filtering data of the specified type ('dict') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=dict
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_dict(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=dict
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_dict(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_valid_type_data_exception(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key' function with valid data and a valid data type (Exception).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when
        filtering data of the specified type ('Exception') from the input data. The expected result is a list
        containing the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {Exception: Exception}
        result = DataStructureCore().filter_dict_by_data_type_key(
            data=self.dictionary, type_data=Exception
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(str(expected_result), str(result))

    def test_unit_data_structure_filter_dict_by_data_type_key_with_invalid_data_and_valid_type_data_exception(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.invalid_data, type_data=Exception
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_with_valid_data_and_invalid_type_data_exception(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_none(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (NoneType).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('NoneType') from the input data. The expected result is a list
        containing the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = self.dictionary
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=NoneType
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with
        invalid data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=NoneType
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key function when provided with valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_str(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (str).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('str') from the input data. The expected result is a dict containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {5: "a", "hola": "adios"}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=str
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_str(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=str
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_str(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_int(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (int).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('int') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {2: 23, 3: 4, "b": 7, (1, 3): 6}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=int
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_int(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=int
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_int(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_float(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (float).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('float') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {3.5: 1.8}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=float
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_float(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=float
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_float(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_bool(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (bool).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('bool') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {True: False}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=bool
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_bool(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=bool
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_bool(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_list(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (list).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('list') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=list
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_list(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=list
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_list(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_dict(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (dict).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_value' function when
        filtering data of the specified type ('dict') from the input data. The expected result is a list containing
        the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=dict
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_dict(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=dict
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_dict(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_valid_type_data_exception(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_value' function with valid data and a valid data type (Exception).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key' function when filtering
        data of the specified type ('Exception') from the input data. The expected result is a list containing the
        filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {Exception: Exception}
        result = DataStructureCore().filter_dict_by_data_type_value(
            data=self.dictionary, type_data=Exception
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(str(expected_result), str(result))

    def test_unit_data_structure_filter_dict_by_data_type_value_with_invalid_data_and_valid_type_data_exception(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with invalid
        data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.invalid_data, type_data=Exception
            )

    def test_unit_data_structure_filter_dict_by_data_type_value_with_valid_data_and_invalid_type_data_exception(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_value function when provided with valid
        data but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_value(
                data=self.dictionary, type_data=self.invalid_data_type
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_and_value_with_valid_data_and_valid_type_data_int(
        self,
    ):
        """
        Test case for the 'filter_dict_by_data_type_key_and_value' function with valid data and a valid data type
        (NoneType).

        This test aims to verify the correct functionality of the 'filter_dict_by_data_type_key_and_value' function when
        filtering data of the specified type ('NoneType') from the input data. The expected result is a list
        containing the filtered data.

        The input data for this test should be appropriately set in the 'self.data' attribute.

        Assertions:
        - Checks if the result is an instance of a dict, ensuring the function returns a dict.
        - Compares the result with the expected result to confirm accurate data filtering.
        """
        expected_result = {2: 23, 3: 4}
        result = DataStructureCore().filter_dict_by_data_type_key_and_value(
            data=self.dictionary, key_type_data=int, value_type_data=int
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_structure_filter_dict_by_data_type_key_and_value_with_invalid_data_and_valid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key_and_value function when provided with
        invalid data (along with a valid data type) to ensure the function appropriately handles cases of invalid input.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key_and_value(
                data=self.invalid_data, key_type_data=int, value_type_data=NoneType
            )

    def test_unit_data_structure_filter_dict_by_data_type_key_and_value_with_valid_data_and_invalid_type_data_none(
        self,
    ):
        """
        This test block verifies the behavior of the filter_dict_by_data_type_key_and_value function when provided with
        valid data
        but an invalid data type to ensure the function handles cases where the type of the data is not valid.
        """
        with self.assertRaises(TypeError):
            DataStructureCore().filter_dict_by_data_type_key_and_value(
                data=self.dictionary,
                key_type_data=self.invalid_data,
                value_type_data=self.invalid_data_type,
            )
