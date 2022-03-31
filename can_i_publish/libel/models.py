from django.db import models


class Question(models.Model):
    question_id = models.CharField(max_length=4, default="")
    question_text = models.TextField( default="")

    def __str__(self):
        return self.question_id


class Choice(models.Model):
    question = models.ManyToManyField(Question)
    choice_text = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.choice_text



"""
Questions
Answers that lead to other questions and endpoints

DB: need to store the questions and answers (all are static). There
are several answer choices for each question

Question
id | q_text

Choice
question (q_text) one to one rel | choice 

the logic map will be an iterable dictionary not stored in the DB

You need to be able to map choices to certain questions. Most of them are 'yes' and 'no' but some of them are not.

"""