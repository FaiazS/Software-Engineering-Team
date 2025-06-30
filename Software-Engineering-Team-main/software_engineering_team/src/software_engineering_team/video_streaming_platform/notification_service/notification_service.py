from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Notification(BaseModel):
    user_id: str
    message: str

class Observer:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, notification: Notification):
        for observer in self.observers:
            observer(notification)

notification_service = FastAPI()

notifications = Observer()

@notification_service.post('/api/notifications')
def send_notification(notification: Notification):
    notifications.notify_observers(notification)
    return {'msg': 'Notification sent'}