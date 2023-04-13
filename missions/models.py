from django.db import models
from multiselectfield import MultiSelectField

class Mission(models.Model):
    LEVEL = [
        (1, "Level1"),
        (2, "Level2"),
        (3, "Level3"),
        (4, "Level4")
    ]
    TAGS = [
        ("exercise", "운동"),
        ("transport", "교통"),
        ("cleaning", "청소"),
        ("diet", "식생활"),
        ("leisure", "여가생활"),
        ("digital", "디지털"),
        ("save", "절약")
    ]
    name = models.CharField(max_length=20)
    level = models.IntegerField(choices=LEVEL)
    description = models.CharField(max_length=100)
    tag = MultiSelectField(choices=TAGS, max_length=20, default="")

    def __str__(self):
        return self.name