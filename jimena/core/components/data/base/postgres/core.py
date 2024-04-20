from typing import Optional, Tuple

import psycopg2
from psycopg2.extensions import connection
from configparser import ConfigParser
from jimena.core.components.core import JCore
from jimena.core.components.tools.constants import FILENAME, SECTION


class DataBasePostgres(JCore):

    def __init__(self):
        super().__init__()
        self.conn = None
        self.cur = None

    def config(self, filename: str, section: str) -> dict:
        """
        Reads configuration parameters from a file and returns them as a dictionary.

        This method reads configuration parameters from the specified file using
        the ConfigParser module. It extracts parameters from the specified section
        and returns them as a dictionary. If the specified section does not exist
        in the file, it logs an error and returns an empty dictionary.

        :param filename: The path to the configuration file.
        :type filename: str
        :param section: The section of the configuration file to read parameters from.
        :type section: str
        :return: A dictionary containing the configuration parameters.
        :rtype: dict
        """
        parser = ConfigParser()
        parser.read(filename)

        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            self.logger.ERROR(
                "Section {0} not found in the {1} file".format(section, filename)
            )

        return db

    def connect(
        self, host: str, database: str, user: str, password: str
    ) -> tuple[psycopg2.extensions.connection, psycopg2.extensions.cursor]:
        """
        Connects to a database and returns a tuple containing the connection and cursor objects.

        This method establishes a connection to the database using psycopg2, and returns a tuple
        containing the connection and cursor objects. If an error occurs during the
        connection process, it logs an error message.

        :param host: The hostname of the database server.
        :type host: str
        :param database: The name of the database to connect to.
        :type database: str
        :param user: The username for authentication.
        :type user: str
        :param password: The password for authentication.
        :type password: str
        :return: A tuple containing the database connection and cursor objects.
        :rtype: tuple[psycopg2.extensions.connection, psycopg2.extensions.cursor]
        """
        try:
            self.conn = psycopg2.connect(
                host=host, database=database, user=user, password=password
            )
            self.cur = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.ERROR(error)

    def show_version(self, cur: psycopg2.extensions.cursor) -> Optional[Tuple]:
        """
        Retrieves the database version information.

        This method establishes a connection to the database using the connect method,
        retrieves the database version information using a cursor, and returns the
        fetched database version.

        :return: The database version information.
        :rtype: tuple or None
        """
        try:
            db_version = cur.fetchone()
            return db_version

        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def close(self):
        """
        Closes the database connection and cursor.

        This method establishes a connection to the database using the connect method,
        and then closes the cursor and connection objects.

        """
        try:
            self.cur.close()
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def apply_script(self, sql_content: str, cur: psycopg2.extensions.cursor):

        try:
            cur.execute(sql_content)
            return cur.fetchall()
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e

    def save_changes(self, conn: psycopg2.extensions.connection):
        """
        Commits the transaction to save changes in the database.

        This method commits the transaction to save any changes made to the database
        using the provided connection object.

        :param conn: The database connection object.
        :type conn: psycopg2.extensions.connection
        """
        try:
            conn.commit()
        except Exception as e:
            self.logger.error(f"Unrecognized error - msg: {e} type: {type(e)}")
            raise e
