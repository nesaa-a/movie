from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
  def hash_pwd(password: str) -> str:
    """Returns the hashed password"""
    return pwd_context.hash(password)

  def verify(plain_pwd: str, hashed_pwd: str) -> bool:
    """Checks if the entered password is the same as the one in the database"""
    return pwd_context.verify(plain_pwd, hashed_pwd)