from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError


class ScopeFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            scope = form.data
            count = 0
            for item in scope.values():
                if 'on' in item and count != 2:
                    count += 1
                elif count > 1:
                    raise ValidationError('Основным может быть только один раздел')
            if count == 0:
                raise ValidationError('Выберите основной раздел')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
