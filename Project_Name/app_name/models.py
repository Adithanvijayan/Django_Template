from django.db import models
import uuid

# Create your models here.
class table_name(models.Model):
    unique_id = models.UUIDField(primary_key=True, null=False , default=uuid.uuid4, editable=False)
    integer_field = models.IntegerField()
    char_field = models.CharField(max_length = 50, null=False)
    textarea_field = models.TextField()
    def __str__(self):
        return '{}'.format(self.integer_field)  