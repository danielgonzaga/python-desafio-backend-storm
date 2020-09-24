# -*- coding: utf-8 -*-
from colorama import Fore, Style


def main():
    sequence = sequence_definition()
    validation = balancing_check(sequence)
    color = ""

    if validation == ' NAO':
        color = Fore.RED
    else:
        color = Fore.GREEN

    print(color + sequence + validation)


def sequence_definition():
    sequence = ""

    while True:
        print("\n--- MENU ---\n"
              "1. [\n"
              "2. {\n"
              "3. (\n"
              "4. ]\n"
              "5. }\n"
              "6. )\n"
              "7. Encerrar\n"
              "Escolha sua opção: ", end='')
        try:
            selected_input = input()
            selected_input = int(selected_input)
            if isinstance(selected_input, int):
                if 1 <= selected_input <= 7:
                    if selected_input == 1:
                        sequence += "["
                    elif selected_input == 2:
                        sequence += "{"
                    elif selected_input == 3:
                        sequence += "("
                    elif selected_input == 4:
                        sequence += "]"
                    elif selected_input == 5:
                        sequence += "}"
                    elif selected_input == 6:
                        sequence += ")"
                    elif selected_input == 7:
                        if len(sequence) == 0:
                            print(Fore.RED + "A sequência ainda está vazia")
                            print(Style.RESET_ALL)
                        else:
                            break

                    print("Sequencia atual: ", end='')
                    for items in sequence:
                        print(items, end='')
                else:
                    print(Fore.RED + "Digite uma das opções entre 1 e 7")
                    print(Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Digite uma das opções entre 1 e 7")
            print(Style.RESET_ALL)

    return sequence


def balancing_check(sequence):
    if ('[' in sequence and ']' not in sequence) or \
       ('{' in sequence and '}' not in sequence) or \
       ('(' in sequence and ')' not in sequence):
        return ' NAO'
    else:
        mapped_sequence = dict(zip('({[', ')}]'))
        checked_sequence = []

        for bracket in sequence:
            if bracket in mapped_sequence:
                checked_sequence.append(mapped_sequence[bracket])
            elif not (checked_sequence and bracket == checked_sequence.pop()):
                return ' NAO'

        return ' SIM'


if __name__ == "__main__":
    main()
