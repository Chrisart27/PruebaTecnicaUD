from django.contrib import admin
from CodingChallengeApp.models import Result


class ResultAdmin(admin.ModelAdmin):
    readonly_fields = ['first', 'second', 'third', 'first_count', 'second_count',
                       'third_count', 'created_at', 'error_msg', 'success', 'input']

admin.site.register(Result, ResultAdmin)
