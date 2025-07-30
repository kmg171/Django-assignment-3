from django.contrib import admin
from django.urls import path, include

from blog import views as blog_views
from member import views as member_views  # member 앱의 views 불러오기

urlpatterns = [
    path('admin/', admin.site.urls),

    # 블로그
    path('', blog_views.blog_list, name='blog_list'),
    path('<int:pk>/', blog_views.blog_detail, name='blog_detail'),

    # 인증 (로그인/로그아웃)
    path('accounts/', include('django.contrib.auth.urls')),

    # 회원가입
    path('signup/', member_views.sign_up, name='signup'),  # signup 경로 직접 연결
]
