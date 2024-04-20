from types import NoneType
from typing import Union, Type, Optional, Any

from jimena.core.components.data.core import JDataCore


class DataStructureCore(JDataCore):

    def __init__(self):
        super().__init__()

    def filter_list_by_data_type(self, data: list, type_data: Type) -> list:
        """
        Filter a list based on the specified data type.
        :param data: The list to be filtered.
        :type data: list
        :param type_data: The target data type.
        :type type_data: str
        :return: A new list containing only elements of the specified data type.
        :rtype: list
        :exception If an error occurs during the filtering process, such as an invalid data type.
        """
        if not isinstance(data, list):
            self.logger.error(
                f"Type error - data type: {type(data)}, but expected list"
            )
            raise TypeError
        try:
            if type_data == int:
                response = [
                    d
                    for d in data
                    if isinstance(d, type_data) and not isinstance(d, bool)
                ]
            else:
                response = [d for d in data if isinstance(d, type_data)]
            return response
        except TypeError as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_dict_by_data_type_key(self, data: dict, type_data: Type) -> dict:
        """
        Filter a dictionary based on the specified data type of keys.
        :param data: The dictionary to be filtered.
        :type data: dict
        :param type_data: The target data type for keys.
        :type type_data: type
        :return: A new dictionary containing only elements with keys of the specified data type.
        :rtype: dict
        :exception If an error occurs during the filtering process, such as an invalid data type.
        """
        if not isinstance(data, dict):
            self.logger.error(
                f"Type error - data type: {type(data)}, but expected dict"
            )
            raise TypeError
        try:
            if type_data is NoneType:
                return data

            if type_data == int:
                response = {
                    key: value
                    for key, value in data.items()
                    if isinstance(key, type_data) and not isinstance(key, bool)
                }
            elif type_data == Exception:
                response = {
                    key: value for key, value in data.items() if key is Exception
                }
            else:
                response = {
                    key: value
                    for key, value in data.items()
                    if isinstance(key, type_data)
                }

            return response
        except TypeError as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_dict_by_data_type_value(self, data: dict, type_data: Type) -> dict:
        """
        Filter a dictionary based on the specified data type of values.
        :param data: The dictionary to be filtered.
        :type data: dict
        :param type_data: The target data type for values.
        :type type_data: type
        :return: A new dictionary containing only elements with values of the specified data type.
        :rtype: dict
        :exception If an error occurs during the filtering process, such as an invalid data type.
        """
        if not isinstance(data, dict):
            self.logger.error(
                f"Type error - data type: {type(data)}, but expected dict"
            )
            raise TypeError
        try:
            if type_data is NoneType:
                return data

            if type_data == int:
                response = {
                    key: value
                    for key, value in data.items()
                    if isinstance(value, type_data) and not isinstance(value, bool)
                }
            elif type_data == Exception:
                response = {
                    key: value for key, value in data.items() if value is Exception
                }
            else:
                response = {
                    key: value
                    for key, value in data.items()
                    if isinstance(value, type_data)
                }
            return response
        except TypeError as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_dict_by_data_type_key_and_value(
        self, data: dict, key_type_data: Type, value_type_data: Type
    ) -> dict:
        """
        Filter a dictionary by the data type of keys and values.

        :param data: The dictionary to filter.
        :type data: dict
        :param key_type_data: The target data type for keys.
        :type key_type_data: type
        :param value_type_data: The target data type for values.
        :type value_type_data: type
        :return: A new dictionary containing only elements with keys and values of the specified data type.
        :rtype: dict
        """
        try:
            dict_key = self.filter_dict_by_data_type_key(
                data=data, type_data=key_type_data
            )
            dict_value = self.filter_dict_by_data_type_value(
                data=data, type_data=value_type_data
            )
            return {key: dict_key[key] for key in dict_key if key in dict_value}
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_list_data_by_data_range(
        self,
        data: list,
        lower_limit: Optional[Union[int, float]],
        upper_limit: Optional[Union[int, float]],
    ):
        """
        Filter a list based on the specified range.
        :param data: The list to be filtered.
        :type data: list
        :param lower_limit: The lower limit
        :type lower_limit: int or float or None
        :param upper_limit: The upper limit
        :type upper_limit: int or float or None
        :return: A new list containing only elements in the specified range.
        :rtype: list
        """
        if not isinstance(data, list):
            raise TypeError("The data has to be a list")
        data_filtered = self.filter_list_by_data_type(
            data=data, type_data=int
        ) + self.filter_list_by_data_type(data=data, type_data=float)
        if lower_limit is None and upper_limit is None:
            return sorted(data_filtered)

        if upper_limit is None:
            data_filtered = [x for x in data_filtered if lower_limit <= x]
        elif lower_limit is None:
            data_filtered = [x for x in data_filtered if x <= upper_limit]
        else:
            data_filtered = [
                x for x in data_filtered if lower_limit <= x <= upper_limit
            ]

        return sorted(data_filtered)

    def filter_dict_by_key_and_value_type_and_value(
        self,
        data: dict,
        key_type: Type,
        key_value: Any,
        item_type: Type,
        item_value: Any,
    ) -> dict:
        """
        Filters a dictionary based on specified key and item types and their respective values.
        :param data: The dictionary to filter.
        :type data: dict
        :param key_type: The type of keys to filter.
        :type key_type: NewType
        :param key_value: The value of keys to filter.
        :param item_type: The type of items to filter.
        :type item_type: NewType
        :param item_value: The value of items to filter.
        :return: A filtered dictionary based on the specified criteria.
        :rtype: dict
        """
        if not isinstance(data, dict):
            self.logger.warning(f"Warning: The data {data} isn't a dictionary")
        if key_type is NoneType and item_type is NoneType:
            return data
        filtered_dict = DataStructureCore().filter_dict_by_data_type_key_and_value(
            data=data, key_type_data=key_type, value_type_data=item_type
        )

        if key_value is None and item_value is None:
            return filtered_dict

        final_dict = {}
        for key, value in filtered_dict.items():
            if (
                item_value is None or item_value is not None and value == item_value
            ) and (key_value is None or key_value is not None and key == key_value):
                final_dict[key] = value
        return final_dict

    def validate_file_extension(self, path: str, extension: str):
        """
        Checks if the extension of a file path matches a specified extension.
        :param path: The file path to check.
        :type path: str
        :param extension: The expected file extension.
        :type extension: str
        :raises ValueError: If the file path does not end with the specified extension.
        """
        if not path.endswith(extension):
            self.logger.error(
                f"Error: the extension of the file {path} isn't {extension} "
            )

    @classmethod
    def validate_data_types_in_dict(
        cls, dict_data_type: dict, dict_data_value: dict
    ) -> bool:
        """
        Validates whether the value (or list of values) in a dictionary (`dict_data_value`) has the
        same data type as the data type specified in another dictionary (`dict_data_type`).

        :param dict_data_type: Dictionary containing the data types to be validated.
        :type dict_data_type: dict
        :param dict_data_value: Dictionary containing the values to be validated.
        :type dict_data_value: dict
        :return: Returns True if the value in `dict_data_value` is an instance of the data type specified in
                 `dict_data_type`. Returns False otherwise.
        :raises ValueError: Raises exceptions with descriptive messages if the dictionaries are invalid
                due to their length or if the keys do not match.
        """
        if len(dict_data_type) != len(dict_data_value):
            return False
        for key, value in dict_data_value.items():
            if key not in dict_data_type.keys():
                cls.logger.warning(
                    f"The dictionary {dict_data_type} doesn't contain the key {key}"
                )
                return False

            if not isinstance(value, dict_data_type[key]):
                cls.logger.warning(
                    f"The value of the key {key} is {value} but it was expected {type(dict_data_type[key])}"
                )
                return False

        return True
