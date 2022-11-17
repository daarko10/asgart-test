import uvicorn
from fastapi_offline import FastAPIOffline

app = FastAPIOffline()


@app.get('/')
def route():
    return {"message": "test"}


@app.get('/saadon')
def route2():
    return 'Saadon is gay'


@app.get('/dago')
def route2():
    return 'dago asdfsdfis the worst ever'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
