from django.contrib import admin
from .models import Card, Relationship


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'card_id',
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


admin.site.register(Card, CardAdmin)
admin.site.register(Relationship, RelationshipAdmin)
