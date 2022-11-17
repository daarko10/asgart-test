import uvicorn
from fastapi_offline import FastAPIOffline

app = FastAPIOffline()


@app.get('/')
def route():
    return {"message": "test"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
