import importlib
from typing import Optional

from jimena.core.components.core import JCore


class ImportTools(JCore):
    """Import tools class"""

    def __init__(self):
        super().__init__()

    def module_exists(
        self, module_name: str, package_name: Optional[str] = None
    ) -> bool:
        """
        Method that returns the existence or not of a module.

        The 'package_name' argument is required when performing a relative import. It
        specifies the package to use as the anchor point from which to resolve the
        relative import to an absolute import.

            True -> Correct module.
            False -> Incorrect module.

        :param package_name: Package name
        :param module_name: Module name.
        :return: [Bool] Response.
        """

        try:
            importlib.import_module(name=module_name, package=package_name)
            return True
        except ModuleNotFoundError:
            self.logger.warning(
                f"Module {module_name} not found. To install: pip install {module_name}"
            )
            return False
