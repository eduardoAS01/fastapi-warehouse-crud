from fastapi import FastAPI
from routers.client import router as client_router
#from auth.router import router as login_router


app = FastAPI()

app.include_router(client_router)