from django.contrib import admin
from .models import Blog  # ← 여기서 점(.) 꼭 붙여주세요!

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    ...
