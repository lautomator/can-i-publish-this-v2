from django.contrib import admin
from .models import Card, Relationship, Metric


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'card_slug',
        'card_type',
        'can_publish_status'
    )


class RelationshipAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'choice_one_next',
        'choice_two_next',
        'choice_back'
    )


class MetricAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'card_choice_one',
        'card_choice_two'
    )


admin.site.register(Card, CardAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Metric, MetricAdmin)
