from django.db import models


class Ward(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class EPC(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name="wards")
    postcode = models.CharField(max_length=10)
    uprn = models.CharField(max_length=12)
    address_1 = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500)
    post_town = models.CharField(max_length=500)
    assessment_date = models.DateField()
    data = models.JSONField()

    def __str__(self):
        return "EPC for: {}".format(self.uprn)
