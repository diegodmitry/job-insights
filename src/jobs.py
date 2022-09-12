from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as csv_file:
        list_of_dicts = list(csv.DictReader(csv_file))
        return list_of_dicts
