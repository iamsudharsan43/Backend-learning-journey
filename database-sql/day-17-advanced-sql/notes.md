# Day 17 – Advanced SQL

## Why advanced SQL matters
Real applications never fetch all data.
They:
- Filter rows
- Sort results
- Update records
- Delete records safely

## WHERE clause
Used to filter rows.

Example:
SELECT * FROM jobs WHERE status = 'Applied';

## ORDER BY
Used to sort results.

Example:
SELECT * FROM jobs ORDER BY company ASC;

ASC → ascending
DESC → descending

## UPDATE
Used to modify existing records.

Example:
UPDATE jobs SET status = 'Selected' WHERE id = 1;

⚠️ Always use WHERE with UPDATE.

## DELETE
Used to remove records.

Example:
DELETE FROM jobs WHERE id = 3;

⚠️ DELETE without WHERE deletes ALL rows.

## Backend mindset
- Never trust default queries
- Always filter intentionally
- Be careful with UPDATE & DELETE

## What I learned today
- How to filter data using WHERE
- How to sort results using ORDER BY
- How to update and delete records safely
