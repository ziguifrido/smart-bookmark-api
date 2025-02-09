from fastapi import FastAPI
import util.version as version
from controllers.bookmark_controller import router as bookmark_router

app = FastAPI()
app.include_router(bookmark_router)

@app.get('/version')
async def root():
  return {'version': version.get_version()}
