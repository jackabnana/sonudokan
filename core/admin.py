from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from .models import Ad, AdPlacement
from django_summernote.admin import SummernoteModelAdmin
from djsingleton.admin import SingletonAdmin



@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass


@admin.register(AdPlacement)
class AdPlacementAdmin(SingletonAdmin):
    pass


class FlatPageAdmin(FlatPageAdmin, SummernoteModelAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'registration_required',
                'template_name',
            ),
        }),
    )
    summernote_fields = ('content',)


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
