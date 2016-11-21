from django.db import models
from app.tasks import ImageResizeTask


class Image(models.Model):
    image = models.ImageField(upload_to='images', max_length=255)
    getting_time = models.DateTimeField(auto_created=True)
    time_of_end_converting_job = models.DateTimeField(default=None, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Image, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                update_fields=update_fields)
        # run celery task to resize image
        ImageResizeTask().delay(self)
