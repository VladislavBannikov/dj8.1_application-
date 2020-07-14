import csv

from django.shortcuts import render

from .models import Columns, FilePath



def table_view(request):
    csv_filename = FilePath.get_path()  # TODO: check if Null or False
    columns = Columns.objects.all().order_by("order_number").values("name", "width")

    template = "table.html"
    with open(csv_filename, "rt") as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=";")
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {
                    header.get(idx) or "col{:03d}".format(idx): value
                    for idx, value in enumerate(table_row)
                }
                table.append(row)

        context = {"columns": columns, "table": table, "csv_file": csv_filename}
        result = render(request, template, context)
    return result
