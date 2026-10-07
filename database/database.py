import json
import sqlite3

from config import DB_PATH
from database.schema import CREATE_ANALYSES_TABLE


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    connection = get_connection()

    try:
        connection.execute(CREATE_ANALYSES_TABLE)
        connection.commit()

    finally:
        connection.close()


def save_analysis(
    file_name: str,
    candidate_name: str,
    resume_score: float,
    skills: list[str],
):

    initialize_database()

    connection = get_connection()

    try:

        connection.execute(
            """
            INSERT INTO analyses
            (
                file_name,
                candidate_name,
                resume_score,
                skills
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                file_name,
                candidate_name,
                resume_score,
                json.dumps(skills),
            ),
        )

        connection.commit()

    finally:
        connection.close()


def get_analysis_history():

    initialize_database()

    connection = get_connection()

    try:

        cursor = connection.execute(
            """
            SELECT
                id,
                file_name,
                candidate_name,
                resume_score,
                skills,
                created_at
            FROM analyses
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        return rows

    finally:
        connection.close()