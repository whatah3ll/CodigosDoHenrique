from pywinauto import Desktop, Application
import pyautogui
import time
class SiaPdvClass():
    pyautogui.FAILSAFE = True
    def selecionaSiaPdv():
        try:
            app = Application(backend="win32").connect(title="SIA PDV - Criare Tecnologia")  # Conecta na janela pelo título
            main_window = app.window(title="SIA PDV - Criare Tecnologia")  # Obtém a referência para a janela principal
            main_window.set_focus()  # Traga a janela para o foco na tela
            pyautogui.click()
            # Verifica se a janela está realmente ativa após a conexão
            if main_window.is_visible():
                return True  # Retorno indicando sucesso
            else:
                print("Tela não visivel")
                return False
        except Exception as e:
            # Tratamento de exceção caso não consiga conectar
            print(f"Erro ao tentar conectar a tela: {e}")
            return False
        
    def selecionaSiaPdvVenda():
        try:
            app = Application(backend="uia").connect(title="SIA PDV - Criare Tecnologia")  # Conecta na janela pelo título
            main_window = app.window(title="SIA PDV - Criare Tecnologia")  # Obtém a referência para a janela principal
            main_window.set_focus()  # Traga a janela para o foco na tela
            pyautogui.click()
            # Verifica se a janela está realmente ativa após a conexão
            if main_window.is_visible():
                return True  # Retorno indicando sucesso
            else:
                print("Tela não visivel")
                return False
        except Exception as e:
            # Tratamento de exceção caso não consiga conectar
            print(f"Erro ao tentar conectar a tela: {e}")
            return False
        
    def travaAtencao():
        try:
            app = Application(backend="win32").connect(title="Atenção")  # Conecta na janela pelo título
            main_window = app.window(title="Atenção")  # Obtém a referência para a janela principal
            main_window.set_focus()  # Traga a janela para o foco na tela
            # Verifica se a janela está realmente ativa após a conexão
            if main_window.is_visible():
                return True  # Retorno indicando sucesso
            else:
                print("Tela não visivel")
                return False
        except Exception as e:
            # Tratamento de exceção caso não consiga conectar
            print(f"Erro ao tentar conectar a tela: {e}")
            return False
        
    def travaATENCAO():
        try:
            app = Application(backend="win32").connect(title="ATENÇÃO")  # Conecta na janela pelo título
            main_window = app.window(title="ATENÇÃO")  # Obtém a referência para a janela principal
            main_window.set_focus()  # Traga a janela para o foco na tela
            # Verifica se a janela está realmente ativa após a conexão
            if main_window.is_visible():
                return True  # Retorno indicando sucesso
            else:
                print("Tela não visivel")
                return False
        except Exception as e:
            # Tratamento de exceção caso não consiga conectar
            print(f"Erro ao tentar conectar a tela: {e}")
            return False
        
    def travaErro():
        try:
            app = Application(backend="win32").connect(title="Erro")  # Conecta na janela pelo título
            main_window = app.window(title="Erro")  # Obtém a referência para a janela principal
            main_window.set_focus()  # Traga a janela para o foco na tela
            # Verifica se a janela está realmente ativa após a conexão
            if main_window.is_visible():
                return True  # Retorno indicando sucesso
            else:
                print("Tela não visivel")
                return False
        except Exception as e:
            # Tratamento de exceção caso não consiga conectar
            print(f"Erro ao tentar conectar a tela: {e}")
            return False
        
    def travaCancelaNFC():
        try:
            app = Application(backend="win32").connect(title="NFC-e - Cancelamento")  # Conecta na janela pelo título
            main_window = app.window(title="NFC-e - Cancelamento")  # Obtém a referência para a janela principal
            main_window.set_focus()  # Traga a janela para o foco na tela
            # Verifica se a janela está realmente ativa após a conexão
            if main_window.is_visible():
                return True  # Retorno indicando sucesso
            else:
                print("Tela não visivel")
                return False
        except Exception as e:
            # Tratamento de exceção caso não consiga conectar
            print(f"Erro ao tentar conectar a tela: {e}")
            return False

    def travaDialog():
        app = Application(backend="win32").connect(title="SIA PDV - Criare Tecnologia")  # Conecta na janela pelo título
        main_window = app.window(title="SIA PDV - Criare Tecnologia")  # Obtém a referência para a janela principal
        main_window.set_focus() # Traga a janela para o foco na tela
        pyautogui.click()
        textoTela = app.top_window()
        texto_desejado = "Informação"
        try:
            all_text = textoTela.window_text()
            print(all_text)
            if texto_desejado in all_text:
                print(f"O texto '{texto_desejado}' foi encontrado na tela.")
                return True
            else:
                print(f"O texto '{texto_desejado}' não foi encontrado na tela.")
                return False
        except Exception as e:
            print(f"Erro ao tentar encontrar o texto: {str(e)}")

    def travaDialogUia():
        app = Application(backend="uia").connect(title="SIA PDV - Criare Tecnologia")  # Conecta na janela pelo título
        main_window = app.window(title="SIA PDV - Criare Tecnologia")  # Obtém a referência para a janela principal
        main_window.set_focus() # Traga a janela para o foco na tela
        pyautogui.click()
        textoTela = app.top_window()
        texto_desejado = "Informação"
        try:
            all_text = textoTela.window_text()
            print(all_text)
            if texto_desejado in all_text:
                print(f"O texto '{texto_desejado}' foi encontrado na tela.")
                return True
            else:
                print(f"O texto '{texto_desejado}' não foi encontrado na tela.")
                return False
        except Exception as e:
            print(f"Erro ao tentar encontrar o texto: {str(e)}")

    def vendaPadrão(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            venda = 2
            while not pararLoop:
                contaVenda = 1
                if formaPag > 13:
                    formaPag = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 2 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    travaHomolo = SiaPdvClass.travaDialog()
                    if travaHomolo:
                        pyautogui.press("escape") # pula o alert de ambiente em homologação
                        time.sleep(intervaloTecla)
                    travaEntrega = SiaPdvClass.travaDialog()
                    if travaEntrega:
                        pyautogui.press("2") # seleciona não para informar os dados de entrega
                        time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F1") # abre a tela de pagamento
                time.sleep(intervaloTecla)
                match formaPag:
                    case 1:
                        pyautogui.press("1") # seleciona a forma de pagamento(por enquanto até o 13, mas havera mudanças pelo case de apertar 1 e ele voltar para o 1 em vez de fazer o 10 por exemplo)
                    case 2:
                        pyautogui.press("2")
                    case 3:
                        pyautogui.press("3")
                    case 4:
                        pyautogui.press("4")
                    case 5:
                        pyautogui.press("5")
                    case 6:
                        pyautogui.press("6")
                    case 7:
                        pyautogui.press("7")
                    case 8:
                        pyautogui.press("8")
                    case 9:
                        pyautogui.press("9")
                    case 10:
                        pyautogui.press("10")
                    case 11:
                        pyautogui.press("11")
                    case 12:
                        pyautogui.press("12")
                    case 13:
                        pyautogui.press("13")
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona a forma de pagamento
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # confirma o pagamento
                time.sleep(intervaloTecla + 10)
                travaAtencao = SiaPdvClass.travaAtencao()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                contador += 1
                formaPag += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e

    def venda100Prod(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            venda = 100
            while not pararLoop:
                contaVenda = 1
                if formaPag > 13:
                    formaPag = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 100 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    if contaVenda == 1:
                        travaHomolo = SiaPdvClass.travaDialog()
                        if travaHomolo:
                            pyautogui.press("escape") # pula o alert de ambiente em homologação
                            time.sleep(intervaloTecla)
                        travaEntrega = SiaPdvClass.travaDialog()
                        if travaEntrega:
                            pyautogui.press("2") # seleciona não para informar os dados de entrega
                            time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F1") # abre a tela de pagamento
                time.sleep(intervaloTecla)
                match formaPag:
                    case 1:
                        pyautogui.press("1") # seleciona a forma de pagamento(por enquanto até o 13, mas havera mudanças pelo case de apertar 1 e ele voltar para o 1 em vez de fazer o 10 por exemplo)
                    case 2:
                        pyautogui.press("2")
                    case 3:
                        pyautogui.press("3")
                    case 4:
                        pyautogui.press("4")
                    case 5:
                        pyautogui.press("5")
                    case 6:
                        pyautogui.press("6")
                    case 7:
                        pyautogui.press("7")
                    case 8:
                        pyautogui.press("8")
                    case 9:
                        pyautogui.press("9")
                    case 10:
                        pyautogui.press("10")
                    case 11:
                        pyautogui.press("11")
                    case 12:
                        pyautogui.press("12")
                    case 13:
                        pyautogui.press("13")
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona a forma de pagamento
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # confirma o pagamento
                time.sleep(intervaloTecla + 10)
                travaAtencao = SiaPdvClass.travaAtencao()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                contador += 1
                formaPag += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e

    def venda200Prod(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            venda = 200
            while not pararLoop:
                contaVenda = 1
                if formaPag > 13:
                    formaPag = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 100 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    if contaVenda == 1:
                        travaHomolo = SiaPdvClass.travaDialog()
                        if travaHomolo:
                            pyautogui.press("escape") # pula o alert de ambiente em homologação
                            time.sleep(intervaloTecla)
                        travaEntrega = SiaPdvClass.travaDialog()
                        if travaEntrega:
                            pyautogui.press("2") # seleciona não para informar os dados de entrega
                            time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F1") # abre a tela de pagamento
                time.sleep(intervaloTecla)
                match formaPag:
                    case 1:
                        pyautogui.press("1") # seleciona a forma de pagamento(por enquanto até o 13, mas havera mudanças pelo case de apertar 1 e ele voltar para o 1 em vez de fazer o 10 por exemplo)
                    case 2:
                        pyautogui.press("2")
                    case 3:
                        pyautogui.press("3")
                    case 4:
                        pyautogui.press("4")
                    case 5:
                        pyautogui.press("5")
                    case 6:
                        pyautogui.press("6")
                    case 7:
                        pyautogui.press("7")
                    case 8:
                        pyautogui.press("8")
                    case 9:
                        pyautogui.press("9")
                    case 10:
                        pyautogui.press("10")
                    case 11:
                        pyautogui.press("11")
                    case 12:
                        pyautogui.press("12")
                    case 13:
                        pyautogui.press("13")
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona a forma de pagamento
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # confirma o pagamento
                time.sleep(intervaloTecla + 10)
                travaAtencao = SiaPdvClass.travaAtencao()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                contador += 1
                formaPag += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e

    def cancelaVenda(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            venda = 2
            while not pararLoop:
                contaVenda = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 2 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    travaHomolo = SiaPdvClass.travaDialog()
                    if travaHomolo:
                        pyautogui.press("escape") # pula o alert de ambiente em homologação
                        time.sleep(intervaloTecla)
                    travaEntrega = SiaPdvClass.travaDialog()
                    if travaEntrega:
                        pyautogui.press("2") # seleciona não para informar os dados de entrega
                        time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F7") # abre a tela de cancelamento
                time.sleep(intervaloTecla + 1)
                pyautogui.press("1")
                time.sleep(intervaloTecla + 1)
                pyautogui.press("F3")
                time.sleep(intervaloTecla)
                travaAtencao = SiaPdvClass.travaAtencao()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                contador += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e

    def extraFinan(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            venda = 2
            while not pararLoop:
                contaVenda = 1
                if formaPag > 13:
                    formaPag = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # selecina a opção recebimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor da recebimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valo1r
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a recebimento
                    time.sleep(intervaloTecla)
                    travaReceb = SiaPdvClass.travaDialogUia()
                    while travaReceb == True: # teste para esperar a operação de recebimento
                        travaReceb = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F1") # selecina a opção suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor da suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valo1r
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a suprimento
                    time.sleep(intervaloTecla)
                    travaSupri = SiaPdvClass.travaDialogUia()
                    while travaSupri == True: # teste para esperar a operação de suprimento
                        travaSupri = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 2 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    travaHomolo = SiaPdvClass.travaDialog()
                    if travaHomolo:
                        pyautogui.press("escape") # pula o alert de ambiente em homologação
                        time.sleep(intervaloTecla)
                    travaEntrega = SiaPdvClass.travaDialog()
                    if travaEntrega:
                        pyautogui.press("2") # seleciona não para informar os dados de entrega
                        time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F1") # abre a tela de pagamento
                time.sleep(intervaloTecla)
                match formaPag:
                    case 1:
                        pyautogui.press("1") # seleciona a forma de pagamento(por enquanto até o 13, mas havera mudanças pelo case de apertar 1 e ele voltar para o 1 em vez de fazer o 10 por exemplo)
                    case 2:
                        pyautogui.press("2")
                    case 3:
                        pyautogui.press("3")
                    case 4:
                        pyautogui.press("4")
                    case 5:
                        pyautogui.press("5")
                    case 6:
                        pyautogui.press("6")
                    case 7:
                        pyautogui.press("7")
                    case 8:
                        pyautogui.press("8")
                    case 9:
                        pyautogui.press("9")
                    case 10:
                        pyautogui.press("10")
                    case 11:
                        pyautogui.press("11")
                    case 12:
                        pyautogui.press("12")
                    case 13:
                        pyautogui.press("13")
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona a forma de pagamento
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # confirma o pagamento
                time.sleep(intervaloTecla + 10)
                travaAtencao = SiaPdvClass.travaAtencao()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                contador += 1
                formaPag += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e

    def cancelaProd(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            venda = 2
            while not pararLoop:
                contaVenda = 1
                if formaPag > 13:
                    formaPag = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 2 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    travaHomolo = SiaPdvClass.travaDialog()
                    if travaHomolo:
                        pyautogui.press("escape") # pula o alert de ambiente em homologação
                        time.sleep(intervaloTecla)
                    travaEntrega = SiaPdvClass.travaDialog()
                    if travaEntrega:
                        pyautogui.press("2") # seleciona não para informar os dados de entrega
                        time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F12") # abre o menu
                time.sleep(intervaloTecla)
                pyautogui.press("3") # muda para a aba de cancelamentos
                time.sleep(intervaloTecla)
                pyautogui.press("F2") # abre a tela de cancelamento de item
                time.sleep(intervaloTecla)
                pyautogui.typewrite("1") # digita o codigo do item
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona o itme
                time.sleep(intervaloTecla)
                pyautogui.press("F3") # confirma o cancelamento
                time.sleep(intervaloTecla)
                pyautogui.press("F3") # confirma o motivo do cancelamento
                time.sleep(intervaloTecla) 
                pyautogui.press("F1") # abre a tela de pagamento
                time.sleep(intervaloTecla)
                match formaPag:
                    case 1:
                        pyautogui.press("1") # seleciona a forma de pagamento(por enquanto até o 13, mas havera mudanças pelo case de apertar 1 e ele voltar para o 1 em vez de fazer o 10 por exemplo)
                    case 2:
                        pyautogui.press("2")
                    case 3:
                        pyautogui.press("3")
                    case 4:
                        pyautogui.press("4")
                    case 5:
                        pyautogui.press("5")
                    case 6:
                        pyautogui.press("6")
                    case 7:
                        pyautogui.press("7")
                    case 8:
                        pyautogui.press("8")
                    case 9:
                        pyautogui.press("9")
                    case 10:
                        pyautogui.press("10")
                    case 11:
                        pyautogui.press("11")
                    case 12:
                        pyautogui.press("12")
                    case 13:
                        pyautogui.press("13")
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona a forma de pagamento
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # confirma o pagamento
                time.sleep(intervaloTecla + 10)
                travaAtencao = SiaPdvClass.travaAtencao()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                contador += 1
                formaPag += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e

    def cancelaUltimaVenda(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            venda = 2
            while not pararLoop:
                contaVenda = 1
                if formaPag > 13:
                    formaPag = 1
                if contador == 1:
                    pdvTela = SiaPdvClass.selecionaSiaPdv()
                    if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                        err = "Erro ao tentar encontrar a janela do sia PDV"
                        yield "err", err
                        break
                    time.sleep(intervaloTecla)
                    pyautogui.press("F2") # abre o caixa
                    time.sleep(intervaloTecla)
                    travaCaixa = SiaPdvClass.travaDialog()
                    if travaCaixa:
                        pyautogui.press("1") # confirma a abertura
                    time.sleep(intervaloTecla)
                    pyautogui.press("escape") # pula o alert de de suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento do suprimento(por enquanto seleciona a primeira)
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("200") # digita o valor do suprimento
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma de vez o suprimento
                    travaAbre = SiaPdvClass.travaDialog()
                    while travaAbre == True: # teste para esperar a operação de suprimento
                        travaAbre = SiaPdvClass.travaDialog()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 5)
                    pyautogui.press("F12") # abre o menu
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # selecina a opção sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # seleciona a forma de pagamento
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("50") # digita o valor da sangria
                    time.sleep(intervaloTecla)
                    pyautogui.press("F3") # confirma o valor
                    time.sleep(intervaloTecla)
                    pyautogui.press("1") # confirma a sangria
                    time.sleep(intervaloTecla)
                    travaSangria = SiaPdvClass.travaDialogUia()
                    while travaSangria == True: # teste para esperar a operação de sangria
                        travaSangria = SiaPdvClass.travaDialogUia()
                        print("esperando dialog sumir")
                        time.sleep(2)
                    time.sleep(intervaloTecla + 2)
                pdvTela = SiaPdvClass.selecionaSiaPdv()
                if pdvTela == False:  # Chama a função selecionaMultiPdv para verificar a visibilidade da janela
                    err = "Erro ao tentar encontrar a janela do sia PDV"
                    yield "err", err
                    break
                while contaVenda <= venda: # teste para adicionar 2 produtos
                    time.sleep(intervaloTecla)
                    pyautogui.typewrite("1922") # digita o codigo do produto
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") # adicionar o produto
                    time.sleep(intervaloTecla)
                    travaHomolo = SiaPdvClass.travaDialog()
                    if travaHomolo:
                        pyautogui.press("escape") # pula o alert de ambiente em homologação
                        time.sleep(intervaloTecla)
                    travaEntrega = SiaPdvClass.travaDialog()
                    if travaEntrega:
                        pyautogui.press("2") # seleciona não para informar os dados de entrega
                        time.sleep(intervaloTecla)
                    contaVenda += 1
                time.sleep(intervaloTecla)
                pyautogui.press("F1") # abre a tela de pagamento
                time.sleep(intervaloTecla)
                match formaPag:
                    case 1:
                        pyautogui.press("1") # seleciona a forma de pagamento(por enquanto até o 13, mas havera mudanças pelo case de apertar 1 e ele voltar para o 1 em vez de fazer o 10 por exemplo)
                    case 2:
                        pyautogui.press("2")
                    case 3:
                        pyautogui.press("3")
                    case 4:
                        pyautogui.press("4")
                    case 5:
                        pyautogui.press("5")
                    case 6:
                        pyautogui.press("6")
                    case 7:
                        pyautogui.press("7")
                    case 8:
                        pyautogui.press("8")
                    case 9:
                        pyautogui.press("9")
                    case 10:
                        pyautogui.press("10")
                    case 11:
                        pyautogui.press("11")
                    case 12:
                        pyautogui.press("12")
                    case 13:
                        pyautogui.press("13")
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # seleciona a forma de pagamento
                time.sleep(intervaloTecla)
                pyautogui.press("enter") # confirma o pagamento
                time.sleep(intervaloTecla + 10)
                # travaAtencao = SiaPdvClass.travaAtencao()
                # if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                #     yield "err", "Alerta inesperado na tela!"
                #     break
                # travaErro = SiaPdvClass.travaErro()
                # if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                #     yield "err", "Alerta inesperado na tela!"
                #     break
                # travaDialog = SiaPdvClass.travaDialog()
                # if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                #     yield "err", "Alerta inesperado na tela!"
                #     break
                time.sleep(intervaloTecla + 5)
                pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                while pdvFinaliza == False:  # teste para esperar a tela de venda aparecer de novo antes de iniciar a automação novamente
                    pdvFinaliza = SiaPdvClass.selecionaSiaPdv()
                time.sleep(intervaloTecla)
                pyautogui.press("F12") # abre o menu
                time.sleep(intervaloTecla)
                pyautogui.press("3") # muda para a aba de cancelamentos
                time.sleep(intervaloTecla)
                pyautogui.press("F3") # abre o meno de cancelamento de ultima venda
                time.sleep(intervaloTecla)
                pyautogui.press("F3") # confirma o cancelamento
                time.sleep(8)
                travaAtencao = SiaPdvClass.travaATENCAO()
                if travaAtencao: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaErro = SiaPdvClass.travaErro()
                if travaErro: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                travaDialog = SiaPdvClass.travaDialog()
                if travaDialog: # teste para caso aparecer um alert inesperado na tela(alinha melhor com o gustavo)
                    yield "err", "Alerta inesperado na tela!"
                    break
                contador += 1
                formaPag += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal:")
            print(type(e), e)
            yield "err", type(e), e