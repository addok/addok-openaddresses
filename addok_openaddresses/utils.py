import csv
from progressist import ProgressBar

from addok.config import config


def group_addresses(rows):
    ADDRESSES = {}
    bar = ProgressBar(throttle=10000, template='Grouping addresses… {done}')
    for row in csv.DictReader(rows):
        if not row.get('STREET'):
            print('\rFiltering out street without name', row)
            continue
        if row['STREET'] not in ADDRESSES:
            row['housenumbers'] = {}
            row['id'] = 'street-{}'.format(row['ID'])
            row['lat'] = row['LAT']
            row['lon'] = row['LON']
            row.update(config.OPENADDRESSES_EXTRA)
            ADDRESSES[row['STREET']] = row
        ADDRESSES[row['STREET']]['housenumbers'][row['NUMBER']] = {
            'lat': row['LAT'],
            'lon': row['LON'],
            'id': row['ID'],
        }
        bar.update()

    for address in ADDRESSES.values():
        yield address


def make_labels(helper, result):
    if not result.labels:
        # FIXME: move to a US dedicated plugin instead.
        result.labels = result._rawattr('STREET')[:]
        label = result.labels[0]
        unit = getattr(result, 'UNIT', None)
        if unit:
            label = '{} {}'.format(label, unit)
        city = getattr(result, 'CITY', None)
        if city and city != label:
            label = '{} {}'.format(label, city)
            postcode = getattr(result, 'POSTCODE', None)
            if postcode:
                label = '{} {}'.format(label, postcode)
            result.labels.insert(0, label)
        housenumber = getattr(result, 'housenumber', None)
        if housenumber:
            label = '{} {}'.format(housenumber, label)
            result.labels.insert(0, label)
