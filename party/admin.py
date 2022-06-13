from django.contrib import admin

# Register your models here.
from party.models import *


class InlineTabularParticipants(admin.TabularInline):
    model = ParticipantsThroughModel
    autocomplete_fields = ('records', )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [InlineTabularParticipants, ]
    exclude = ('created_at', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields = ('amount', 'title', )
