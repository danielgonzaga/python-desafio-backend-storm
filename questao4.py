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
    total_rain = rain_calculation(numbers)
    print("Água retida após a chuva: {}".format(total_rain))


def rain_calculation(numbers):
    begin_interval_index = None
    end_interval_index = None
    interval_rain = []
    total_rain = 0
    converted_numbers = [int(convert_numbers) for convert_numbers in numbers]

    for index, n in enumerate(converted_numbers):
        index = int(index)
        n = int(n)

        if n != 0 and begin_interval_index is None:
            begin_interval_index = index
        elif begin_interval_index is not None and index < len(converted_numbers)-1:
            if n >= converted_numbers[begin_interval_index]:
                end_interval_index = index
            elif n > converted_numbers[index-1] and n > converted_numbers[index+1]:
                end_interval_index = index
            else:
                interval_rain.append(n)
        elif begin_interval_index is not None and index == len(converted_numbers)-1 and n > converted_numbers[index-1]:
            end_interval_index = index

        if begin_interval_index is not None and end_interval_index is not None:
            for rain in interval_rain:
                if converted_numbers[begin_interval_index] > converted_numbers[end_interval_index]:
                    total_rain += converted_numbers[end_interval_index] - rain
                else:
                    total_rain += converted_numbers[begin_interval_index] - rain
            begin_interval_index = end_interval_index
            end_interval_index = None
            interval_rain.clear()

    return total_rain


if __name__ == "__main__":
    main()
