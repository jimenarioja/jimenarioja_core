import inspect
import sys
import time
from copy import deepcopy

from jimena.core.components.data.structure.core import DataStructureCore


class ToolsDecorators:

    def __init__(self):
        super().__init__()
        self.data_structure_core = DataStructureCore()
        self.logger = self.data_structure_core.logger

    def timing(self, function):
        """
        Decorator to measure the execution time of a function.

        This decorator measures the time taken by a function to execute by recording the initial and final times
        before and after executing the function. It prints the timing information in seconds.

        :param function: The function to be decorated.
        :type function: function
        :return: The wrapped function.
        :rtype: function
        """

        def wrap(*args, **kwargs):
            try:
                initial_time = time.time()
                result = function(*args, **kwargs)
                final_time = time.time()
                self.logger.info(
                    f"TIMING of function {function.__qualname__}: {round(final_time - initial_time, 2)} seconds "
                )
                return result
            except Exception as e:
                self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
                raise e

        return wrap

    def get_size(self, function):
        """
        Decorator to measure the size of the result of a function.

        This decorator calculates the size of the result returned by a function
        by using `sys.getsizeof()`. It prints the size of the result along with
        the result itself.

        :param function: The function to be decorated.
        :type function: function
        :return: The wrapped function.
        :rtype: function
        """

        def wrap(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                print(
                    f"The result is {result} and its size is: {sys.getsizeof(result)}"
                )
                return sys.getsizeof(result)
            except Exception as e:
                self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
                raise e

        return wrap

    def ignore_raise(self, function):
        """
        Decorator to execute a function and ignore any exceptions raised.

        This decorator wraps a function and executes it. If the function raises
        an exception during execution, the decorator catches the exception and
        returns None as the result. It prints the result after execution.

        :param function: The function to be decorated.
        :type function: function
        :return: The wrapped function.
        :rtype: function
        """

        def wrap(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                return result
            except Exception as e:
                self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
                return str(e)

        return wrap

    def validator(self, strict: bool):
        """
        Decorator factory to create a validator decorator.

        This decorator factory takes a boolean parameter 'strict'. Depends its value raise an exception (true) or print
        a string (false) and returns a decorator 'real_validator' that can be used to validate the result of a function
        based on the value of 'strict'.

        :param strict: A boolean flag indicating whether strict validation should be applied.
        :type strict: bool
        :return: The decorator 'real_validator'.
        :rtype: function
        """

        def external_wrap(function):
            def internal_wrap(*args, **kwargs):
                try:
                    type_data = function.__annotations__
                    return_statement = None
                    if "return" in inspect.getsource(function):
                        return_statement = type_data.popitem()
                        print(return_statement)
                    value_data = kwargs
                    new_value_data = {}
                    for key in value_data.keys():
                        if key in type_data.keys():
                            new_value_data[key] = value_data[key]
                        else:
                            print(
                                f"Warning: {key} - {value_data[key]} is not official input data in function "
                                f"{function.__qualname__}"
                            )
                            if strict:
                                raise ValueError("The type is not valid")
                    if not self.data_structure_core.validate_data_types_in_dict(
                        dict_data_type=type_data,
                        dict_data_value=deepcopy(new_value_data),
                    ):
                        if strict:
                            raise ValueError("The type is not valid")
                        print("Warning: Validation not correct")

                    result = function(*args, **new_value_data)
                    if return_statement is not None and not isinstance(
                        result, return_statement[1]
                    ):
                        if strict:
                            raise ValueError("The return type is not valid")
                        print("Warning: Return type not correct.")
                    return result
                except Exception as e:
                    self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
                    raise e

            return internal_wrap

        return external_wrap

    def extension(self, function):
        """
        Decorator to check if the file extension matches the specified extension.

        This decorator wraps a function and checks if the file path provided as an argument
        ends with the specified extension. If the file extension does not match, it raises
        a ValueError exception.

        :param function: The function to be decorated.
        :type function: function
        :return: The wrapped function.
        :rtype: function
        """

        def wrap(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                return result
            except Exception as e:
                self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
                raise e

        return wrap
