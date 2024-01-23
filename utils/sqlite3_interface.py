from flask import g
import sqlite3


class Sqlite3Interface:
    """Pythonic and also the flask way to use sqlite3 inside flask."""

    def __init__(self, app, db_path):
        self.app = app
        self.db_path = db_path

        app.teardown_appcontext(self._close_connection)

    def _get_db(self):
        """Getting db from the global object "g", create one if not exists.

        Returns:
            db: Connection
        """
        db = getattr(g, "_database", None)

        if db is None:
            db = g._database = sqlite3.connect(self.db_path)

        return db

    def _close_connection(self, exception):
        """Close sqlite3 connection on teardown.

        Args:
            exception (Exception): Raise exception if there's one.
        """
        db = getattr(g, "_database", None)

        if db is not None:
            db.commit()
            db.close()

    def exec_query(self, query, args=()):
        """Executing a SQL query to the database.

        Args:
            query (str): The query string.
            args (tuple): Iterable arguments.

        Returns:
            Cursor: The cursor object.
        """
        db = self._get_db()
        cur = db.cursor()
        results = cur.execute(query, args)

        return results
