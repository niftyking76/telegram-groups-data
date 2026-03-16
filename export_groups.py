import psycopg2
import json

DB_URL = "postgresql://neondb_owner:npg_O8yn7oWlKCZM@ep-shy-brook-a109nwqt-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# change table name if needed
cur.execute("SELECT * FROM groups")

columns = [desc[0] for desc in cur.description]

rows = cur.fetchall()

groups = []

for row in rows:
    record = {}
    for col, val in zip(columns, row):
        record[col] = val
    groups.append(record)

# save json
with open("groups.json", "w", encoding="utf-8") as f:
    json.dump(groups, f, ensure_ascii=False, indent=2)

print(f"Exported {len(groups)} groups to groups.json")

cur.close()
conn.close()
