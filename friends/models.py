from datetime import date, datetime
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse


class Friends(models.Model):

    friend_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend_mobile = models.CharField(max_length=13) #12자리만 받으려면 어떻게 해야하지?
    Agroup = "Agroup"
    Bgroup = "Bgroup"
    Cgroup = "Cgroup"
    Dgroup = "Dgroup"
    GRADE = (
        (Agroup, "A-Group"),
        (Bgroup, "B-Group"),
        (Cgroup, "C-Group"),
        (Dgroup, "D-Group"),
    )
    friend_group = models.CharField(max_length=10, choices=GRADE, default=Bgroup)
    Friend = "Friend"
    Business = "Business"
    Family = "Family"
    Another = "Another"
    RELATIONSHIP = (
        (Friend, "Friend"),
        (Business, "Business"),
        (Family, "Family"),
        (Another, "Another")
    )
    friend_relation = models.CharField(max_length=10, choices=RELATIONSHIP, default=Business)
    latest_connect = models.DateField(default=date.today)
    friend_memo = models.CharField(max_length=500)
    scheduled_connect = models.DateField(blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.friend_group == "Agroup":
            self.scheduled_connect = self.latest_connect + datetime.timedelta(days=30)
        elif self.friend_group == "Bgroup":
            self.scheduled_connect = self.latest_connect + datetime.timedelta(days=60)
        elif self.friend_group == "Cgroup":
            self.scheduled_connect = self.latest_connect + datetime.timedelta(days=90)
        elif self.friend_group == "Dgroup":
            self.scheduled_connect = self.latest_connect + datetime.timedelta(days=120)
        # 메서드를  override할 때는 꼭 super 클래스의 메서드도 호출한다.
        # super 클래스의 메서드를 호출 하려면 super(현재클래스, self).메서드()
        super(Friends,self).save(force_insert,force_update,using,update_fields)


    def updateconnect(request, id):
        print(id)
        model = Friends.objects.get(pk=id)
        model.latest_connect = date.today()
        if model.friend_group == "Agroup":
            model.scheduled_connect = model.latest_connect + datetime.timedelta(days=30)
        elif model.friend_group == "Bgroup":
            model.scheduled_connect = model.latest_connect + datetime.timedelta(days=60)
        elif model.friend_group == "Cgroup":
            model.scheduled_connect = model.latest_connect + datetime.timedelta(days=90)
        elif model.friend_group == "Dgroup":
            model.scheduled_connect = model.latest_connect + datetime.timedelta(days=120)
        super(Friends,model).save()
        return JsonResponse({"latest_connect":model.latest_connect, "scheduled_connect":model.scheduled_connect})


class Comment(models.Model):
    friend = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='friend')
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=300)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Comment, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['-comment_created']
