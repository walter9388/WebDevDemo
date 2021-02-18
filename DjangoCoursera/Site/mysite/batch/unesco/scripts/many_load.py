import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import *


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Category.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso

    for row in reader:
        print(row[0])

        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        s, created = State.objects.get_or_create(name=row[8], region=r)
        c, created = Category.objects.get_or_create(name=row[7])

        try:
            y=int(row[3])
        except:
            y = None

        try:
            a = float(row[6])
        except:
            a = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            long = float(row[4])
        except:
            long = None

        ss=Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=long,latitude=lat,area_hectares=a,category=c,state=s,iso=i)
        ss.save()

