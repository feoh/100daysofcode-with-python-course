import csv
from pprint import pprint

def fix_int_fields(row_to_fix):
    int_fields = ['beer_servings','spirit_servings','wine_servings']
    for int_field in int_fields:
        row_to_fix[int_field] = int(row_to_fix[int_field])

    return row_to_fix


if __name__ == '__main__':
    row = {}
    all_rows = []
    with open("drinks.csv") as drinks:
        for row in csv.DictReader(drinks):
            all_rows.append(fix_int_fields(row))

    pprint(all_rows)

