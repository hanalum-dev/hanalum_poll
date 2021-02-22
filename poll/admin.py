from django.contrib import admin

from .models import Poll, Option, Vote

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'content',
        'created_at',
        'updated_at',
    ]


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'status',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'title',
        'status',
        'created_at',
        'updated_at',
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'poll',
        'option',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'name',
        'poll',
        'option',
        'created_at',
        'updated_at',
    ]
