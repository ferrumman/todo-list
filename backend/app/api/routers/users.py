from fastapi import APIRouter

from ..domain import user
from ..repository import users

router = APIRouter()
controller = users.get_user_controller()


@router.get("/users/", tags=["users"])
async def read_users():
    # controller = users.get_user_controller()
    controller.login()

    # test.test()
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/users/")
async def create_user(user: user.User):
    controller.sign_up(user)
    return user
