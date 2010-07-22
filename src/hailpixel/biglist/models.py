from django.db import models

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    task = models.CharField(max_length = 500)
    due = models.DateTimeField(blank = True, null = True)
    done = models.BooleanField(default = False)
    
    def __unicode__(self):
        return '(%s) %s' % (self.done and 'done' or 'not done', self.task)
