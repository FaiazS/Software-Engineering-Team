from fastapi import FastAPI
from user_service import the_app as user_service_app
from video_service import the_app as video_service_app
from editing_service import the_app as editing_service_app
from notification_service import notification_service as notification_service_app
from integration_service import the_app as integration_service_app

app = FastAPI()

app.mount('/api/users', user_service_app)
app.mount('/api/videos', video_service_app)
app.mount('/api/videos', editing_service_app)
app.mount('/api/notifications', notification_service_app)
app.mount('/api/integration', integration_service_app)

@app.get('/')
def read_root():
    return {'msg': 'Welcome to the Video Streaming Platform API'}