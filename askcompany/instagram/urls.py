from django.urls import path, re_path, register_converter
from . import views

class Yearconverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)
    
register_converter(Yearconverter, 'year')

app_name = 'instagram' # URL Reverse에서 namespace역할을 하게 된다.

urlpatterns = [
    path('', views.post_list, name='post_list'), # views에 post_list 함수 호출 
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    path('archives/<year:year>/', views.archives_year),
]