# -*- coding: utf-8 -*-
from colorama import Fore, Style


def main():
    nums = [2, 7, 11, 15]
    selected_num = ""

    print("[2, 7, 11, 15]\n")
    print("Digite um número inteiro como alvo: ", end='')

    while True:
        selected_num = input()

        try:
            selected_num = int(selected_num)
            if isinstance(selected_num, int):
                break
        except ValueError:
            print(Fore.RED + "Erro: Digite apenas numeros inteiros")
            print(Style.RESET_ALL)

    result = sum_verification(nums, selected_num)
    if result == 1:
        print(Fore.RED + "Não é possível utilizar os números disponíveis para o alvo selecionado")
    else:
        print("Array: {}\n"
              "Índice do elemento 1 no array: {}\n"
              "Índice do elemento 2 no array: {}\n"
              "Soma: {} + {} = {}"
              .format(nums, result[0], result[1], nums[result[0]], nums[result[1]], nums[result[0]] + nums[result[1]]))


def sum_verification(nums, selected_num):
    if selected_num < 9 or selected_num > 26:
        return 1
    else:
        if nums[0] + nums[1] == selected_num:
            return [0, 1]
        elif nums[0] + nums[2] == selected_num:
            return [0, 2]
        elif nums[0] + nums[3] == selected_num:
            return [0, 3]
        elif nums[1] + nums[2] == selected_num:
            return [1, 2]
        elif nums[1] + nums[3] == selected_num:
            return [1, 3]
        elif nums[2] + nums[3] == selected_num:
            return [2, 3]
        else:
            return 1


if __name__ == "__main__":
    main()
