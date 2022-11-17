import uvicorn
from fastapi_offline import FastAPIOffline

app = FastAPIOffline()


@app.get('/')
def route():
    return {"message": "test"}


@app.get('/saadon')
def route2():
    return 'Saadon is gay'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
