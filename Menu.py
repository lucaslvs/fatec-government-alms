from Plot import Plot

class Menu():

    def __showOption1(self):
        return int(input(
            '''
                \n\n
                (1) - Visualizar os dados brutos\n
                (2) - Visualizar gráficos\n
                (3) - Sair\n
            '''))
    def __showOption2(self):
        return int(input(
                    """
                    \n\n
                    (1) - Gasto por estado/ano \n
                    (2) - Gasto de todos os estados/ano \n
                    (3) - Gasto dentro de um x periodo de tempo (Por estado)
                    (4) - Voltar \n
                    \n
                    """
                ))
    def __showOption3(self):
        return int(input('''
                \n\n
                (1) - Verificar outra informação\n
                (2) - Voltar ao menu principal\n
                '''))
    
    def showMenu(self, jsonData):
        plt = Plot(jsonData)

        while True:

            opt1 = self.__showOption1()
            
            if opt1 == 1:
                pass
            elif opt1 == 2:
                while True:

                    opt2 = self.__showOption2()
                    
                    if opt2 == 1:
                        state = input('Selecione o estado: ', end = '')
                        year = int(input('Selecione o ano: ', end = ''))
                        plt.plot_state_year(state, year)
                        
                        if plt.__showOption3() == 1:
                            continue
                        else:
                            break
                   
                    elif opt2 == 2:
                        plt.plot_aState_aYear()
                        
                        if plt.__showOption3() == 1:
                            continue
                        else:
                            break
                    
                    elif opt2 == 3:
                        state = input('Selecione o estado: ', end = '') 
                        start = int(input('Insira o ano de inicio'))
                        end = int(input('Insira o ano de fim'))
                        plt.plot_timeline(state, start,end)
                        
                        if plt.__showOption3() == 1:
                            continue
                        else:
                            break
                    elif opt2 == 4:
                        break
            
            elif opt1 == 3:
                exit()