from itertools import product
from string import ascii_uppercase, digits
from hashlib import md5
import json


def build_medallion_table():
    medallion_table = {}

    # medallion 5X55
    prod = list(product(digits, ascii_uppercase, digits, digits))
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

    # licence with six digits
    prod = list(product(digits, repeat=6))
    prod_string = [''.join(element) for element in prod]
    prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
    licence_table.update(prod_dict)

    # licence with seven digits starting with a 5
    prod_string = ['5' + element for element in prod_string]
    prod_dict = {md5(element.encode()).hexdigest().upper(): element for element in prod_string}
    licence_table.update(prod_dict)

    return licence_table


medallion = build_medallion_table()

with open('medallion_table.txt', 'w') as output:
    json.dump(medallion, output)

licence = build_licence_table()

with open('licence_table.txt', 'w') as output:
    json.dump(licence, output)
