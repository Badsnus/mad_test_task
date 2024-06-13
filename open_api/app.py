from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/memes")
async def root():
    return []


@app.get("/memes/{id}")
async def root(id: int):
    return {'id': id}


@app.post("/memes")
async def root(id: int):
    return {}


@app.put("/memes/{id}")
async def root(id: int):
    return {'id': id}


@app.delete("/memes/{id}")
async def root(id: int):
    return {'id': id}
