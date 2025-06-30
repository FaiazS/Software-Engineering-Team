from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

videos = []

the_app = FastAPI()

class Video(BaseModel):
    id: int
    title: str
    content: str
    user_id: str
    likes: int = 0
    dislikes: int = 0
    comments: List[str] = []

@the_app.post('/api/videos/upload')
def upload_video(video: Video):
    if any(v.id == video.id for v in videos):
        raise HTTPException(status_code=400, detail='Video with this ID already exists')
    videos.append(video)
    return {'msg': 'Video uploaded successfully'}

@the_app.get('/api/videos/{id}')
def get_video(id: int):
    video = next((v for v in videos if v.id == id), None)
    if video is None:
        raise HTTPException(status_code=404, detail='Video not found')
    return video

@the_app.post('/api/videos/{id}/like')
def like_video(id: int):
    video = next((v for v in videos if v.id == id), None)
    if video is None:
        raise HTTPException(status_code=404, detail='Video not found')
    video.likes += 1
    return {'msg': 'Video liked'}

@the_app.post('/api/videos/{id}/dislike')
def dislike_video(id: int):
    video = next((v for v in videos if v.id == id), None)
    if video is None:
        raise HTTPException(status_code=404, detail='Video not found')
    video.dislikes += 1
    return {'msg': 'Video disliked'}

@the_app.post('/api/videos/{id}/comments')
def add_comment(id: int, comment: str):
    video = next((v for v in videos if v.id == id), None)
    if video is None:
        raise HTTPException(status_code=404, detail='Video not found')
    video.comments.append(comment)
    return {'msg': 'Comment added'}