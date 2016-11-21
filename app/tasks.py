import datetime
from celery import Task
from PIL import Image


class ImageResizeTask(Task):
    def __init__(self):
        self.ignore_result = True

    def run(self, obj):
        img = Image.open(obj.image)
        img = img.resize((img.size[0]/2, img.size[1]/2), Image.ANTIALIAS)
        obj.image = img
        obj.time_of_end_converting_job = datetime.datetime.now()
        obj.save()


