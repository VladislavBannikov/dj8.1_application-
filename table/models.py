from django.db import models


# Create your models here.


class Columns(models.Model):
    name = models.CharField(max_length=30, verbose_name="column name")
    width = models.PositiveIntegerField(verbose_name="column width")
    order_number = models.PositiveIntegerField(verbose_name="Order number")

    def __str__(self):
        return self.name


class FilePath(models.Model):
    path = models.CharField(max_length=400)

    @classmethod
    def get_path(cls):
        records = cls.objects.all()
        if records.count() == 1:
            return records[0].path
        elif records.count() > 1:
            raise Exception("One record expected.")
        else:
            return None

    @classmethod
    def set_path(cls, path: str):
        records = cls.objects.all()
        if records.count() == 1:
            rec = records[0]
            rec.path = path
            rec.save()
            return True
        elif records.count() > 1:
            raise Exception("One record expected.")
        else:
            FilePath.objects.create(path=path)
            return True
        pass
