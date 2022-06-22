from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    class Meta:
        ordering = ['id']

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(CustomUser, related_name='voter_question', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_question')
    view_count = models.IntegerField(null=True, blank=True, default=0)
    notice = models.BooleanField(default=False)  # 공지사항 여부

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('pybo:question_detail', args=[self.id])

    def get_recent_comments(self):
        return self.comment_set.all().order_by('-create_date')[:5]

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부

    def __str__(self):
        return self.name

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

