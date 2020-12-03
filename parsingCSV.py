import csv


def parsingCSV(cpfc_f, csv_f):
    reader = csv.DictReader(csv_f, delimiter=';')
    for line in reader:
        cpfc_f.write(f"{line['Shrt_Desc']}\n"
                     f"     Белки:        {line['Protein_(g)']} г.\n"
                     f"     Жиры:         {line['Lipid_Tot_(g)']} г.\n"
                     f"     Углеводы:     {line['Carbohydrt_(g)']} г.\n"
                     f"     Калорийность: {line['Energ_Kcal']} ккал.\n\n")


def main():
    cpfc_f = open('cpfc.txt', 'w', encoding='utf-8')
    cpfc_f.write('Калорийность и содержание белков, жиров и углеводов в продуктах:\n\n')
    with open('ABBREV.csv', encoding='utf-8') as csv_f:
        parsingCSV(cpfc_f, csv_f)


if __name__ == '__main__':
    main()
