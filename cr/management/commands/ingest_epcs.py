import csv
from datetime import date

from django.core.management import BaseCommand

from ...models import EPC, Ward


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("cr/data/2022Q1.csv", "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for r in reader:
                # For now we'll save every ward.
                ward, created = Ward.objects.get_or_create(
                    code=r["Ward Code"], name=r["Ward Name"]
                )
                # but we only care about these epcs
                if r["Ward Code"] == "00QPMM":
                    # print(r["Ward Code"])
                    # breakpoint()
                    # Sometimes the dates are messed up.
                    assessment_date = date.fromisoformat(r["Date of Assessment"])
                    year = assessment_date.year
                    if year < 100:
                        year += 2000
                    if year == 213:
                        year = 2013
                    if year == 1970:
                        year = 2022
                    if year >= 2100:
                        str_year = str(year)
                        fixed_str_year = "201" + str_year[-1]
                        year = int(fixed_str_year)
                    new_date = date(year, assessment_date.month, assessment_date.day)

                    epc = EPC.objects.create(
                        ward=ward,
                        postcode=r["Postcode"],
                        uprn=r["Property_UPRN"],
                        address_1=r["ADDRESS1"],
                        address_2=r["ADDRESS2"],
                        post_town=r["POST_TOWN"],
                        assessment_date=assessment_date,
                        data=r,
                    )
                    print("EPC saved: {}".format(epc))
