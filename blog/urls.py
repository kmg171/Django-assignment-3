from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # /blog/ 접속시 blog_list 뷰 실행
]
