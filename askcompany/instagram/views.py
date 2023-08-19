from django.views.generic import ListView, DetailView
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

post_list = ListView.as_view(model=Post)

# def  post_list(request):
#     qs = Post.objects.all()     # 전부 가져옴
#     q = request.GET.get('q', '')    # 

#     if q:   # q 라는 검색어가 있다면 
#         qs = qs.filter(message__icontains=q) # q 가 포함된 내용을 조회
#     # instagram/templates/instagram/post_list.html 경로
#     return render(request, 'instagram/post_list.html', {
#         'post_list' : qs, # html 파일에서 참조하는 이름 'post_list'
#         'q' : q, 
#     })


# FBV 함수 기반 뷰
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)   # 매칭되는 pk 값이 없을 때 404를 띄운다.
    
#     return render(request, 'instagram/post_detail.html', {
#         'post' : post,
#     })

# CBV 클래스 기반 뷰
post_detail = DetailView.as_view(model=Post)


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")