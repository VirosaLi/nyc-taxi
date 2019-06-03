from itertools import product
from string import ascii_letters, ascii_uppercase, digits
from hashlib import md5
import json


def build_medallion_table():
    medallion_table = {}

    # # medallion X555
    # prod = list(product(ascii_uppercase, digits, digits, digits))
    # prod_string = [''.join(element) for element in prod]
    # prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
    # medallion_table.update(prod_dict)

    # medallion 5X55
    prod = list(product(digits, ascii_letters, digits, digits))
    prod_string = [''.join(element) for element in prod]
    prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
    medallion_table.update(prod_dict)

    # medallion XX555
    prod = list(product(ascii_uppercase, ascii_uppercase, digits, digits, digits))
    prod_string = [''.join(element) for element in prod]
    prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
    medallion_table.update(prod_dict)

    # medallion XXX555
    prod = list(product(ascii_uppercase, ascii_uppercase, ascii_uppercase, digits, digits, digits))
    prod_string = [''.join(element) for element in prod]
    prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
    medallion_table.update(prod_dict)

    return medallion_table


def build_licence_table():
    licence_table = {}

    for i in range(1, 8):
        prod = list(product(digits, repeat=i))
        prod_string = [''.join(element) for element in prod]
        prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
        licence_table.update(prod_dict)

    return licence_table


def main():
    medallion = build_medallion_table()

    with open('medallion_table.txt', 'w') as output:
        json.dump(medallion, output)

    licence = build_licence_table()

    with open('licence_table.txt', 'w') as output:
        json.dump(licence, output)


if __name__ == '__main__':
    main()
