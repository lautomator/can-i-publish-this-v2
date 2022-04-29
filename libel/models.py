from django.db import models


class Card(models.Model):
    card_slug = models.CharField("Card Slug", max_length=4, null=True)
    card_text = models.TextField("Card Content", null=True)

    CARD_TYPE_CHOICES = (
        ('q', 'Question'),
        ('c', 'Continuation'),
        ('e', 'End Card')
    )

    card_type = models.CharField(
        "Card Type",
        max_length=1,
        choices=CARD_TYPE_CHOICES,
        default='q'
    )

    PUBLISH_CHOICES = (
        ('yes', 'Can Publish'),
        ('no', 'Pause')
    )

    can_publish_status = models.CharField(
        "Can Publish Status",
        max_length=3,
        choices=PUBLISH_CHOICES,
        blank=True,
        null=True
    )

    choice_one = models.CharField("Choice 1", max_length=144, blank=True, default="yes")
    choice_two = models.CharField("Choice 2", max_length=144, blank=True, default="no")

    def __str__(self):
        return self.card_slug


class Relationship(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    choice_one_next = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name="+",
        blank=True,
        null=True
    )
    choice_two_next = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name="+",
        blank=True,
        null=True
    )
    choice_back = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name="+",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.card.card_slug + ' rel'


class Metric(models.Model):
    card_slug = models.CharField("Card Slug", max_length=4, null=True)
    card_choice_one = models.IntegerField("Choice 1", default=0)
    card_choice_two = models.IntegerField("Choice 2", default=0)

    def __str__(self):
        return self.card_slug
