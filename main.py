from fastapi import FastAPI
import util.version as version
from controllers.group_controller import router as group_router
from controllers.bookmark_controller import router as bookmark_router

app = FastAPI()
app.include_router(bookmark_router)
app.include_router(group_router)

@app.get('/version')
async def root():
  return {'version': version.get_version()}
