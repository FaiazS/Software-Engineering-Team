from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class EditingMethod:
    def apply(self):
        raise NotImplementedError

class Trim(EditingMethod):
    def apply(self, video_content):
        return 'Trimmed video'

class AddFilter(EditingMethod):
    def apply(self, video_content):
        return 'Video with added filter'

class VideoEditor:
    def edit_video(self, method: EditingMethod, video_content):
        return method.apply(video_content)

the_app = FastAPI()

class EditRequest(BaseModel):
    video_id: int
    method: str

@the_app.post('/api/videos/{id}/edit')
def edit_video(id: int, request: EditRequest):
    video_content = 'video_data' # Placeholder: Normally you'd fetch the video from the database
    editor = VideoEditor()
    if request.method == 'trim':
        edited_video = editor.edit_video(Trim(), video_content)
    elif request.method == 'add_filter':
        edited_video = editor.edit_video(AddFilter(), video_content)
    else:
        raise HTTPException(status_code=400, detail='Unknown editing method')
    return {'msg': 'Video edited successfully', 'content': edited_video}