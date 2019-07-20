import csv
from pprint import pprint

def fix_int_fields(row_to_fix):
    int_fields = ['beer_servings','spirit_servings','wine_servings']
    for int_field in int_fields:
        row_to_fix[int_field] = int(row_to_fix[int_field])

    return row_to_fix



def most_beer(drinks_list):
    return sorted(drinks_list, key=lambda r: r['beer_servings'], reverse=True)


if __name__ == '__main__':
    row = {}
    all_rows = []
    with open("drinks.csv") as drinks:
        for row in csv.DictReader(drinks):
            all_rows.append(fix_int_fields(row))

    most_beer_list = most_beer(all_rows)

    print("Top 5 Beer Drinking Countries According to 538:")
    for row in most_beer_list[:5]:
        print(f"Country: {row['country']}\t\tBeer Servings: {row['beer_servings']}")

