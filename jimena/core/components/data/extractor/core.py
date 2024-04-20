import csv
import json

from jimena.core.components.data.core import JDataCore


class DataExtractorCore(JDataCore):

    def __init__(self):
        super().__init__()

    def json_extractor(self, path: str):
        """
        Extracts JSON data from a file given its path.
        :param path: The file path from which JSON data will be extracted.
        :type path: str
        :return: The JSON data extracted from the file.
        :rtype: dict
        :raises FileNotFoundError: If the file specified by the path does not exist.
        :raises PermissionError: If the program does not have permission to read the file.
        :raises json.JSONDecodeError: If the file does not contain valid JSON data.
        """
        try:
            with open(path, "r") as file:
                data = json.load(file)
                return data
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def csv_extractor(self, path: str):
        """
        Extracts data from a CSV file given its path.
        :param path: The file path from which CSV data will be extracted.
        :type path: str
        :return: The data extracted from the CSV file.
        :rtype: list of lists
        :raises FileNotFoundError: If the file specified by the path does not exist.
        :raises PermissionError: If the program does not have permission to read the file.
        """
        try:
            with open(path, "r") as file:
                csv_data = csv.reader(file)
                data = []
                for raw in csv_data:
                    data.append(raw)
                return data
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def generic_extractor(self, path: str):
        """
        Extracts data from a file given its path.
        :param path: The file path from which data will be extracted.
        :type path: str
        :return: The data extracted from the file.
        :rtype: list of str
        :raises FileNotFoundError: If the file specified by the path does not exist.
        :raises PermissionError: If the program does not have permission to read the file.
        """
        try:
            with open(path, "r") as file:
                data = file.readlines()
                return data
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e
