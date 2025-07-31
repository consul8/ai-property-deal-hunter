import os
import sqlite3
import pandas as pd

def get_listings():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data.db")
    if not os.path.exists(db_path):
        raise FileNotFoundError("Database file data.db not found.")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM listings", conn)
    conn.close()
    return df