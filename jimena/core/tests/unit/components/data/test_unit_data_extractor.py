from jimena.core.components.data.extractor.core import DataExtractorCore
from jimena.core.tests.setup import JCoreTestCase


class TestUnitDataExtractor(JCoreTestCase):
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
        self.test_resource_data_folder = self.resource_tool_instance.join_paths(
            initial_path=self.test_resource_folder, paths_to_join=["data"]
        )
        self.test_resource_data_folder_json_file = (
            self.resource_tool_instance.join_paths(
                initial_path=self.test_resource_data_folder,
                paths_to_join=["json_file.json"],
            )
        )
        self.test_resource_data_folder_path_csv = (
            self.resource_tool_instance.join_paths(
                initial_path=self.test_resource_data_folder,
                paths_to_join=["csv_file.csv"],
            )
        )
        self.test_resource_data_folder_path_generic = (
            self.resource_tool_instance.join_paths(
                initial_path=self.test_resource_data_folder,
                paths_to_join=["generic_file.txt"],
            )
        )
        self.test_resource_data_folder_invalid_path = (
            self.resource_tool_instance.join_paths(
                initial_path=self.test_resource_data_folder,
                paths_to_join=["dataset.dat"],
            )
        )

    def tearDown(self) -> None:
        """
        Set up method called after each test case execution.
        """
        pass

    def test_unit_data_extractor_json_extractor_valid_path(self):
        expected_result = {"color": "Red", "fruit": "Apple", "size": "Large"}
        result = DataExtractorCore().json_extractor(
            self.test_resource_data_folder_json_file
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(expected_result, result)

    def test_unit_data_extractor_json_extractor_invalid_path(self):
        with self.assertRaises(Exception):
            DataExtractorCore().json_extractor(
                self.test_resource_data_folder_invalid_path
            )

    def test_unit_data_extractor_csv_extractor_valid_path(self):
        expected_result = ["hi", "that", "is", "a", "test!"]
        result = DataExtractorCore().csv_extractor(
            self.test_resource_data_folder_path_csv
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result[0])

    def test_unit_data_extractor_csv_extractor_invalid_path(self):
        with self.assertRaises(Exception):
            DataExtractorCore().csv_extractor(
                self.test_resource_data_folder_invalid_path
            )

    def test_unit_data_extractor_generic_extractor_valid_path(self):
        expected_result = ["hi, that is a test!\n"]
        result = DataExtractorCore().generic_extractor(
            self.test_resource_data_folder_path_generic
        )
        self.assertIsInstance(result, list)
        self.assertEqual(expected_result, result)

    def test_unit_data_extractor_generic_extractor_invalid_path(self):
        with self.assertRaises(Exception):
            DataExtractorCore().generic_extractor(
                self.test_resource_data_folder_invalid_path
            )
