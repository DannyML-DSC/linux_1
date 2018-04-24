
# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Scrumyuser(models.Model):
    Name = models.CharField(max_length=200)
    email = models.CharField(max_length=20)
    Owner = models.CharField(name='Owner', max_length=200, default='Owner' )
    admin = models.CharField(name='Admin', max_length=200,default='Admin')
    QA =models.CharField(name='QA', max_length=200,default='QA')
    Developer = models.CharField(name='Developer', max_length=200,default='Developer')

    class Meta:

        verbose_name = 'Scrumyuser'
    def __str__(self):
        return self.Name, self.email, self.Owner,self.QA,self.Developer





class Scrumystatus(models.Model):
    STATUS = {
        ('WT', 'weekly Task'),
        ('DT', 'daily task'),
        ('V', 'Verified'),
        ('D', 'Done'),


    }
    status = models.CharField(max_length=50, choices=STATUS, primary_key=1)

    class Meta:
        verbose_name_plural = 'Scrumystatus'
    def __str__(self):
        return self.status


class ScrummyGoals(models.Model):
    danny = models.ForeignKey(Scrumyuser, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Scrumystatus, on_delete=models.CASCADE)
    task = models.TextField()
    task_id = models.IntegerField(default=700, null=False)
    time_of_status_change = models.DateTimeField(default=datetime.now)
    moved_by = models.CharField(max_length=50, default="not moved yet")
    created_by = models.CharField(max_length=50, null=False)
    movement_track = models.IntegerField(default=1234, null=False)

    def get_absolute_url(self):
         return reversed('dannyscrumy:home')

    class Meta:
        verbose_name_plural = 'ScrumyGoals'
    def __str__(self):
        return self.task


class GoalStatus(models.Model):
    status= {

        ('WT', 'weekly Target'),
        ('DT', 'daily target'),
        ('V', 'Verified'),
        ('D', 'Done'),

    }
    recent_goal = models.ManyToOneRel('ScrummyGoals', on_delete=models.CASCADE, field_name='goals', to=ScrummyGoals)
    # weekly_target = models.OneToOneField('ScrummyGoals', on_delete=models.CASCADE, unique=True)
    daily_target = models.OneToOneField('ScrummyGoals', on_delete=models.CASCADE, unique=True)

    class Meta:
        verbose_name_plural='GoalStatus'
    verify = models.CharField(max_length=200, default="verified")





