import os
import sqlite3


class DataBaseController:
    def __init__(self, dbase_file_name: str):
        app_file_path = os.path.join(os.path.dirname(__file__), dbase_file_name)
        self.app_db = sqlite3.connect(app_file_path)
        self.app_cursor = self.app_db.cursor()

    def close(self):
        self.app_db.close()

    def create_scores_table(self):
        """
        Creates the Scores table, if it doesn't exist yet
        """
        self.app_cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Scores (
                    name TEXT,
                    score INTEGER
                )
            """
        )
        self.app_db.commit()

    def add_score(self, name, score):
        """
        Saves a player's initials and score
        """
        self.app_cursor.execute(
            """
                INSERT INTO Scores (name, score)
                VALUES (:name, :score)
            """,
            {'name': name, 'score': score}
        )
        self.app_db.commit()

    def get_top_scores(self, count):
        """
        Returns the highest scores, best first
        """
        self.app_cursor.execute(
            """
                SELECT name, score
                FROM Scores
                ORDER BY score DESC
                LIMIT :count
            """,
            {'count': count}
        )
        return self.app_cursor.fetchall()
