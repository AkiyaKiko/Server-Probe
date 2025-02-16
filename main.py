from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from utils.sys_stat import get_system_info

app = FastAPI()


@app.get("/status")
async def get_status():
    stat = await get_system_info()
    return JSONResponse(content=stat)

# 静态文件
app.mount("/", StaticFiles(directory="front-end", html=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
