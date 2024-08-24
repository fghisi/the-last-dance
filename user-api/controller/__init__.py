from fastapi import APIRouter

from controller import user


router = APIRouter()
router.include_router(user.router)
