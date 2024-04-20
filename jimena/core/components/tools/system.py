import os
import platform
import subprocess
from pathlib import Path
from typing import Union, Optional, List

from jimena.core import get_j_core_source_folder_path
from .constants import TESTS, RESOURCES, COMPONENTS
from .decorators import ToolsDecorators
from ..core import JCore


class SystemTools(JCore):
    """
    A utility class providing system-related tools.

    This class contains methods related to system operations such as folder creation, file handling, etc.
    """

    def __init__(self):
        """
        Initializes the SystemTools class.

        This method initializes the SystemTools class and sets up the logger using the LoggingHandler.
        """
        super().__init__()

    def set_cwd(self, directory_path):
        """
        Change the current working directory to the specified directory path,
        and list the files in the directory.

        Args:
            directory_path (str): The path to the directory to change to.

        Returns:
            list: A list of file names in the directory.
        """
        try:
            os.chdir(directory_path)
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    @ToolsDecorators().ignore_raise
    def create_local_folder_if_not_exists(self, folder_path: Union[str, Path]) -> bool:
        """
        Creates a local folder if it does not already exist.

        This method attempts to create a folder at the specified path if it doesn't already exist.
        It returns True if the folder is created, otherwise False.

        :param folder_path: The path of the folder to be created.
        :type folder_path: Union[str, Path]
        :return: True if the folder is created, False otherwise.
        :rtype: bool
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            self.logger.debug(f"Create Local Folder: {folder_path}")
            return not Path(folder_path).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def get_files_in_local_folder(self, folder_path: Union[str, Path]) -> list:
        """
        Retrieves a list of files in the specified local folder.

        This method traverses the specified folder path and retrieves a list of all files within it.

        :param folder_path: The path of the folder to retrieve files from.
        :type folder_path: Union[str, Path]
        :return: A list of file paths within the folder.
        :rtype: List[str]
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            response = []
            for folder_p, folder_name, files_path in os.walk(folder_path):
                for file_path in files_path:
                    file_path = os.path.join(folder_p, file_path)
                    response.append(file_path)
                self.logger.debug(f"In Folder Path: {folder_p} - Files: {files_path}")
            return response
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    @ToolsDecorators().ignore_raise
    def remove_local_file(self, file_path: Union[str, Path]) -> bool:
        """
        Removes a local file.

        This method attempts to remove a file at the specified path.
        Returns True if the file is removed successfully, otherwise False.

        :param file_path: The path of the file to be removed.
        :type file_path: Union[str, Path]
        :return: True if the file is removed, False otherwise.
        :rtype: bool
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            self.logger.debug(f"Remove Local File: {file_path}")
            os.remove(Path(file_path))
            return not os.path.exists(file_path)
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    @ToolsDecorators().ignore_raise
    def remove_local_files(self, files_path: List[str]) -> List[bool]:
        """
        Removes multiple local files.

        This method attempts to remove multiple files based on the provided list of file paths.
        Returns a list indicating the removal status for each file.

        :param files_path: List of file paths to be removed.
        :type files_path: List[str]
        :return: List of removal status for each file.
        :rtype: List[bool]
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            self.logger.debug(f"Remove files: {files_path}")
            return [
                self.remove_local_file(file_path=f) for f in files_path if f is not None
            ]
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    @ToolsDecorators().ignore_raise
    def remove_local_folder(
        self, folder_path: Union[str, Path], paths_to_join: Optional[list] = None
    ) -> bool:
        """
        Remove a local directory.

        This method attempts to remove a file at the specified path.
        Returns True if the file is removed successfully, otherwise False.

        :param folder_path: Path of the directory to be removed.
        :type folder_path: Union[str, Path]
        :param paths_to_join: Additional paths to extend the directory path.
        :type paths_to_join: Optional[list]
        :return: True if the file is removed, False otherwise.
        :rtype: bool
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            import shutil

            self.logger.debug(
                f"Remove Local Folder: {folder_path} with extends path: {paths_to_join}"
            )
            if paths_to_join:
                folder_path = self.join_paths(
                    initial_path=folder_path, paths_to_join=paths_to_join
                )
            shutil.rmtree(Path(folder_path))
            return not os.path.exists(folder_path)
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    @ToolsDecorators().ignore_raise
    def update_cwd(self, cwd: str):
        """
        Updates the current working directory.

        This method attempts to update the current working directory to the specified 'cwd' path.

        :param cwd: The path to update the current working directory to.
        :type cwd: str
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            self.logger.debug(f"Update Current Working Directory To: {cwd}")
            os.chdir(cwd)
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    @ToolsDecorators().ignore_raise
    def get_folder_path_from_local_file_path(self, file_path: str) -> str:
        """
        Get the folder path from a local file path.

        This method retrieves the directory path from the provided 'file_path'.

        :param file_path: The file path for which the folder path is obtained.
        :type file_path: str
        :return: The folder path derived from the file path.
        :rtype: str
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            response = os.path.dirname(file_path)
            self.logger.debug(f"Get Folder Path From {file_path}: {response}")
            return response
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def get_current_folder_being_run(self, file_path: str) -> str:
        """
        Get the current folder path where a file is being executed.

        This method retrieves the current folder path where the specified 'file' is being executed.

        :param file_path: File path for which the current folder path is being obtained.
        :type file_path: str
        :return: Current folder path.
        :rtype: str
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            return os.path.dirname(os.path.abspath(file_path))
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def join_paths(self, initial_path: str, paths_to_join: list) -> str:
        """
        Join multiple paths into a single path.

        This method concatenates multiple paths into a single path.

        :param initial_path: Initial path to start joining.
        :type initial_path: str
        :param paths_to_join: List of paths to be joined.
        :type paths_to_join: list
        :return: Joined path.
        :rtype: str
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            result = initial_path
            for p in paths_to_join:
                result = os.path.join(result, p)
            return result
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def exists_path(self, path: str) -> bool:
        """
        Check if a given path exists.

        This method checks whether the specified path exists in the file system.

        :param path: The path to be checked.
        :type path: str
        :return: True if the path exists, False otherwise.
        :rtype: bool
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            return os.path.exists(path)
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e


