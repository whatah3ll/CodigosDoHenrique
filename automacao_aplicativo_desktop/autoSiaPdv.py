from classe.SiaPdvClass import SiaPdvClass
import flet as ft
import time
testesPossiveis = None
testeEscolhido = None
contadorAtual = 1
pararLoop = False
cad = False

def main(page: ft.page):
    SiaPdvInstancia = SiaPdvClass()

    def attTeste(testeMudado):
        global testesPossiveis
        if testeMudado == "Vendas":
            testesPossiveis = testesVenda
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
        page.window_destroy()
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

    def avisoCont(e):
        def fechaAviso(e):
            aviso.open = False
            page.update()
            time.sleep(1)
            continuar(e)
            
        aviso = ft.AlertDialog(
            modal=True,
            bgcolor="#0d1935",
            title=ft.Text("Aviso IMPORTANTE!"),
            content=ft.Column(
                controls=[ft.Text(f"Caso o processo esteja acima de 1 execução mantenha na tela de venda antes de continuar, caso contrário mantenha o processo com o caixa fechado e na tela inicial do Sia pdv"),],
                height=100
            ),
            actions=[
                ft.ElevatedButton("OK", color=ft.colors.WHITE, bgcolor=ft.colors.RED, on_click=fechaAviso)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = aviso
        aviso.open = True
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
            page.dialog = err
            err.open = True
            page.update()
        else:
            intervaloTeclas = int(intervaloSec.value)
            intervaloExec = int(intervaloExe.value)
            page.clean()
            page.add(teste)

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
        page.dialog = err
        err.open = True
        page.update()

    def voltarTeste(e):
        global pararLoop
        global testeEscolhido
        testeEscolhido = None
        pararLoop = True
        page.clean()
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
        page.dialog = erro
        erro.open = True
        pararLoop = True
        page.update()

    def aviso(e):
        def fechaAviso(e):
            aviso.open = False
            page.update()
            time.sleep(1)
            iniciar(e)
            
        aviso = ft.AlertDialog(
            modal=True,
            bgcolor="#0d1935",
            title=ft.Text("Aviso IMPORTANTE!"),
            content=ft.Column(
                controls=[ft.Text(f"Garanta que o Sia Pdv esteja aberto e com o caixa fechado(caixa fechado somente se for a primeira execução)!!"),
                            ft.Text(f"OBS: Caso queira parar a automação, apenas mova o mouse para a parte superior esquerda da tela ou use a interface")],
                height=100
            ),
            actions=[
                ft.ElevatedButton("OK", color=ft.colors.WHITE, bgcolor=ft.colors.RED, on_click=fechaAviso)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = aviso
        aviso.open = True
        page.update()

    def iniciar(e):
        global testeEscolhido
        global contadorAtual
        global pararLoop
        global cad
        pararLoop = False
        if testesPossiveis.value == "" and testes.value == "":
            errTeste(e)
        else:
            # Depois que o botão "OK" for clicado, continua aqui
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
                case "Venda padrão":
                    contador = SiaPdvInstancia.vendaPadrão(intervaloTeclas, intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case "Venda 100 produtos":
                    contador = SiaPdvInstancia.venda100Prod(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case "Venda 200 produtos":
                    contador = SiaPdvInstancia.venda200Prod(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case "Cancelamento venda":
                    contador = SiaPdvInstancia.cancelaVenda(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case "Extras e financeiro":
                    contador = SiaPdvInstancia.extraFinan(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case "Cancelamento de produto":
                    contador = SiaPdvInstancia.cancelaProd(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case "Cancelamento da ultima venda":
                    contador = SiaPdvInstancia.cancelaUltimaVenda(intervaloTeclas,intervaloExec, pararLoop, contadorAtual)
                    for dados in contador:
                        if pararLoop:
                            break
                        if dados[0] == "contador":
                            contadorAtual = dados[1]
                            atualizarTesteIniciado()
                        else:
                            erroTesteIniciado(dados[0], dados[1])
                case _:
                    errTeste(e)
        

    page.title = "Automação Sia Pdv"
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
    testes = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            on_change=pegaTestes,
                            options=[
                                ft.dropdown.Option("Vendas"),
                            ],
                            )
    testesVenda = ft.Dropdown(label="Escolha qual teste você deseja fazer",
                            width=400,
                            options=[
                                ft.dropdown.Option("Venda padrão"),
                                ft.dropdown.Option("Venda 100 produtos"),
                                ft.dropdown.Option("Venda 200 produtos"),
                                ft.dropdown.Option("Cancelamento venda"),
                                ft.dropdown.Option("Extras e financeiro"),
                                ft.dropdown.Option("Cancelamento de produto"),
                                ft.dropdown.Option("Cancelamento da ultima venda"),
                            ],
                            )

    btnProx = ft.ElevatedButton("Proximo",color=ft.colors.WHITE, bgcolor="#cf6317", on_click=prox)
    btnSair = ft.ElevatedButton("Sair",color=ft.colors.WHITE, bgcolor="#cf6317",on_click=sair)
    btnIniciar = ft.ElevatedButton("Iniciar",color=ft.colors.WHITE, bgcolor="#cf6317",on_click=aviso)
    btnParar = ft.ElevatedButton("Parar", color=ft.colors.WHITE, bgcolor="#cf6317",on_click=parar)
    btnCont = ft.ElevatedButton("Continuar", color=ft.colors.WHITE, bgcolor="#cf6317", on_click=avisoCont)
    btnVoltarTeste = ft.ElevatedButton("Voltar",color=ft.colors.WHITE,bgcolor="#cf6317",on_click=voltarTeste)

    inicio =ft.Card(
        width=500,
        color="#0d1935",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ACCESS_TIME,color="#cf6317"),
                        title=ft.Text("Iniciando processo de automação de testes do Sia Pdv"),
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


    teste = ft.Card(
        width=500,
        color="#0d1935",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FORMAT_LIST_BULLETED,color="#cf6317"),
                        title=ft.Text("Testes do Sia pdv"),
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



    page.add(inicio)

ft.app(main)