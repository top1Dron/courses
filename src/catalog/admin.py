from django.contrib import admin
from catalog.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lections_quantity')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Course, CourseAdmin)