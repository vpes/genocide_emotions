import csv
import os
import sys

from django.db import transaction



@transaction.atomic
def init(project_path):
    from emotions_website1.models import Country,VisitorQuery
    from emotions_website1.process_query import do_process_query
    id = VisitorQuery.objects.filter(processed__isnull=True).values_list('id',flat=True).first()
    if id is not None:
        do_process_query(id)
    return
    path='{}../data/countries.csv'.format(project_path)
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i,row in enumerate(reader):
            if i == 0:
                continue
            c = Country(name=row[0],
                        alpha2=row[1],
                        code =row[3],
                        region = row[5],
                        subregion = row[6],
                        intermregion =row[7]
                        )
            c.save()
            print(c)

if __name__ == "__main__":
    homePath = os.path.join(os.path.dirname(os.path.abspath(os.path.split(__file__)[0])))
    if homePath in sys.path:
        sys.path.remove(homePath)
    sys.path.insert(0, homePath)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emotions_website1.settings")
    import django

    django.setup()
    init(homePath)