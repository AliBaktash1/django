from django.db import models


# Create your models here.
class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255)
    @property
    def short_name(self):
        return self.full_name[:3]


class Book(models.Model):
    title = models.TextField(db_index=True)
    author = models.ForeignKey(
        to="library.Author",
        on_delete=models.CASCADE,
        related_name="books",
    )


    likes = models.PositiveIntegerField(default=0)