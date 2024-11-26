import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.detect_all import router as location_detect_all_router
from src.routers.backup_and_restore import router as backup_and_restore_router
from dotenv import load_dotenv

load_dotenv()
MAIN_PORT = os.getenv('MAIN_PORT')

app = FastAPI()

# Thêm CORS nếu cần
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(location_detect_all_router, prefix="/api/v1")
app.include_router(backup_and_restore_router, prefix="/api/data")


@app.get('/hello')
async def root():
    return {"message": "Hello - I'm Linkk"}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', MAIN_PORT)))


