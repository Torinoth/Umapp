from django.contrib import admin
from .models import UmaGirl


class UmaGirlAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = (
            'name', 'nameEN', 'birthday', 'height', 'weight', 'breast', 'waist', 'hip', 'icon',
            'draftImage', 'memo', 'slug')
        return self.changeform_view(request, object_id, form_url, extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        self.readonly_fields = ('slug',)
        return self.changeform_view(request, None, form_url, extra_context)


admin.site.register(UmaGirl, UmaGirlAdmin)
