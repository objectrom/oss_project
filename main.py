from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from name import name_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5501", "http://3.224.168.79", "http://44.223.123.230"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "hello world"
    }

app.include_router(name_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)