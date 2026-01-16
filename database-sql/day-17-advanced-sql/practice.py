import sqlite3

# ---------------- CONNECT ----------------
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# ---------------- WHERE ----------------
print("\n📌 Jobs with status = 'Applied'")
cursor.execute(
    "SELECT id, company, role, status FROM jobs WHERE status = ?",
    ("Applied",)
)
applied_jobs = cursor.fetchall()
for job in applied_jobs:
    print(job)

# ---------------- ORDER BY ----------------
print("\n📌 Jobs ordered by company (ASC)")
cursor.execute(
    "SELECT id, company, role, status FROM jobs ORDER BY company ASC"
)
ordered_jobs = cursor.fetchall()
for job in ordered_jobs:
    print(job)

# ---------------- UPDATE ----------------
print("\n📌 Updating job status (id = 1 → Selected)")
cursor.execute(
    "UPDATE jobs SET status = ? WHERE id = ?",
    ("Selected", 1)
)

# ---------------- DELETE ----------------
print("\n📌 Deleting job with id = 2")
cursor.execute(
    "DELETE FROM jobs WHERE id = ?",
    (2,)
)

# ---------------- FINAL STATE ----------------
print("\n📌 Final job table")
cursor.execute("SELECT * FROM jobs")
final_rows = cursor.fetchall()
for row in final_rows:
    print(row)

# Mini Task

print("\n📌 Update Apple status as 'Hired',Delete where status is 'Interview' and order by id in desc ways")
cursor.execute("UPDATE jobs SET status = ? WHERE id = ?",("Hired", 3))
cursor.execute("DELETE FROM jobs WHERE status = ?",("Interview",))
cursor.execute("SELECT * FROM jobs ORDER BY id DESC")
task_1=cursor.fetchall()
for row in task_1:
    print(row)

# ---------------- COMMIT & CLOSE ----------------
conn.commit()
conn.close()
