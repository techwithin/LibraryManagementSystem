from django.db import models
import datetime
# Create your models here.

class Books(models.Model):
    acc_no = models.IntegerField(default = 0, null = False, primary_key = True)
    book_name = models.CharField(default = "", max_length = 500)
    authorname =  models.CharField(default = "", max_length = 500)
    authorsmark = models.CharField(default = "", max_length = 10)
    subject = models.CharField(default = "", max_length = 50)
    copy_no = models.IntegerField(default = 0, null = False)
    user_id = models.CharField(default = "", null = False, max_length = 50)
    publisher_name = models.CharField(max_length = 200, default = "")
    # date_of_pub = models.DateField(default=datetime.datetime.now().year)
    # date_of_acc = models.DateField(default=datetime.datetime.now().year)
    source = models.CharField(default = "", null = False, max_length = 50)
    bill_no = models.CharField(default = "", null = False, max_length = 50)
    # date_of_bill = models.DateField(default=datetime.datetime.now().year)
    price = models.IntegerField(default = 0, null = False)
    cd = models.BooleanField(default = False)

    def __int__(self):
      return self.acc_no


