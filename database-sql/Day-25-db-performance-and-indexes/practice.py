import sqlite3

conn = sqlite3.connect("performance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    company TEXT,
    status TEXT
)
""")

# Create index
cursor.execute("CREATE INDEX IF NOT EXISTS idx_status ON jobs(status)")

# Insert sample data
for i in range(1, 101):
    cursor.execute(
        "INSERT INTO jobs (company, status) VALUES (?, ?)",
        (f"Company {i}", "Applied" if i % 2 == 0 else "Interview")
    )

conn.commit()

# Query using index
cursor.execute("SELECT * FROM jobs WHERE status = 'Applied'")
rows = cursor.fetchall()

print(f"Applied jobs count: {len(rows)}")

conn.close()
