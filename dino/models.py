import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):  # noqa: DJ10,DJ11
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"Question: {self.question_text}"

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):  # noqa: DJ10,DJ11
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Choice text: {self.choice_text}, votes: {self.votes}"
