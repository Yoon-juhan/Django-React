from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model): # Post 테이블을 생성
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    title = models.CharField(max_length=100) # 필드명 = 타입
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    