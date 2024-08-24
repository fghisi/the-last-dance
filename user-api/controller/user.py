from fastapi import APIRouter

from starlette.status import HTTP_201_CREATED


router = APIRouter()


@router.post(
    path="/users",
    status_code=HTTP_201_CREATED,
)
def post_users():
    pass
