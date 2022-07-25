from django.db import models


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length=50) #verbose_name = "Başlık"
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    article_image = models.FileField(blank=True,null = True,verbose_name = "Add Photograph")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-created_date"]
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name = "Article",related_name = "comments")
    comment_author = models.CharField(max_length= 30,verbose_name="Name")
    comment_content = models.CharField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ["-comment_date"]