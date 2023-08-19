from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# Register your models here.

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag','message', 'message_length', 'created_at', 'updated_at', 'is_public']
    list_display_links = ['message'] # 메세지 열에 링크
    list_filter = ['created_at', 'is_public'] # 필터링
    search_fields = ['message'] # 메세지 내용으로 검색할 수 있는 검색창

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 75px;"/>')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"
    

@admin.register(Comment) # Wrapping
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass