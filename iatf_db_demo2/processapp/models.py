from django.db import models


class Process(models.Model):

    # ToDo Primary Key

    step_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    responsible = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    evidence = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
