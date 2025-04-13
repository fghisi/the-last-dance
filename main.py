from fastapi import FastAPI

from user_api.main import app as user_api


app = FastAPI()
app.mount("/user-api", user_api)
