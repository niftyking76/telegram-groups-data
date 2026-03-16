import psycopg2
import json
import os
from datetime import datetime

DB_URL = os.environ["DB_URL"]

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

cur.execute("SELECT * FROM groups")

columns = [desc[0] for desc in cur.description]
rows = cur.fetchall()

groups = []

for row in rows:
    record = {}

    for col, val in zip(columns, row):

        # convert datetime to string
        if isinstance(val, datetime):
            val = val.isoformat()

        record[col] = val

    groups.append(record)

with open("groups.json", "w", encoding="utf-8") as f:
    json.dump(groups, f, ensure_ascii=False, indent=2)

print(f"Exported {len(groups)} groups")

cur.close()
conn.close()
