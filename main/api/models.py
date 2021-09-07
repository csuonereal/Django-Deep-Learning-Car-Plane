from django.db import models

import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(filename)

class DL_MODEL(models.Model):
    dl_image = models.FileField(blank=True, null=True, verbose_name="Image",upload_to=get_file_path)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date

