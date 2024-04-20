"""
This module contains the RegexTools class, providing various methods for working with regular expressions,
including pattern searching, filtering, and manipulation.
"""

import re
from re import Pattern
from typing import List, Union, Optional, Iterable


class RegexTools:
    """
    A utility class for working with regular expressions.

    This class provides various methods to perform operations related to regular expressions
    such as pattern searching, filtering, and manipulation.
    """

    def __init__(self):
        """
        Initializes the RegexTools class.

        This method initializes the RegexTools class and sets up the logger using the LoggingHandler.
        """
        super().__init__()

    def to_pattern(self, string: str) -> Pattern:
        """
        Converts a string into a regular expression pattern.

        **Documentation**:

        `Function re-compile <https://docs.python.org/3/library/re.html#re.compile>`_

        This function takes a string filter 'f' and compiles it into a regular expression pattern
        using to 're. compile' function from the 're' module.

        :param string: Filter string to be converted into a regular expression pattern.
        :type string: str
        :return: Regular expression pattern generated from the filter string.
        :rtype: Pattern
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            response = re.compile(rf"{string}")
            return response
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def search_pattern(self, pattern: Pattern, string: str) -> Optional[re.Match]:
        """
        Searches for the first occurrence of a pattern in a given string.

        This function uses to 're. search' function from the 're' module to find the first occurrence
        of the specified pattern within the given string.

        **Documentation**:

        `Function re-search <https://docs.python.org/3/library/re.html#re.search>`_

        :param pattern: The regular expression pattern to search for.
        :type pattern: Pattern
        :param string: The string in which to search for the pattern.
        :type string: str
        :return: The match object if the pattern is found, otherwise None.
        :rtype: Optional[Match]
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            return re.search(pattern=pattern, string=string)
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def to_and_patterns(self, strings: Union[List[str], List[Pattern]]) -> Pattern:
        """
        Converts a list of filters into a concatenated ANDs regular expression pattern.

        This function takes a list containing strings and/or precompiled regular expression patterns ('Pattern')
        and generates a regular expression pattern by concatenating the filters using the AND operator ('.*?').
        Each filter is enclosed within a non-capturing group in the resulting regular expression.

        **Documentation**:

        `Function re-compile <https://docs.python.org/3/library/re.html#re.compile>`_

        :param strings: List of strings and/or precompiled regular expression patterns.
        :type strings: Union[List[str], List[Pattern]]
        :return: Regular expression pattern with the filters introduced separated by ANDs.
        :rtype: Pattern
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            # Convert all items in the 'filters' list to strings or existing pattern strings
            strings = [f.pattern if isinstance(f, Pattern) else f for f in strings]
            # Join the filters using the AND operator within a non-capturing group in the regular expression
            pattern = "".join(
                [rf"({self.REGEX_AND_OPERATOR}{f})" for f in strings if f is not None]
            )
            pattern = re.compile(rf".*{pattern}.*")
            return pattern
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def to_or_patterns(self, strings: Union[List[str], List[Pattern]]) -> Pattern:
        """
        Converts a list of filters into a concatenated ORs regular expression pattern.

        This function takes a list containing strings and/or precompiled regular expression patterns ('Pattern')
        and generates a regular expression pattern by concatenating the filters using the OR operator ('|').
        Each filter is enclosed within a non-capturing group in the resulting regular expression.
        """
        try:
            # Convert all items in the 'filters' list to strings
            strings = [
                f.pattern if isinstance(f, Pattern) else f
                for f in strings
                if f is not None
            ]
            # Join the filters using the OR operator within a non-capturing group in the regular expression
            pattern = re.compile(rf".*({'|'.join(strings)}).*")
            return pattern
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_dict_list_by_pattern(
        self, pattern: Pattern, input_data: List[dict], key_to_match: str
    ) -> List[dict]:
        """
        Filters a list of dictionaries by matching a pattern within a specific key's content.

        This function filters a list of dictionaries based on whether the content of the specified key
        matches the provided regular expression pattern.

        **Documentation**:

        `Function re-search <https://docs.python.org/3/library/re.html#re.search>`_

        :param pattern: The regular expression pattern to search for.
        :type pattern: Pattern
        :param input_data: The list of dictionaries to filter.
        :type input_data: List[Dict[str, Any]]
        :param key_to_match: The key within each dictionary whose content will be matched against the pattern.
        :type key_to_match: str
        :return: A list of dictionaries containing contents matching the pattern.
        :rtype: List[Dict[str, Any]]
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            response = list(
                filter(
                    lambda c: self.search_pattern(
                        pattern=pattern, string=c[key_to_match]
                    ),
                    input_data,
                )
            )
            return response
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_str_list_by_pattern(
        self, pattern: Pattern, input_data: List[str]
    ) -> List[str]:
        """
        Filters a list of strings based on a given regular expression pattern.

        This function filters a list of strings based on whether each string matches the provided
        regular expression pattern.

        **Documentation**:

        `Function re-search <https://docs.python.org/3/library/re.html#re.search>`_

        :param pattern: The regular expression pattern to search for.
        :type pattern: Pattern
        :param input_data: The list of strings to filter.
        :type input_data: List[str]
        :return: A list of strings that match the pattern.
        :rtype: List[str]
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            response = list(
                filter(
                    lambda c: self.search_pattern(pattern=pattern, string=c),
                    input_data,
                )
            )

            return response
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def filter_iterable_by_pattern(
        self, pattern: Pattern, input_data: Iterable, evaluate: str
    ) -> Iterable:
        """
        Filters an iterable based on a given regular expression pattern.

        This function filters an iterable object (e.g., list, tuple, etc.) based on whether each element
        evaluates to a match for the provided regular expression pattern.

        **Documentation**:

        `Function re-search <https://docs.python.org/3/library/re.html#re.search>`_

        :param pattern: The regular expression pattern to search for.
        :type pattern: Pattern
        :param input_data: The iterable object to filter.
        :type input_data: Iterable
        :param evaluate: The expression to evaluate for each element in the iterable to match the pattern.
        :type evaluate: str
        :return: An iterable containing elements that match the pattern.
        :rtype: Iterable
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            response = filter(
                lambda c: self.search_pattern(pattern=pattern, string=eval(evaluate)),
                input_data,
            )
            return response
        except Exception as e:
            # Log the error and raise it further
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    # constants
    REGEX_NOT_SLASH_TERMINATION = r"^(?!.*\/$).*$"
    REGEX_SLASH_TERMINATION = r".*/$"
    REGEX_NOT_INCLUDE_SLASH = r"^[^\/]*$"
    REGEX_INCLUDE_SLASH_MAX_N_TIMES = r"^([^\/]*\/){0,%s}[^\/]*$"
    REGEX_INCLUDE_SLASH_N_TIMES = r"^([^\/]*\/){0,%s}[^\/]*$"
    REGEX_REPLICA_TERMINATION = r".*-replica$"
    REGEX_NOT_REPLICA_TERMINATION = r"^(?!.*-replica$).*$"
    REGEX_AND_OPERATOR = r"?=.*"
    REGEX_IS_HASH = r"([a-fA-F\d]{32})"
