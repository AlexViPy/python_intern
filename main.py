from fastapi import FastAPI, Query
import uvicorn
from app import is_alive_host

app = FastAPI()

@app.get('/health')
async def get_is_alive_host(hostname: str = Query(...)):
    result = is_alive_host(hostname)
    return {'status':'up' if result else 'down'}
        

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port='8001', reload=True)