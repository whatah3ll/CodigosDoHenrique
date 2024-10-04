from classe.SiaWebClass import SiaWebClass
import flet as ft

testesPossiveis = None
testeEscolhido = None
contadorAtual = 1
pararLoop = False
cad = False

def main(page: ft.page):
    SiaWebInstancia = SiaWebClass()

    def attTeste(testeMudado):
        global testesPossiveis
        if testeMudado == "Cadastros":
            testesPossiveis = testesCad
        elif testeMudado == "Movimentações":
            testesPossiveis = testesMov
        elif testeMudado == "Financeiro":
            testesPossiveis = testesFin
        elif testeMudado == "Relatórios":
            testesPossiveis = testesRel
        else:
            testesPossiveis = ft.Dropdown(label="Escolha qual teste você deseja fazer!",
                        width=401,
                        options=[
                        ],
                        )
        return testesPossiveis

    def pegaTestes(e):
        global testesPossiveis
        testeAtual = testes.value
        testesPossiveis = attTeste(testeAtual)
        # Reconstrua todo o conteúdo do card de teste com o novo dropdown
        teste.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Testes do Sia Web"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Teste de:"),
                    ),
                    ft.Row(
                        [testes],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Qual teste:")
                    ),
                    ft.Row(
                        [testesPossiveis],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [btnIniciar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()
    
    global testesPossiveis 
    ini = "inicio"
    testesPossiveis = attTeste(ini)

    def sair(e):
        global pararLoop
        page.window.destroy()
        pararLoop = True

    def parar(e):
        global pararLoop
        global contadorAtual
        global testeEscolhido
        pararLoop = True
        testeIniciado.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarTeste, btnCont, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()

    def pararCad(e):
        global pararLoop
        global contadorAtual
        global testeEscolhido
        pararLoop = True
        testeIniciadoCad.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PEOPLE, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PEOPLE, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarCad, btnContCad,  btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()
            
    def continuar(e):
        global pararLoop
        global contadorAtual
        pararLoop = False
        testeIniciado.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarTeste, btnParar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()
        iniciar(e)

    def continuarCad(e):
        global pararLoop
        global contadorAtual
        pararLoop = False
        testeIniciadoCad.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PEOPLE, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PEOPLE, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarCad, btnPararCad,  btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()
        iniciar(e)

    def prox(e):
        global intervaloTeclas
        global intervaloExec
        if intervaloSec.value == "" and intervaloExe.value == "":
            def closeErr(e):
                err.open = False
                page.update()
            err = ft.AlertDialog(
                modal=True,
                title=ft.Text("Valores invalidos!"),
                content=ft.Text("Intervalos de tempo vazios"),
                actions=[
                    ft.TextButton("Ok", on_click=closeErr),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.overlay.append(err)
            err.open = True
            page.update()
        else:
            intervaloTeclas = int(intervaloSec.value)
            intervaloExec = int(intervaloExe.value)
            page.clean()
            page.overlay.append(logCad)
            logCad.open = True
            page.update()
    
    def errTeste(e):
        def closeErr(e):
            err.open = False
            page.add(teste)
        err = ft.AlertDialog(
            modal=True,
            title=ft.Text("Valores invalidos!"),
            content=ft.Text("Selecione um teste antes"),
            actions=[
                ft.TextButton("Ok", on_click=closeErr),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.clean()
        page.overlay.append(err)
        err.open = True
        page.update()
    
    def login(e):
        # page.overlay.append(logCad)
        page.close(logCad)
        page.add(login)

    def cadastrar(e):
        global contadorAtual
        global pararLoop
        global cad
        cad = True
        page.close(logCad)
        page.add(testeIniciadoCad)
        contador = SiaWebInstancia.cadastroSiaWeb(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
        for dados in contador:
            if pararLoop:
                break
            if dados[0] == "contador":
                contadorAtual = dados[1]
                atualizarTesteIniciadoCad()
            else:
                erroTesteIniciadoCad(dados[1], dados[2])

    def voltarLogin(e):
        page.clean()
        page.open(logCad)
        page.update()

    def voltarLogCad(e):
        page.close(logCad)
        page.add(inicio)

    def voltarTeste(e):
        global pararLoop
        global testeEscolhido
        testeEscolhido = None
        pararLoop = True
        page.clean()
        page.add(teste)

    def logar(e):
        global cad
        cad = False
        user = email.value
        passWord = senha.value
        page.clean()
        SiaWebInstancia.loginSiaWeb(user, passWord, intervaloTeclas)
        page.add(teste)
    
    def atualizarTesteIniciado():
        global contadorAtual
        testeIniciado.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarTeste, btnParar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()
    
    def atualizarTesteIniciadoCad():
        global contadorAtual
        testeIniciado.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarCad, btnParar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        page.update()

    def erroTesteIniciado(tipo, err):
        global pararLoop
        global contadorAtual
        page.clean()
        def fechaErr(e):
            erro.open = False
            page.add(testeIniciado)
            parar(e)

        erro = ft.AlertDialog(
            modal=True,
            bgcolor="#0d1935",
            title=ft.Text("Ocorreu um erro durante a automação"),
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[ft.Text(f"Erro ocorrido na execução {contadorAtual} da automação:"),
                          ft.Text(str(tipo)),
                          ft.Text(str(err))],
                height=200
            ),
            actions=[
                ft.ElevatedButton("OK",color=ft.colors.WHITE, bgcolor=ft.colors.RED, on_click=fechaErr)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.overlay.append(erro)
        erro.open = True
        pararLoop = True
        page.update()

    def erroTesteIniciadoCad(tipo, err):
        global pararLoop
        global contadorAtual
        page.clean()
        def fechaErr(e):
            erro.open = False
            page.add(testeIniciadoCad)
            parar(e)
        erro = ft.AlertDialog(
            modal=True,
            bgcolor="#0d1935",
            title=ft.Text("Ocorreu um erro durante a automação"),
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[ft.Text(f"Erro ocorrido na execução {contadorAtual} da automação:"),
                          ft.Text(str(tipo)),
                          ft.Text(str(err))],
                height=200
            ),
            actions=[
                ft.ElevatedButton("OK",color=ft.colors.WHITE, bgcolor=ft.colors.RED, on_click=fechaErr)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.overlay.append(erro)
        erro.open = True
        pararLoop = True
        page.update()

    def iniciar(e):
        global testeEscolhido
        global contadorAtual
        global pararLoop
        global cad
        pararLoop = False
        if cad:
            cadastrar(e)
        if testesPossiveis.value == "" and testes.value == "":
            errTeste(e)
        else:
            if testeEscolhido is None:
                testeEscolhido = testesPossiveis.value
                contadorAtual = 1
                page.clean()
                testeIniciado.content = ft.Container(
                content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarTeste, btnParar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
                width=400,
                padding=10,
            )
                page.add(testeIniciado)
            match testeEscolhido:
                case "Emitentes":
                    contador = SiaWebInstancia.cadEmitentes(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Produtos":
                    contador = SiaWebInstancia.cadProdutos(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Operações":
                    contador = SiaWebInstancia.cadOperacoes(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Vendedores":
                    contador = SiaWebInstancia.cadVendedores(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Plano de contas":
                    contador = SiaWebInstancia.cadPlanoContas(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Formas de pagamento":
                    contador = SiaWebInstancia.cadPagamentos(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Planos de pagamento":
                    contador = SiaWebInstancia.cadPlanoPag(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Transportadoras":
                    contador = SiaWebInstancia.cadTransportadora(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Intermediadores":
                    contador = SiaWebInstancia.cadIntermediadores(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Bancos":
                    contador = SiaWebInstancia.cadBancos(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Adm. Cartão":
                    contador = SiaWebInstancia.cadAdmCartao(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Vendas":
                    contador = SiaWebInstancia.cadVendas(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Saída devolução":
                    contador = SiaWebInstancia.cadSaidaDev(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Entrada devolução":
                    contador = SiaWebInstancia.cadEntradaDev(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Outras operações":
                    contador = SiaWebInstancia.cadOutrasOpe(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Compras":
                    contador = SiaWebInstancia.cadCompras(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Controle de estoque":
                    contador = SiaWebInstancia.cadEstoque(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Fluxo de Caixa":
                    contador = SiaWebInstancia.cadFluxoCaixa(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Contas a pagar":
                    contador = SiaWebInstancia.cadContasPagar(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Contas a receber":
                    contador = SiaWebInstancia.cadContasReceber(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório produtos":
                    contador = SiaWebInstancia.relProdutos(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório emitentes":
                    contador = SiaWebInstancia.relEmitentes(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório vendedores":
                    contador = SiaWebInstancia.relVendedores(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório transportadoras":
                    contador = SiaWebInstancia.relTransportadoras(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório intermediadores":
                    contador = SiaWebInstancia.relIntermediadores(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório movimentações":
                    contador = SiaWebInstancia.relMovimentacoes(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório contas a receber":
                    contador = SiaWebInstancia.relContasReceber(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório contas a pagar":
                    contador = SiaWebInstancia.relContasPagar(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório caixa":
                    contador = SiaWebInstancia.relCaixa(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório entrada mercadorias":
                    contador = SiaWebInstancia.relEntradaMerc(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório saida mercadorias":
                    contador = SiaWebInstancia.relSaidaMerc(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório plano de contas":
                    contador = SiaWebInstancia.relPlanoContas(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case "Relatório comissão por vendedores":
                    contador = SiaWebInstancia.relComissao(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[1], dados[2])
                case _:
                    errTeste(e)

        

    page.title = "Automação Sia Web"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    intervaloSec = ft.TextField(label="Digite o intervalo de tempo entre teclas:",
                                width=400,
                                focused_border_color="#cf6317",
                                border_color=ft.colors.GREY_700,
                                input_filter=ft.InputFilter(allow=True,regex_string=r"[1-9]",replacement_string="")
                                )
    intervaloExe = ft.TextField(label="Digite o intervalo de tempo entre execução do processo:",
                                width=400,
                                focused_border_color="#cf6317",
                                border_color=ft.colors.GREY_700,
                                input_filter=ft.InputFilter(allow=True,regex_string=r"[1-9]",replacement_string="")
                                )
    email = ft.TextField(label="Digite seu email:",
                        width=400,
                        focused_border_color="#cf6317",
                        border_color=ft.colors.GREY_700
                        )
    senha = ft.TextField(label="Digite sua senha:",
                        width=400,
                        focused_border_color="#cf6317",
                        border_color=ft.colors.GREY_700,
                        password=True,
                        can_reveal_password=True
                        )
    testes = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            on_change=pegaTestes,
                            options=[
                                ft.dropdown.Option("Cadastros"),
                                ft.dropdown.Option("Movimentações"),
                                ft.dropdown.Option("Financeiro"),
                                ft.dropdown.Option("Relatórios")
                            ],
                            )
    testesCad = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            options=[
                                ft.dropdown.Option("Emitentes"),
                                ft.dropdown.Option("Produtos"),
                                ft.dropdown.Option("Operações"),
                                ft.dropdown.Option("Vendedores"),
                                ft.dropdown.Option("Plano de contas"),
                                ft.dropdown.Option("Formas de pagamento"),
                                ft.dropdown.Option("Planos de pagamento"),
                                ft.dropdown.Option("Transportadoras"),
                                ft.dropdown.Option("Intermediadores"),
                                ft.dropdown.Option("Bancos"),
                                ft.dropdown.Option("Adm. Cartão"),
                            ],
                            )
    testesMov = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            options=[
                                ft.dropdown.Option("Vendas"),
                                ft.dropdown.Option("Saída devolução"),
                                ft.dropdown.Option("Entrada devolução"),
                                ft.dropdown.Option("Outras operações"),
                                ft.dropdown.Option("Compras"),
                                ft.dropdown.Option("Controle de estoque"),
                            ],
                            )
    testesFin = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            options=[
                                ft.dropdown.Option("Fluxo de Caixa"),
                                ft.dropdown.Option("Contas a pagar"),
                                ft.dropdown.Option("Contas a receber")
                            ]
                            )
    
    testesRel = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            options=[
                                ft.dropdown.Option("Relatório produtos"),
                                ft.dropdown.Option("Relatório emitentes"),
                                ft.dropdown.Option("Relatório vendedores"),
                                ft.dropdown.Option("Relatório transportadoras"),
                                ft.dropdown.Option("Relatório intermediadores"),
                                ft.dropdown.Option("Relatório movimentações"),
                                ft.dropdown.Option("Relatório contas a receber"),
                                ft.dropdown.Option("Relatório contas a pagar"),
                                ft.dropdown.Option("Relatório caixa"),
                                ft.dropdown.Option("Relatório entrada mercadorias"),
                                ft.dropdown.Option("Relatório saida mercadorias"),
                                ft.dropdown.Option("Relatório plano de contas"),
                                ft.dropdown.Option("Relatório comissão por vendedores"),
                            ]
                            )


    btnProx = ft.ElevatedButton("Proximo",color=ft.colors.WHITE, bgcolor="#cf6317", on_click=prox)
    btnLogin = ft.ElevatedButton("Proximo",color=ft.colors.WHITE, bgcolor="#cf6317", on_click=logar)
    btnSair = ft.ElevatedButton("Sair",color=ft.colors.WHITE, bgcolor="#cf6317",on_click=sair)
    btnVoltarLogin = ft.ElevatedButton("Voltar", color=ft.colors.WHITE, bgcolor="#cf6317", on_click=voltarLogin)
    btnIniciar = ft.ElevatedButton("Iniciar",color=ft.colors.WHITE, bgcolor="#cf6317",on_click=iniciar)
    btnParar = ft.ElevatedButton("Parar", color=ft.colors.WHITE, bgcolor="#cf6317",on_click=parar)
    btnPararCad = ft.ElevatedButton("Parar", color=ft.colors.WHITE, bgcolor="#cf6317",on_click=pararCad)
    btnCont = ft.ElevatedButton("Continuar", color=ft.colors.WHITE, bgcolor="#cf6317", on_click=continuar)
    btnContCad = ft.ElevatedButton("Continuar", color=ft.colors.WHITE, bgcolor="#cf6317", on_click=continuarCad)
    btnVoltarTeste = ft.ElevatedButton("Voltar",color=ft.colors.WHITE,bgcolor="#cf6317",on_click=voltarTeste)
    btnVoltarCad = ft.ElevatedButton("Voltar",color=ft.colors.WHITE,bgcolor="#cf6317",on_click=prox)

    inicio =ft.Card(
        width=500,
        color="#0d1935",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ACCESS_TIME,color="#cf6317"),
                        title=ft.Text("Iniciando processo de automação de testes do sia Web!"),
                        subtitle=ft.Text(
                            "Intervalo de tempo entre teclas (em segundos):"
                        ),
                    ),
                    ft.Row(
                        [intervaloSec],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ACCESS_TIME,color="#cf6317"),
                        subtitle=ft.Text(
                            "Intervalo de tempo entre execuções do processo (em segundos):",
                        ),
                        
                    ),
                    ft.Row(
                        [intervaloExe],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [btnProx, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    logCad = ft.AlertDialog(
        modal=True,
        bgcolor="#0d1935",
        title=ft.Text("Login e cadastro Sia Web"),
        content=ft.Text("Deseja logar ou cadastrar no sia Web"),
        actions=[
            ft.ElevatedButton("Login",color=ft.colors.WHITE, bgcolor="#cf6317",on_click=login),
            ft.ElevatedButton("Cadastrar",color=ft.colors.WHITE, bgcolor="#cf6317", on_click=cadastrar),
            ft.ElevatedButton("Voltar",color=ft.colors.WHITE, bgcolor=ft.colors.RED, on_click=voltarLogCad)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


    login = ft.Card(
        width=500,
        color="#0d1935",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PEOPLE,color="#cf6317"),
                        title=ft.Text("Login no Sia Web"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PEOPLE,color="#cf6317"),
                        title=ft.Text("Email"),
                        ),
                    ft.Row(
                        [email],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PASSWORD,color="#cf6317"),
                        title=ft.Text(
                            "Senha:",
                            no_wrap=True
                        ),
                    ),
                    ft.Row(
                        [senha],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [btnLogin, btnVoltarLogin],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
    teste = ft.Card(
        width=500,
        color="#0d1935",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Testes do Sia Web"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Teste de:"),
                    ),
                    ft.Row(
                        [testes],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Qual teste:")
                    ),
                    ft.Row(
                        [testesPossiveis],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [btnIniciar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    testeIniciado = ft.Card(
        width=500,
        color="#0d1935",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Testes iniciado"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED, color="#cf6317"),
                        title=ft.Text("Numero de execuções:"),
                    ),
                    ft.Row(
                        [ft.Text(value=str(contadorAtual))],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        [btnVoltarTeste, btnParar, btnSair],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    testeIniciadoCad = ft.Card(
            width=500,
            color="#0d1935",
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PEOPLE, color="#cf6317"),
                            title=ft.Text("Testes iniciado"),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PEOPLE, color="#cf6317"),
                            title=ft.Text("Numero de execuções:"),
                        ),
                        ft.Row(
                            [ft.Text(value=str(contadorAtual))],
                            alignment=ft.MainAxisAlignment.CENTER,
                            
                        ),
                        ft.Row(
                            [btnVoltarCad, btnPararCad, btnSair],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )


    page.add(inicio)

ft.app(main)