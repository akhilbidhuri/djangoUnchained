from django.db import models

#Users Model
class Users(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    real_name = models.CharField(max_length = 50)
    tz = models.CharField(max_length = 50)
    def __str__(self):
        return self.real_name


#Activity Period Model
class ActivityPeriod(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return self.user.real_name