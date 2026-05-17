from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    description=models.TextField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='borrows')
    book=models.ForeignKey(Book,on_delete=models.CASCADE, related_name='borrows')
    borrowed_at=models.DateTimeField(auto_now=True)
    returned=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
