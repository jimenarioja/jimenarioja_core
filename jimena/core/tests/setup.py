from unittest import TestCase

from jimena.core.components.tools.system import ResourcesTools


class JCoreTestCase(TestCase):
    """
    Base test case for JCore functionalities.
    """

    def setUp(self) -> None:
        """
        Displays information about the current test.
        """
        self.resource_tool_instance = ResourcesTools()

    @classmethod
    def setUpClass(cls):
        """
        Initializes common resources before running the tests.
        Sets up the logger and displays the initialization message.
        """
        cls.test_resource_folder = ResourcesTools().get_resource_folder_path(
            testing=True
        )

    @classmethod
    def tearDownClass(cls):
        """
        Finalizes common resources after running all tests.
        Displays the finish message.
        """
        pass
