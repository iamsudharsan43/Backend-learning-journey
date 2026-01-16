# Day 18 – SQLite vs PostgreSQL

## Why this comparison matters
Almost every backend interview asks:
“Which database would you use and why?”

Knowing the trade-offs is more important than syntax.

---

## SQLite – What it is
SQLite is a lightweight, file-based database.

### Characteristics
- Database stored in a single file
- No server process
- Zero configuration
- Built into Python

### Where SQLite is used
- Learning & practice
- Small applications
- Prototypes
- Mobile apps
- Local tools

### Pros
- Very easy to use
- No setup required
- Fast for small data
- Perfect for beginners

### Cons
- Not good for high traffic
- Limited concurrency
- Not suitable for large-scale apps
- No advanced user/role management

---

## PostgreSQL – What it is
PostgreSQL is a powerful, server-based relational database.

### Characteristics
- Runs as a separate server
- Supports multiple users
- Handles concurrent requests
- Highly scalable

### Where PostgreSQL is used
- Production backend systems
- Web applications
- Financial systems
- SaaS platforms

### Pros
- Strong data integrity
- High concurrency
- Advanced indexing
- JSON support
- Excellent performance at scale

### Cons
- Requires setup
- More complex than SQLite
- Slight learning curve

---

## Key differences (INTERVIEW GOLD)

| Feature | SQLite | PostgreSQL |
|------|-------|-----------|
| Type | File-based | Server-based |
| Setup | None | Required |
| Concurrency | Limited | Excellent |
| Scale | Small | Large |
| Production use | Rare | Very common |

---

## Backend decision rule
- Learning / local → SQLite
- Production / scalable → PostgreSQL

---

## What I learned today
- Why SQLite is used for learning
- Why PostgreSQL is used in production
- How backend DB choices affect scalability
