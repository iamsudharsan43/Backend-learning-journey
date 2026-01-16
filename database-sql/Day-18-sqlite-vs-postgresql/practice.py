print("SQLite vs PostgreSQL – Conceptual Comparison\n")

databases = {
    "SQLite": {
        "type": "File-based",
        "best_for": "Learning & small apps",
        "concurrency": "Low",
        "setup": "None"
    },
    "PostgreSQL": {
        "type": "Server-based",
        "best_for": "Production systems",
        "concurrency": "High",
        "setup": "Required"
    }
}

for db, info in databases.items():
    print(f"🔹 {db}")
    for key, value in info.items():
        print(f"   {key}: {value}")
    print()