class ResourcesTools(SystemTools):
    """
    A class that extends SystemTools and provides methods related to resource management.

    This class inherits from SystemTools and provides additional functionalities for handling resources,
    such as calculating the maximum number of threads based on available memory.
    """

    def max_threads_by_memory(self, memory_thread: int = 500) -> int:
        """
        Calculates the maximum number of threads based on available memory.

        This method calculates the maximum number of threads that can be created based on the available memory
        and CPU cores. It uses the provided 'memory_thread' parameter to estimate the amount of memory
        desired to allocate per thread.

        :param memory_thread: Amount of memory (in MB) desired to allocate per thread.
        :type memory_thread: int, optional
        :return: The maximum number of threads that can be created based on available memory and CPU cores.
        :rtype: int
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            if platform.system() == "Windows":
                output = subprocess.check_output(
                    ["wmic", "OS", "get", "FreePhysicalMemory"], universal_newlines=True
                )
                available_memory_kb = int(output.split("\n")[1])
                available_memory_mb = round(
                    available_memory_kb / 1024, 2
                )  # Convert KB to MB
            else:  # For Linux/Mac
                output = subprocess.check_output(
                    ["free", "-m"], universal_newlines=True
                )
                lines = output.split("\n")
                available_memory_mb = int(lines[1].split()[3])  # Free memory column

            # Define the amount of memory in megabytes to allocate per thread
            memory_per_thread_mega_bytes = memory_thread

            # Calculate the maximum number of threads based on available memory
            max_threads = available_memory_mb // memory_per_thread_mega_bytes

            # Limit the maximum number of threads to the number of available CPU cores
            self.logger.info(
                f"Memory by thread: {memory_per_thread_mega_bytes} MB - "
                f"Available memory: {available_memory_mb} MB - "
                f"Max threads: {max_threads}"
            )
            return max_threads
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def remove_resource_folder_path(self, testing: bool, extend: Optional[list] = None):
        """
        Remove the resource folder path.

        :param testing: A boolean flag indicating whether the code is in a testing environment.
        :type testing: bool
        :param extend: Additional paths to extend the resource folder path.
        :type extend: Optional[list]
        :return: None
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            resource_path = self.get_resource_folder_path(testing=testing)
            response = self.remove_local_folder(
                folder_path=resource_path, paths_to_join=extend
            )
            if response:
                status = "SUCCESS"
            else:
                status = "FAILED"

            self.logger.debug(
                f"{status} - Remove folder: "
                f"{self.join_paths(initial_path=resource_path, paths_to_join=extend)}"
            )
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def get_resource_folder_path(self, testing: bool) -> str:
        """
        Get the path of the resource folder.

        This method retrieves the path of the resource folder based on the provided boolean flag 'testing'.
        If 'testing' is True, it sets the current working directory to the jimena core source folder path and
        constructs the resource folder path as 'j_core_source_folder_path/tests/resources'. Otherwise,
        it constructs the resource folder path as 'os.getcwd()/components/resources'.

        :param testing: A boolean flag indicating whether the code is in a testing environment.
        :type testing: bool
        :return: The path of the resource folder.
        :rtype: str
        :raises Exception: :py:class:`Exception` If an error occurs during the operation.
        """
        try:
            j_core_source_folder_path = get_j_core_source_folder_path()
            if testing:
                self.update_cwd(cwd=j_core_source_folder_path)
                cwd = os.path.join(os.getcwd(), TESTS, RESOURCES)
            else:
                cwd = os.path.join(os.getcwd(), COMPONENTS, RESOURCES)
            self.logger.debug(f"Get Resource Folder Path - {cwd}")
            return cwd
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e
