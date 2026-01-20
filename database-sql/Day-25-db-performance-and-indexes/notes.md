# Day 25 – Database Performance, Indexes & Common Mistakes

## Why database performance matters
A backend may have perfect APIs,
but if DB queries are slow, the entire system is slow.

Database performance directly affects:
- API response time
- User experience
- Server cost

---

## What is an Index?
An index is a data structure that makes queries faster.

Think of it like:
- A book index → jump directly to a topic
- Instead of reading every page

---

## When indexes are used
Indexes help when:
- Searching with WHERE
- Sorting with ORDER BY
- Filtering large tables

Example:
```sql
SELECT * FROM jobs WHERE status = 'Applied';
