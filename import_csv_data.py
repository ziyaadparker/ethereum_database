import csv
import sys
import os
import django

project_dir = '~/Documents/projects/github/ethereum_database'
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ethereum_database.settings'

django.setup()

from front_app.models import EthereumKeys

path_to_file = 'eth_prvt_keys.csv'

with open(path_to_file, 'r') as f:

    for line in f.readlines():
        line = line.replace("\n", "")
        line = line.replace('"', '')

        line = line.split(',')

        print(line[0])
        print(line[1])

        h = EthereumKeys()

        h.public_key = line[0]
        h.private_key = line[1]
        h.save()
