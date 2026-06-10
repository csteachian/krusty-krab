# Krusty Krab Table Booking System

import sqlite3
import sys

def main():
    db_path = sys.argv[1] if len(sys.argv) > 1 else "krustykrab.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query1 = """SELECT"""

    try:
        cursor.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table', 'view') ORDER BY name;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
