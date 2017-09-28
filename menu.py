from plot import *


def menu(json_data):
    while True:
        choice = int(input(
            """
            \n\n
            (1) - Listar os dados
            (2) - Gerar gŕaficos
            (3) - Sair
            \n
            """
        ))
        if choice > 3 or choice < 1:
            print('\nOpção Inválida!\n')
        elif choice == 1:
            while True:
                break
        elif choice == 2:
            while True:
                choice = int(input(
                    """
                    \n\n
                    (1) - Por ano
                    (2) - Por estado
                    (3) - Todos os anos
                    (4) - Todos os estados
                    (5) - Voltar
                    \n
                    """
                ))
                if choice > 5 or choice < 1:
                    print('\nOpção Inválida!\n')
                elif choice == 1:
                    while True:
                        year = input('Ano:')
                    if year > actual_year or year < 2004:
                        print('Ano inválido!')
                    else:
                        plot_year(json_data, year)
                        break
                elif choice == 2:
                    while True:
                        state = input('Estado:')
                    if state in json_data["allStates"].keys():
                        plot_year(json_data, year)
                        break
                    else:
                        print('\nEstados inválido digite corretamente\n')
                        plot_state(json_data, state)
                elif choice == 3:
                    plot_all_years(json_data)
                elif choice == 4:
                    plot_all_states(json_data)
                else:
                    break
        else:
            break
