from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router

app = FastAPI(
    title="App"
)

app.include_router(items_router)
app.include_router(users_router)


@app.get('/')
def hello():
    return {
        "message": "Hello",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}"}


