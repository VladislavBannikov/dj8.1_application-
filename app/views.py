import csv

from django.shortcuts import render


CSV_FILENAME = "phones.csv"
COLUMNS = [
    {"name": "id", "width": 1},
    {"name": "name", "width": 3},
    {"name": "price", "width": 2},
    {"name": "release_date", "width": 2},
    {"name": "lte_exists", "width": 1},
]
