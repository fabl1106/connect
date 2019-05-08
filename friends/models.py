from django.db import models
from django.contrib.auth.models import User

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
    RELATIONSHIP = (
        (Friend, "Friend"),
        (Business, "Business"),
        (Family, "Family"),
    )
    friend_relation = models.CharField(max_length=10, choices=RELATIONSHIP, default=Business)
    friend_memo = models.CharField(max_length=500)
    created = models.DateField(u'Day of the event')

    # def __str__(self):
    #     return "Name: " + self.friend_name +", Group: " + self.friend_group

    # class Meta:
    #     ordering = ["site_name"]


class Comment(models.Model):
    friend = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='friend')
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=300)
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-comment_created']