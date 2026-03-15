```python
from django.db import models

# Question model
class Question(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return "Question: " + self.content

    # Check if the selected answers are correct
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True)
        all_answer_ids = [answer.id for answer in all_answers]
        return set(all_answer_ids) == set(selected_ids)


# Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return "Choice: " + self.content


# Submission model
class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id}"
```
