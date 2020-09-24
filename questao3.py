# -*- coding: utf-8 -*-
from colorama import Fore, Style
import re


def main():
    while True:
        print("Digite os nÚmeros inteiros separando-os por vÍrgulas, sem utilizar espaço: ", end='')
        numbers_input = input()
        rgx = re.match("^(\\d+(,\\d+)*)?$", numbers_input)
        if rgx is not None:
            break
        else:
            print(Fore.RED + "Input inválido!")
            print(Style.RESET_ALL)

    numbers = numbers_input.split(",")
    profit_result = profit_calculator(numbers)
    print(profit_result)


def profit_calculator(prices):
    converted_prices = [int(convert_price) for convert_price in prices]

    max_profit = 0
    min_price = converted_prices[0]

    for price in range(1, len(converted_prices)):
        if converted_prices[price] < min_price:
            min_price = converted_prices[price]
        max_profit = max(max_profit, converted_prices[price] - min_price)

    return max_profit


if __name__ == "__main__":
    main()
