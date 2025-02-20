from django.contrib import admin

# Register your models here.

from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    list_filter = ("first_name", "last_name", "email", "date", "occupation")
    ordering = ("-first_name",)
    readonly_fields = ("first_name", "last_name", "email", "date", "occupation")


admin.site.register(Form, FormAdmin)
