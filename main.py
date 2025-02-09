from fastapi import FastAPI
from controllers.bookmark_controller import router as bookmark_router

app = FastAPI()
app.include_router(bookmark_router)

@app.get('/')
async def root():
  return {'message': 'Hello World'}
