import csv
import pandas as pd


def read_table(file_path: str) -> pd.DataFrame:
    with open(file_path, 'r', encoding='utf-8') as file:
        header = []
        rows = []
        is_header_line = True
        reader = csv.reader(file, delimiter=' ', quotechar='"')
        for row in reader:
            if is_header_line:
                header = row[1:]
                is_header_line = False
                continue

            rows.append(row[1:])

        dataframe = pd.DataFrame(columns=header, data=rows)

        return dataframe


def main() -> None:
    titanic_with_labels = read_table('titanic_with_labels.csv')

    def is_sex_defined(x): return x['sex'].lower() not in ['-', 'не указан']

    titanic_with_labels = titanic_with_labels[titanic_with_labels.apply(is_sex_defined, axis=1)]

    def unify_sex_symbol(x): return 1 if x['sex'].lower() in ['m', 'м', 'мужчина'] else 0

    titanic_with_labels['sex'] = titanic_with_labels.apply(unify_sex_symbol, axis=1)

    max_row = titanic_with_labels['row_number'].max()
    no_row_indices = (titanic_with_labels['row_number'].isnull()) & (titanic_with_labels['row_number'] == '')
    titanic_with_labels[no_row_indices]['row_number'] = max_row

    high_quantile = titanic_with_labels["liters_drunk"].astype(float).quantile(0.90)

    def is_adequate_drunk(x): return 0 <= float(x['liters_drunk']) < high_quantile
    adequate_drunk_rows = titanic_with_labels[titanic_with_labels.apply(is_adequate_drunk, axis=1)]

    drunk_average = adequate_drunk_rows['liters_drunk'].astype(float).mean()

    def change_inadequate(x): return x['liters_drunk'] if is_adequate_drunk(x) else drunk_average
    titanic_with_labels['liters_drunk'] = titanic_with_labels.apply(change_inadequate, axis=1)

    print(titanic_with_labels)

    cinema_sessions = read_table('cinema_sessions.csv')
    print(cinema_sessions)


main()
