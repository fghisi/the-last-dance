from fastapi import APIRouter

from user_api.controller import user


router = APIRouter()
router.include_router(user.router)
