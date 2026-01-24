# Day 26 – Password Hashing

## Why password hashing is critical
Passwords must NEVER be stored in plain text.

If a database is leaked:
- Plain passwords → all user accounts compromised
- Hashed passwords → still protected

This is a basic security expectation in all backend interviews.

---

## What is hashing?
Hashing converts a password into a fixed-length string.
- One-way process
- Cannot be reversed
- Same input → same hash (with same salt)

Example:
password123 → $2b$12$X9...

---

## Hashing vs Encryption
- Hashing ❌ cannot be reversed
- Encryption ✅ can be reversed with a key

Passwords should be HASHED, not encrypted.

---

## What is salting?
Salting adds random data before hashing.
- Prevents rainbow table attacks
- Ensures same passwords produce different hashes

bcrypt handles salting automatically.

---

## Why bcrypt?
bcrypt is:
- Slow (intentionally)
- Resistant to brute force attacks
- Industry standard for passwords

---

## Backend rule (INTERVIEW GOLD)
Never:
- Store raw passwords
- Compare passwords directly

Always:
- Hash on registration
- Verify hash on login

---

## What I learned today
- Why passwords must be hashed
- Difference between hashing and encryption
- How bcrypt secures passwords
- How backend systems store credentials safely
