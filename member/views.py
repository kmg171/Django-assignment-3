from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def sign_up(request):
    # POST 데이터가 있으면 form에 바인딩, 없으면 빈 form 생성
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # 회원가입 성공하면 로그인 페이지로 리다이렉트
        return redirect(settings.LOGIN_URL)
    return render(request, 'registration/signup.html', {'form': form})
