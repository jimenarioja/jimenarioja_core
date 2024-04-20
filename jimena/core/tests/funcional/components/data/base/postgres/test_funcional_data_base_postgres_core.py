import subprocess
from unittest import TestCase
from jimena.core.components.data.base.postgres.core import DataBasePostgres


class TestFunctionalDataBasePostgresCore(TestCase):
    """
    Unit tests for the 'Decorators' class.

    This test class is designed to validate the functionality of the 'Decorators' class.
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
        self.database_postgres_object = DataBasePostgres()
        self.host = "localhost"
        self.database = "public"
        self.user = "jimenarioja"
        self.password = "jimena"
        self.not_valid_host = "1234567890"
        self.not_valid_user = "aaa"

        # create_table_command = "bash create_table.sh"

    def tearDown(self) -> None:
        self.database_postgres_object.close()
        self.assertTrue(self.database_postgres_object.cur.closed)
        self.assertFalse(self.database_postgres_object.conn.closed)

        # delete_table_command = "bash delete_table.sh"

    def test_functional_data_base_postgres_core_connect(self):
        self.database_postgres_object.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
        )
        self.assertTrue(self.database_postgres_object.conn)
        self.assertTrue(self.database_postgres_object.cur)
        self.assertEqual(self.database_postgres_object.conn.info.user, self.user)
        self.assertFalse(self.database_postgres_object.cur.closed)

    def test_functional_data_base_postgres_core_connect_not_valid(self):
        with self.assertRaises(Exception):
            self.database_postgres_object.connect(
                host=self.not_valid_host,
                database=self.database,
                user=self.not_valid_user,
                password=self.password,
            )

    def test_functional_data_base_postgres_core_save_changes(self):
        self.database_postgres_object.save_changes(self.database_postgres_object.conn)
        # TODO: add asserts

    def test_functional_data_base_postgres_core_save_changes_not_valid(self):
        with self.assertRaises(Exception):
            self.database_postgres_object.conn(self.database_postgres_object.conn)

    def test_functional_data_base_postgres_core_apply_script(self):
        table_name = "first table"
        sql_content = (
            "SELECT * FROM information_schema.tables WHERE table_schema = 'public'"
        )
        self.database_postgres_object.connect(
            host=self.host, database="jcore", user=self.user, password=self.password
        )
        result = self.database_postgres_object.apply_script(
            sql_content=sql_content, cur=self.database_postgres_object.cur
        )

        result

    def test_functional_data_base_postgres_core_apply_script_not_valid(self):
        with self.assertRaises(Exception):
            self.database_postgres_object.apply_script(
                sql_content="aw", cur=self.database_postgres_object.cur
            )

    def test_functional_data_base_postgres_config(self):
        filename = "config_file_postgres.txt"
        section = ""
        populate_table_command = "bash populate_table.sh"
        subprocess.run(populate_table_command, shell=True, check=True)
        self.database_postgres_object.apply_script(
            script_content=populate_table_command, cur=self.database_postgres_object.cur
        )
        # TODO: añadir section y terminar el test

    def test_functional_data_base_postgres_config_not_valid(self):
        not_valid_filename = "not_existing_file.txt"
        not_valid_section = "section"
        with self.assertRaises(Exception):
            self.database_postgres_object.config(
                filename=not_valid_filename, section=not_valid_section
            )

    def test_functional_data_base_postgres_show_version(self):
        self.database_postgres_object.show_version(
            self, self.database_postgres_object.cur
        )

    def test_functional_data_base_postgres_core_close(self):
        pass

    def test_functional_data_base_postgres_core_close_not_valid(self):
        pass
