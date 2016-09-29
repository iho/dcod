import csv
import os.path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from countries.models import Country, Region


class Command(BaseCommand):
    help = 'Load data from CSV'
    countries_counter = 0

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str)

    def handle(self, *args, **options):

        full_path = os.path.join(settings.BASE_DIR, options['path'])

        if not os.path.isfile(full_path):
            print('File {} does not exist!'.format(full_path))
            return
        with open(full_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip csv headers
            for row in reader:
                self._process_row(row)
        print('{} countries loaded.'.format(self.countries_counter))

    def _process_row(self, row):
        region_name, country_name, value = row
        country, _ = Country.objects.get_or_create(name=country_name)
        region, created = Region.objects.get_or_create(name=region_name)
        if created:
            region.save()
        country.region = region
        country.value = value
        country.save()

        self.countries_counter += 1
