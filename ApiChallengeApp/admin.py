from django.contrib import admin
from ApiChallengeApp.models import UserSelection


class UserSelectionAdmin(admin.ModelAdmin):
    readonly_fields = ['candidates', 'fk_politic', 'created_at']

admin.site.register(UserSelection, UserSelectionAdmin)
