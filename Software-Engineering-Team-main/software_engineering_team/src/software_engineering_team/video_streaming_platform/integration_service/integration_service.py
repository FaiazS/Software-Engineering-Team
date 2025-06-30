from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ExternalServiceAdapter:
    def share_to_service(self, video_data, service: str):
        if service == 'YouTube':
            return 'Shared to YouTube'
        elif service == 'Vimeo':
            return 'Shared to Vimeo'
        else:
            raise HTTPException(status_code=400, detail='Unsupported service')

the_app = FastAPI()

class ShareRequest(BaseModel):
    video_id: int
    service: str

@the_app.post('/api/integration/share')
def share_video(request: ShareRequest):
    video_data = 'video_data'  # Placeholder: Normally you'd fetch the video from the database
    adapter = ExternalServiceAdapter()
    result = adapter.share_to_service(video_data, request.service)
    return {'msg': result}