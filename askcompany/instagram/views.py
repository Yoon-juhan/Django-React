
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Post

# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()


# @login_required
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
# post_detail = DetailView.as_view(model=Post, queryset=Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post
    # queryset=Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)