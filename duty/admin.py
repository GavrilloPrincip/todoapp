from django.contrib import admin

# Register your models here.

from .models import duty   # '.' şuanki klasördeki models'e git.

@admin.register(duty)
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = duty