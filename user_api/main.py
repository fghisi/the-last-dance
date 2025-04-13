from fastapi import FastAPI

from user_api.controller import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router=router)
    return application


app = get_application()
