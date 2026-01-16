import sqlite3

# ---------------- CONNECT TO DATABASE ----------------
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# ---------------- CREATE TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

# ---------------- INSERT DATA ----------------
cursor.execute("""
INSERT INTO jobs (company, role, status)
VALUES (?, ?, ?)
""", ("Google", "Backend Engineer", "Applied"))

cursor.execute("""
INSERT INTO jobs (company, role, status)
VALUES (?, ?, ?)
""", ("Amazon", "SDE", "Interview"))

# Mini Task
cursor.execute("""
INSERT INTO jobs(company,role,status)
VALUES (?,?,?)
""",("Apple","UI&UX","Selected"))

# ---------------- READ DATA ----------------
cursor.execute("SELECT * FROM jobs")
rows = cursor.fetchall()

print("📌 Job Records:")
for row in rows:
    print(row)

# Mini Task
cursor.execute("SELECT company,status FROM jobs")
process = cursor.fetchall()

print("📌 Company and Status:")
for row in process:
    print(row)

# ---------------- COMMIT & CLOSE ----------------
conn.commit()
conn.close()
