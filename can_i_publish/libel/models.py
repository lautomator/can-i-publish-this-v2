from django.db import models


class Card(models.Model):
    card_id = models.CharField(max_length=4, null=True)
    card_text = models.TextField(null=True)
    continuation_card = models.BooleanField(default=False)
    end_card = models.BooleanField(default=False)

    def __str__(self):
        return self.card_id


class Relationship(models.Model):
    c_id = models.ForeignKey(Card, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.q_id.card_id + ' rel'
