from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Link(models.Model):
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="user_links",
                               )
    url = models.URLField()
    short_url = models.CharField(max_length=10)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['-pub_date']
