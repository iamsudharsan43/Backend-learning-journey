from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ---------------- HASH PASSWORD ----------------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# ---------------- VERIFY PASSWORD ----------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ---------------- DEMO ----------------
if __name__ == "__main__":
    user_password = "mysecret123"

    hashed = hash_password(user_password)
    print("Hashed password:", hashed)

    print("Correct password check:",
          verify_password("mysecret123", hashed))

    print("Wrong password check:",
          verify_password("wrongpass", hashed))
