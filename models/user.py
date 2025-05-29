from bson import ObjectId
from core.database import users_collection
from schemas.user import User, UserCreate


async def get_user_by_username(username: str) -> User | None:
    """Get a user by username."""
    user = await users_collection.find_one({"username": username})
    if user:
        return User.model_validate(user)
    return None

async def get_user_by_email(email: str) -> User | None:
    """Get a user by email."""
    user = await users_collection.find_one({"email": email})
    if user:
        return User.model_validate(user)
    return None

async def get_user_by_id(user_id: str) -> User | None:
    """Get a user by id."""
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return User.model_validate(user)
    return None



async def create_user(user: UserCreate) -> User:
    """Create a new user."""
    user_dict = user.model_dump()
    user_dict["password"] = get_password_hash(user_dict[password])