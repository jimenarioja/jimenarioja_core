def get_j_core_source_folder_path():
    """
    Get the path of the j-core source folder.

    This function retrieves the path of the JCore source folder where the current script is located.

    :return: The path of the JCore source folder.
    :rtype: str
    :raises Exception: If an error occurs during the operation.
    """
    import os

    j_core_source_folder_path = os.path.dirname(p=__file__)
    return j_core_source_folder_path
