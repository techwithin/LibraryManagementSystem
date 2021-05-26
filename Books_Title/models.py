from django.db import models
import datetime
import uuid
# Create your models here.

class Title(models.Model):

    uid = models.IntegerField(default = 0)
    title = models.CharField(default = "", max_length = 500)
    author = models.CharField(default = "", max_length = 100)
    total_book_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Books(models.Model):

    uid = models.ForeignKey(Title, on_delete = models.CASCADE)
    acc_no = models.IntegerField(default = 0)
    student_id = models.CharField(default = "", max_length = 20)
    last_used = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return str(self.acc_no)
 



