from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import pyautogui

class SiaWebClass:

    def __init__(self):
        service = Service(r"\siaWeb\operaPath\operadriver_win64\operadriver.exe")
        options = Options()
        options.binary_location = r"\AppData\Local\Programs\Opera\opera.exe"
        options.add_experimental_option('w3c', True)

        self.nav = webdriver.Chrome(service=service, options=options)

    def loginSiaWeb(self,user,senha,intervaloTecla):
        try:
            self.nav.get("")#url removido por questões de proteção da LGPD
            inputLogin = WebDriverWait(self.nav, 10).until(
            EC.presence_of_element_located((By.ID, "form-input-email"))# esperando a input aparecer
            )
            inputLogin.send_keys(str(user))# digita o e-mail
            time.sleep(intervaloTecla)
            self.nav.find_element(By.ID, "form-input-password").send_keys(str(senha))# digita a senha
            time.sleep(intervaloTecla)
            botaoLogin = WebDriverWait(self.nav, 3).until(# espera o botão aparecer
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/main/div[2]/div/form/div/button'))
            )
            botaoLogin.click()# clica no botão login
            try:
                botaoSair = WebDriverWait(self.nav, 3).until(# espera o botão de sair de outro dispositivo caso tiver logado
                EC.presence_of_element_located((By.XPATH, '//button[text()="Deslogar do outro dispositivo"]'))
                )
                botaoSair.click()# clica no botão sair
            except Exception:
                print("Conta não logada em outro usuário")
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro

    def cadastroSiaWeb(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            cnpj = SiaWebClass.geraCnpj
            cpf = SiaWebClass.geraCpf
            while not pararLoop:
                print("entro no while")
                self.nav.get("") # #url removido por questões de proteção da LGPD
                try:
                    linkCad = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[text()='Não tem uma conta? Faça seu cadastro']"))
                    )
                    linkCad.click()
                except Exception as e:
                    print(f"Erro ao clicar em linkCad: {e}")
                    continue

                try:
                    inpEmail = WebDriverWait(self.nav, 3).until(
                        EC.presence_of_element_located((By.ID, "email"))
                    )
                    inpEmail.send_keys(f"teste{contador}@gmail.com")
                except Exception as e:
                    print(f"Erro ao preencher o email: {e}")
                    yield "err", type(e), e
                time.sleep(intervaloTecla)
                try:
                    self.nav.find_element(By.XPATH, "//button[text()='Experimentar por ']").click()
                except Exception as e:
                    print(f"Erro ao clicar no botão experimentar: {e}")
                    yield "err", type(e), e
                time.sleep(intervaloTecla + 1)
                try:
                    emailRepetido = WebDriverWait(self.nav, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Criar uma conta com um novo e-mail']"))
                    )
                    if emailRepetido is not None:
                        contador += 1
                        continue
                except Exception as e:
                    print(f"Erro ao lidar com emailRepetido: {e}")
                try:
                    print("input")
                    inpNome = WebDriverWait(self.nav, 3).until(
                        EC.element_to_be_clickable((By.ID, "form-input-NOME"))
                    )
                    inpNome.send_keys(f"teste{contador}")
                except Exception as e:
                    print(f"Erro ao preencher o nome: {e}")
                    continue

                time.sleep(intervaloTecla)
                try:
                    self.nav.find_element(By.ID, "form-input-SENHA").send_keys(f"Teste{contador}!!")
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-input-_confirmar_senha").send_keys(f"Teste{contador}!!")
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Próximo']").click()
                    time.sleep(intervaloTecla + 1)
                    self.nav.find_element(By.ID, "cadastro-input-razao").send_keys(f"teste{contador}")
                    time.sleep(intervaloTecla)
                    if contador % 2 == 0:
                        self.nav.find_element(By.ID, "form-masked-field-CPF_CNPJ").send_keys(cpf())
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-masked-field-TELEFONE").send_keys(str(contador) * 11)
                    else:
                        self.nav.find_element(By.ID, "form-masked-field-CPF_CNPJ").send_keys(cnpj())
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-masked-field-TELEFONE").send_keys(str(contador) * 10)
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-masked-field-CEP").send_keys(str(contador) * 8)
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-UF").click()
                    time.sleep(intervaloTecla + 1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").clear()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").send_keys("MG")
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").send_keys(Keys.ENTER)
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-ID_CIDADE").click()
                    time.sleep(intervaloTecla + 1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade']").clear()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade']").send_keys("lavras")
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade']").send_keys(Keys.ENTER)
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-checkbox-ACEITE_TERMO_USO").click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Iniciar teste grátis']").click()
                    btnCadastrar = WebDriverWait(self.nav, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Cadastrar']"))
                    )
                    btnCadastrar.click()
                    btnOK = WebDriverWait(self.nav, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
                    )
                    btnOK.click()
                    contador += 1
                    yield "contador", contador # Envia o valor do contador para a tela
                    time.sleep(intervaloExec)
                    if pararLoop: # Teste para parar o loop
                        break
                except Exception as e:
                    print("Ocorreu um erro")
                    print(type(e))
                    print(e)
                    yield "err", type(e), e
                    break
        except Exception as e:
            print("Ocorreu um erro no loop principal")
            print(type(e))
            print(e)
            yield "err", type(e), e

    def cadEmitentes(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            tipoPessoa = 1
            while not pararLoop:
                if tipoPessoa > 3:
                    tipoPessoa = 1
                cpf = SiaWebClass.geraCpf
                cnpj = SiaWebClass.geraCnpj
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") # muda para o cadastro de emitentes #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                time.sleep(intervaloTecla)
                inpCPF = WebDriverWait(self.nav, 3).until(
                    EC.presence_of_element_located((By.ID, "form-masked-field-CPF_CNPJ"))# espera a input aparecer
                )
                if contador % 2 == 0: # teste para alternar entre cpf e cnpj
                    inpCPF.send_keys(cpf()) # digita o cpf
                else:
                    inpCPF.send_keys(cnpj()) # digita o cnpj
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-IE").send_keys(str(contador))# digita o RG ou o IE com o contador só para manter o padrão
                time.sleep(intervaloTecla)
                if contador % 2 == 0: # teste para alternar entre pessoa fisica e juridica
                    self.nav.find_element(By.ID, "form-input-NOME_RS").send_keys("teste" + str(contador))# digita o padrão para testes nna razão social
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder = "dd/mm/yyyy"]').send_keys(str("08022005"))# digita data de nascimento
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-input-NOME_PAI").send_keys("pai" + str(contador))# digita nome pai
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-input-NOME_MAE").send_keys("mae" + str(contador))# digita nome mae
                    time.sleep(intervaloTecla)
                else:
                    self.nav.find_element(By.ID, "form-input-NOME_RS").send_keys(str("teste" + str(contador)))# digita o padrão para testes nna razão social
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder = "dd/mm/yyyy"]').send_keys(str("08022005"))# digita data de nascimento
                    time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-TELEFONE").send_keys(str(contador) * 10)# digita o padrão para numero de telefone
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-CELULAR").send_keys(str(contador) * 11)# digita o padrão para numero de telefone
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-EMAIL").send_keys("teste" + str(contador) + "@gmail.com")# digita o email
                time.sleep(intervaloTecla)
                if tipoPessoa == 2:
                    self.nav.find_element(By.ID, "form-select-TIPO").click()# clique no tipo pessoa
                    time.sleep(intervaloTecla)
                    pyautogui.press("down")#Selciona a opção fornecedor
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter")#aperta enter na opção
                elif tipoPessoa == 3:
                    self.nav.find_element(By.ID, "form-select-TIPO").click()# clique no tipo pessoa
                    time.sleep(intervaloTecla)
                    pyautogui.press("down",presses=10)#Selciona a opção ambos
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter")#aperta enter na opção
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-SUFRAMA").send_keys("teste" + str(contador))# digita o SUFRAMA
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-switch-ATIVO").click()# desativa o emitente ativo
                time.sleep(intervaloTecla)                    
                self.nav.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Informe uma observação"]').send_keys("teste"+str(contador))#Digita observação
                time.sleep(intervaloTecla)
                if contador % 2 == 0:
                    self.nav.find_element(By.ID, "form-checkbox-PRODUTOR_RURAL").click()# seleciona a opção de produtor rural
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-checkbox-CLIENTE_ESPECIAL").click()# seleciona a opção de cliente especial
                    time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-CEP").send_keys(str(contador) * 8)# digita o cep com o padão do contador
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-UF").click()# abre a lista de UF
                time.sleep(intervaloTecla + 1)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').clear()# apaga caso tiver linhas já escritas
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').send_keys("MG")# digitao estado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').send_keys(Keys.ENTER)# seleciona o estado
                time.sleep(intervaloTecla + 1)
                # self.nav.find_element(By.ID, "form-auto-complete-ID_CIDADE").click()
                inputCidade = WebDriverWait(self.nav, 10).until(
                EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_CIDADE"))# espera o botão de abrir o list ser clicavel
                )
                inputCidade.click()# clica no botão de abrir o list
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').clear()# apaga caso tiver linhas já escitas
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').send_keys("lavras")# digita a cidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').send_keys(Keys.ENTER)# seleciona a cidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, 'form-input-ENDERECO').send_keys("teste"+str(contador))# digita o endereço como padrão teste
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, 'form-numeric-format-NUMERO').send_keys(str(contador))# digita o numero como padrão contador
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, 'form-input-BAIRRO').send_keys("teste"+str(contador))# digita o bairro com o padrão teste
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, 'form-input-COMPLEMENTO').send_keys("teste"+str(contador))# digita o complemento com o padrão teste
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Salvar e Inserir"]').click()# salva e abre outro formulario para preencher
                contador += 1
                tipoPessoa += 1
                yield "contador", contador# envia o valor do contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para para o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e
    
    def cadProdutos(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") # muda para a pagina de produtos #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                time.sleep(intervaloTecla + 1)
                # self.nav.find_element(By.XPATH, '//*[@id="produto-form-base"]/div/div[3]/div[1]/div/div[2]/div/button').click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "grupo-input-descricao").send_keys("teste" + str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, 'formularios-button-salvar').click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, '//*[@id="produto-form-base"]/div/div[3]/div[2]/div/div[2]/div/button').click
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, 'form-input-DESCRICAO').send_keys("teste" + str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-auto-complete-ID_GRUPO").click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição do grupo"]').send_keys("teste" + str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "formularios-button-salvar").click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, '//*[@id="produto-form-base"]/div/div[3]/div[3]/div/div[2]/div/button').click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-input-DESCRICAO").send_keys("teste" + str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-auto-complete-ID_CATEGORIA").click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione a categoria"]').send_keys("teste" + str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "formularios-button-salvar").click()
                # time.sleep(intervaloTecla)
                btnEAN = WebDriverWait(self.nav, 3).until(# espera o botão EAN aparecer
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="produto-form-base"]/div/div[2]/div[1]/div[2]/div/button[1]'))
                    )
                btnEAN.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-DESCRICAO").clear()# Apaga tudo que estiver escrito na descrição
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-DESCRICAO").send_keys("teste" + str(contador))# digita a descrição do produto com padrão teste
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_GRUPO").click()# abre a lista de grupos
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição do grupo"]').clear()# apaga o que já estiver no codigo do grupo
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição do grupo"]').send_keys(Keys.ENTER)# e seleciona o grupo
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_CATEGORIA").click()# abre a lista de categorias
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição da categoria"]').clear()# apaga o que ja estiver no codigo da categoria
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição da categoria"]').send_keys(Keys.ENTER)# seleciona a categoria
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_FAMILIA").click()# abre a lista de familia
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição da família"]').clear()# apaga o que ja estiver no codigo da familia
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite o código ou a descrição da família"]').send_keys(Keys.ENTER)# seleciona a familia
                time.sleep(intervaloTecla)
                if contador % 2 == 0:
                    self.nav.find_element(By.ID, "form-auto-complete-UNIDADE").click()# abre a lista de unidades
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a descrição da unidade"]').clear()# Digita a unidade
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a descrição da unidade"]').send_keys("QUILOGRAMA")# Digita a unidade
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a descrição da unidade"]').send_keys(Keys.ENTER)# seleciona a unidade
                    time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-QTD_ESTOQUE").click()# seleciona a input de estoque
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-QTD_ESTOQUE").send_keys(str(contador))# digita a quantidade em estoque
                time.sleep(intervaloTecla)
                if not contador % 2 == 0:    
                    self.nav.find_element(By.ID, "form-switch-ATIVO").click()# aperta o botão de produto ativo
                    time.sleep(intervaloTecla)
                elif contador % 2 == 0:
                    self.nav.find_element(By.ID, "produto-input-PESAVEL").click()# aperta o botão de produto pesavel
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-switch-ENVIA_PDV").click()# aperta o botão de enviar produto para o pdv
                    time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH,'//button[text()="Preços e Custo"]').click()# clica no botão preços e custos
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-PRC_CUSTO").click()# seleciona a input de preço de custo
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-PRC_CUSTO").send_keys(str(contador))# digita o preço de custo
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-MARGEM").click()# seleciona a input da margem
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-MARGEM").send_keys(str(contador))# digita a margem
                time.sleep(intervaloTecla)
                if contador % 2 == 0:
                    self.nav.find_element(By.ID, "form-numeric-format-PRECO_PROMOCAO").click()# seleciona a input de preço da promoção
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-PRECO_PROMOCAO").send_keys(str(contador))# digita o preço da promoção
                    time.sleep(intervaloTecla)
                datasPromo = self.nav.find_elements(By.CSS_SELECTOR, 'input[placeholder="dd/mm/yyyy"')# Pega as inputs
                for dataInput in datasPromo:# e digita em cada uma dela
                    dataInput.send_keys("08022005")
                    time.sleep(intervaloTecla)
                if contador % 2 == 0:
                    self.nav.find_element(By.XPATH,'//button[text()="Balança"]').click()# clica no botão da balança
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma informação nutricional"]').send_keys(Keys.ENTER)# digita o id da informação nutricional
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-VALIDADE_ETIQUETA").send_keys("30")# digita a validade da etiqueta
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-TECLA").send_keys(str(contador))# digita o atalho de tecla para o produto
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Salvar e Inserir"]').click()# Salva e inseri
                try:
                    botaoDupla = WebDriverWait(self.nav, 3).until(# espera o botão de descrição duplicada aparecer
                    EC.presence_of_element_located((By.XPATH, "//button[text()='Sim']"))
                    )
                    time.sleep(5)
                    botaoDupla.click()# clica nele
                except:
                    print("Descrição do produto não existe")
                contador += 1
                yield "contador", contador # manda o valor do contador para a tela
                time.sleep(intervaloExec)
                if pararLoop: # teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadOperacoes(self,intervaloTecla,intervaloExec, pararLoop, contador):
        try:
            operacao = 1
            conta = 1
            while not pararLoop:
                if operacao > 6: # teste para resetar o operção para 1
                    operacao = 1
                if conta > 4: # teste para resetar a conta para 1
                    conta = 1
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD 
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:    
                    self.nav.get("") # muda para a pagina de operações #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                time.sleep(5)
                btnOpe = WebDriverWait(self.nav, 3).until(# espera o botão aparecer
                    EC.presence_of_element_located((By.ID, "form-auto-complete-ID_TIPO_OPERACAO"))
                    )
                btnOpe.click() # clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione um tipo de operação"]').clear() # apaga tudo que já esta na lista
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione um tipo de operação"]').send_keys(str(operacao)) # Digita o id da operação
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione um tipo de operação"]').send_keys(Keys.ENTER) # e seleciona a operação 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_CONTA").click()# abre a lista de contas
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR , 'input[placeholder="Digite o código ou a descrição da conta"]').clear() # apaga tudo que ja estiver na input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR , 'input[placeholder="Digite o código ou a descrição da conta"]').send_keys(Keys.ENTER) # seleciona a conta
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR , 'textarea[placeholder="Informe a descrição"]').send_keys("teste" + str(contador)) # digita a descrição
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Salvar e Inserir"]').click() # salva e inseri
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
                    )
                    btnOk.click()
                except Exception as e:
                    print("Descrição não existente")
                contador += 1
                operacao += 1
                conta += 1
                yield "contador", contador # manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadVendedores(self, intervaloTecla, intervaloExec,pararLoop, contador):
        try:
            cpf = SiaWebClass.geraCpf
            while not pararLoop:
                if contador == 1:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("")# abre a pagina de vendedores #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                time.sleep(5)
                inpNome = WebDriverWait(self.nav, 3).until(# espera a input aparecer
                EC.presence_of_element_located((By.ID, "form-input-NOME"))
                )
                inpNome.send_keys("teste" + str(contador))# digita o nome do vendedor com o padrão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-CPF").send_keys(cpf())# digita o cpf
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-TELEFONE").send_keys(str(contador) * 11)# digita o telefone
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-PERCENTUAL_VENDA").click()# digita comissão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-PERCENTUAL_VENDA").send_keys(str(contador))# digita comissão
                time.sleep(intervaloTecla)
                if contador % 2 == 0:
                    self.nav.find_element(By.ID, "form-switch-ATIVO").click() # muda entre vendedor ativo e inativo
                    time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-CEP").send_keys(str(contador) * 8)# digita o CEP 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-UF").click() # abre o formulario de UF
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').clear() # apaga as linhas já existentes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').send_keys("MG")# digita o UF
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').send_keys(Keys.ENTER)# seleciona o UF
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_CIDADE").click()# abre o formulario de cidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').clear()# apaga as linhas já existentes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').send_keys("lavras")# digita a a cidade 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').send_keys(Keys.ENTER)# seleciona a cidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-input-ENDERECO").send_keys("teste" + str(contador))# digita o endereço com o padro
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-NUMERO").send_keys(str(contador))# digita o numero do endereço
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-BAIRRO").send_keys("teste" + str(contador))# digita o bairro
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-COMPLEMENTO").send_keys("teste" + str(contador))#digita o complemento 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Salvar e Inserir"]').click()# Salva e inseri
                contador += 1
                yield "contador", contador # manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop: # teste para parar o loop 
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadPlanoContas(self, intervaloTecla, intervaloExec,pararLoop, contador):
        try:
            plano = 1
            while not pararLoop:
                if plano == 4: # teste para resetar o plano
                    plano = 1
                if contador == 1:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") # abre a pagina de plano de contas #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                inp = WebDriverWait(self.nav, 3).until(
                    EC.presence_of_element_located((By.ID, "form-input-DESCRICAO")) # espera a input aparecer
                )
                time.sleep(intervaloTecla)
                inp.send_keys("teste" + str(contador)) # digita a descrição
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-select-TIPO").click()# abre o list de tipo
                time.sleep(intervaloTecla)
                match plano: # teste para escolher o plano
                    case 1:
                        pyautogui.press("enter")
                        time.sleep(intervaloTecla)
                    case 2:
                        pyautogui.press("down")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                        time.sleep(intervaloTecla)
                    # case 3:
                    #     pyautogui.press("down")
                    #     time.sleep(intervaloTecla)
                    #     pyautogui.press("down")
                    #     time.sleep(intervaloTecla)
                    #     pyautogui.press("enter")
                    #     time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Salvar e Inserir"]').click()# Salva e inseri
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer para clicar nele
                        )
                    time.sleep(5)
                    btnOk.click()# clica no botão
                    time.sleep(5)
                except Exception:
                    print("Descrição não existente") # caso não apareça só manda a mensagem no console
                contador += 1
                plano += 1
                yield "contador", contador # manda o contador para a tela
                time.sleep(intervaloExec)
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadPagamentos(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            formaPag = 1
            pix = 1
            while not pararLoop:
                if formaPag > 13:
                    formaPag = 1
                if pix > 3:
                    pix = 1
                if contador == 1:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") # abre a tela de formas de pagamento #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                inp = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "form-input-DESCRICAO")) # espera a input aparecer
                    )
                inp.send_keys("teste" + str(contador))# digita a descrição 
                time.sleep(intervaloTecla)
                inputTipo = WebDriverWait(self.nav, 10).until(
                EC.element_to_be_clickable((By.ID, "form-auto-complete-TIPO")) # espera o botão de abri a list aparecer
                )
                inputTipo.click()# clica no botão
                time.sleep(intervaloTecla)
                match formaPag: # teste para verificar a forma de pagamento especifica
                    case 1:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear() # limpa a input
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Dinheiro")# digita a forma de pagamento
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="1"]').click()# clica na forma de pagamento
                    case 2:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()# e assim por diante
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Cheque")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="2"]').click()
                    case 3:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Crédito em loja")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="21"]').click()
                    case 4:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Boleto Bancário")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="15"]').click()
                    case 5:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Depósito Bancário")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="16"]').click()
                    case 6:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("pagamento instantâneo (PIX) - Dinâmico")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="17"]').click()
                    case 7:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Transferência bancária, Carteira Digital")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="18"]').click()
                    case 8:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Programa de fidelidade, Cashback, Crédito Virtual")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="19"]').click()
                    case 9:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Sem Pagamento")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="90"]').click()
                    case 10:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Outros")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="99"]').click()
                    case 11:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Cartão")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="999999"]').click()
                    case 12:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("pagamento instantâneo (PIX) - Estático")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="20"]').click()
                    case 13:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").clear()
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a tipo de forma de pagamento']").send_keys("Cartão da Loja")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, '//div[@data-value="5"]').click()
                time.sleep(intervaloTecla)
                # if contador % 2 == 0:
                    # self.nav.find_element(By.ID, "form-checkbox-DISPONIVEL_PDV").click()
                time.sleep(intervaloTecla)
                if formaPag == 6: # teste para caso a forma de pagamento seja em pix
                    match pix:
                        case 1:
                            self.nav.find_element(By.XPATH, "//input[@value='F']").click() # seleciona a opção pix por fora
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.ID, "form-auto-complete-ID_BANCO_PIX").click()# abre a lista de bancos
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").clear() # limpa tudo que estiver na input
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys("pense bank") # digita o id do banco
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys(Keys.ENTER) # seleciona o banco
                        case 2:
                            self.nav.find_element(By.XPATH, "//input[@value='T']").click() # seleciona a opção pix tef  
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.ID, "form-auto-complete-ID_BANCO_PIX").click() # faz a operação do banco
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").clear()
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys("Pense bank")
                            time.sleep(intervaloTecla)
                            self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys(Keys.ENTER)
                        case 3:
                            try:
                                self.nav.find_element(By.XPATH, "//input[@value='C']").click() # seleciona o pix criare
                            except Exception:
                                print("Pix criare não habilitado")# para caso não fora habilitada a função
                    pix += 1
                elif formaPag == 11: # teste para caso a forma de pagamento seja cartão 
                    if contador % 2 == 0:
                        self.nav.find_element(By.XPATH, "//input[@value='P']").click() # seleciona a opção pos
                    else:
                        self.nav.find_element(By.XPATH, "//input[@value='T']").click() # seleciona a opção tef
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Salvar e Inserir"]').click()# Salva e inseri
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer para clicar nele
                        )
                    time.sleep(5)
                    btnOk.click()# clica no botão
                except Exception:
                    print("Descrição não existente") # caso não apareça só manda a msg no console
                contador += 1
                formaPag += 1
                yield "contador", contador # manda o contador para a tela
                time.sleep(intervaloExec)
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e
    
    def cadPlanoPag(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                if contador == 1:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") # abre a tela de planos de pagamento #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                inp = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "form-input-DESCRICAO"))# espera a input aparecer
                    )
                time.sleep(intervaloTecla)
                inp.send_keys("teste" + str(contador)) # digita a descrição
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-select-TIPO").click()# abre o list de tipo
                time.sleep(intervaloTecla)
                if contador % 2 == 0: # teste para alternar entre a vista e a prazo
                    pyautogui.press("up")# seleciona a opção de a vista
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter") 
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-DESCONTO").click() # seleciona a input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-DESCONTO").send_keys(contador)# digita o desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-ACRESCIMO").click() # seleciona a input de acrescimo
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-ACRESCIMO").send_keys("0") # zera para evitar erros
                    
                else:
                    pyautogui.press("down") # seleciona a opão de a prazo
                    time.sleep(intervaloTecla)
                    pyautogui.press("enter")
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-ACRESCIMO").click() # faz o mesmo para o acrescimo e desconto porém ao contrário
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-ACRESCIMO").send_keys(contador)
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-DESCONTO").click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-DESCONTO").send_keys("0")
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-NUMERO_PARCELA").send_keys(contador)# Digita o numero de parcelas
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-DIA_PRIMEIRA_PARCELA").send_keys(contador)# digita os dias até a primeira parcela
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-numeric-format-DIA_PARCELA").send_keys(contador)# digita os dias entre as parcelas
                time.sleep(intervaloTecla)
                try:
                    self.nav.find_element(By.CSS_SELECTOR, "input[aria-label='Selecionar todas linhas']").click() # seleciona todas as formas de pagamento
                except Exception:
                    print("Ja selecionado!")# para caso já estiver selecionado
                btnInserir = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de salvar e inserir aparecer
                    )
                actions = ActionChains(self.nav)
                actions.move_to_element(btnInserir).perform()# scrola até o botão
                time.sleep(intervaloTecla)
                btnInserir.click()# clica no botão
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer
                        )
                    time.sleep(5)
                    btnOk.click()# clica nele
                except Exception:
                        print("Descrição não existente") # para caso o erro não apareça
                contador += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except KeyboardInterrupt:
            print("tananan")
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadTransportadora(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            cnpj = SiaWebClass.geraCnpj
            while not pararLoop:
                if contador == 1:
                    self.nav.get("") # abre a pagina de transportadora #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") # abre a pagina de transportadora #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                inpCNPJ = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "form-masked-field-CNPJ")) # espera a input cnpj aparecer
                    )
                inpCNPJ.clear() # limpa a input
                time.sleep(intervaloTecla)
                inpCNPJ.send_keys(cnpj())# digita o cnpj
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-RAZAO").clear()# digita a razão social
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-RAZAO").send_keys("teste" + str(contador))# digita a razão social
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-input-IE").send_keys(str(contador)*7) # digita a inscrição estadual
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-TELEFONE").send_keys(str(contador)*11)# digita o telefone
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-masked-field-CEP").send_keys(str(contador)*8)# digita o CEP
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-UF").click()# abre a lista de UF
                time.sleep(intervaloTecla + 1)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').clear()# apaga caso tiver linhas já escritas
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Digite a sigla ou o nome do estado"]').send_keys("MG")# digitao estado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//div[@data-value="mg"]').click()# seleciona o estado
                time.sleep(intervaloTecla + 1)
                # self.nav.find_element(By.ID, "form-auto-complete-ID_CIDADE").click()
                inputCidade = WebDriverWait(self.nav, 10).until(
                EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_CIDADE"))# espera o botão de abrir o list ser clicavel
                )
                inputCidade.click()# clica no botão de abrir o list
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').clear()# apaga caso tiver linhas já escitas
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, 'input[placeholder="Selecione uma cidade de MG"]').send_keys("lavras")# digita a cidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//div[@data-value="3138203"]').click()# seleciona a cidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-LOGRADOURO").send_keys("teste" + str(contador))# digita o logradouro
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-NUMERO").click()# seleciona a input de numero
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-NUMERO").send_keys(str(contador))# digita o numero
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-BAIRRO").send_keys("teste" + str(contador))# digita o bairro
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-COMPLEMENTO").send_keys("teste" + str(contador))# digita o complemento
                time.sleep(intervaloTecla)
                btnInserir = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de salvar e inserir aparecer
                    )
                actions = ActionChains(self.nav)
                actions.move_to_element(btnInserir).perform()# scrola até o botão
                time.sleep(intervaloTecla)
                btnInserir.click()# clica no botão
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer
                        )
                    time.sleep(5)
                    btnOk.click()# clica nele
                except Exception:
                        print("Descrição não existente") # para caso o erro não apareça
                contador += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadIntermediadores(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            cnpj = SiaWebClass.geraCnpj
            while not pararLoop:
                if contador == 1:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                inpCNPJ = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "form-masked-field-CNPJ")) # espera a input cnpj aparecer
                    )
                inpCNPJ.clear() # limpa a input
                time.sleep(intervaloTecla)
                inpCNPJ.send_keys(cnpj()) # digita cnpj
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-NOME").clear() # limpa a input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-NOME").send_keys("teste" + str(contador))# digita o nome
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-ID_CAD_INTTRAN").clear() # limpa a input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-ID_CAD_INTTRAN").send_keys("teste" + str(contador))# digita a identificção do cadastro
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_EMITENTE").click()# abre a lista de emitentes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um emitente']").clear()# limpa a input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um emitente']").send_keys(Keys.ENTER)# digita o nome do emitente
                time.sleep(intervaloTecla + 1)
                btnInserir = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de salvar e inserir aparecer
                    )
                btnInserir.click()
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer
                        )
                    time.sleep(5)
                    btnOk.click()# clica nele
                except Exception:
                        print("Descrição não existente") # para caso o erro não apareça
                contador += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadBancos(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            cnpj = SiaWebClass.geraCnpj
            while not pararLoop:
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                btnBank = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "form-auto-complete-CODIGO")) # espera o botão aparecer
                        )
                btnBank.click()# clica no botão de abrir o list de bancos
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").clear() # limpa tudo que tiver na input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys("000")# digita o codigo do banco
                time.sleep(intervaloTecla+1)
                self.nav.find_element(By.XPATH, "//div[@data-value='000']").click()# clica no banco
                time.sleep(intervaloTecla+1)
                self.nav.find_element(By.ID,"form-masked-field-CNPJ").clear()# limpa tudo que tiver na input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-masked-field-CNPJ").send_keys(cnpj())# digita o cnpj do banco
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-input-NOME").clear()# limpa tudo que tiver na input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-input-NOME").send_keys("teste" + str(contador))# digita o nome do banco
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-masked-field-AGENCIA").send_keys(str(contador)*4)# digita a agencia
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-DIGITO_AGENCIA").send_keys(str(contador))# digita o digito da agencia
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-masked-field-CONTA").send_keys(str(contador)*8)# digita a conta
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-DIGITO_CONTA").send_keys(str(contador))# digita o digito da conta
                time.sleep(intervaloTecla)
                btnInserir = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de salvar e inserir aparecer
                    )
                btnInserir.click()# clica no botão
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer
                        )
                    time.sleep(5)
                    btnOk.click()# clica nele
                except Exception:
                        print("Descrição não existente") # para caso o erro não apareça
                contador += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadAdmCartao(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            meioPag = 1
            cnpj = SiaWebClass.geraCnpj
            while not pararLoop:
                if meioPag > 6:
                    meioPag = 1
                if contador == 1:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                        )
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                inpNome = WebDriverWait(self.nav, 10).until(
                            EC.presence_of_element_located((By.ID, "form-input-NOME")) # espera a input aparecer
                        )
                inpNome.clear()# limpa a input
                time.sleep(intervaloTecla)
                inpNome.send_keys("teste" + str(contador))# digita o nome do cartão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_BANCO").click()# abre o list de bancos
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").clear()# limpa a input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys(Keys.ENTER)# digita o nome do banco
                time.sleep(intervaloTecla+1)
                self.nav.find_element(By.ID, "form-auto-complete-INDICE_MEIO_PGTO_XML").click()# abre o list de indice de meio de pagamento
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").clear()# limpa a input
                time.sleep(intervaloTecla)
                match meioPag:# teste para alternar entre os indices
                    case 1:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").send_keys("Cartão de Crédito")# digita o nome do forma de pagamento
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, "//div[@data-value='3']").click()# clica no opção
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-numeric-format-NUM_MAX_PARCELA").click()# clica na input
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-numeric-format-NUM_MAX_PARCELA").send_keys(str(contador))# difita o numero de parcelas
                    case 2:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").send_keys("Cartão de Débito")# seleciona o tipo de pagamento
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, "//div[@data-value='4']").click()# clica na opção
                    case 3:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").send_keys("Vale Alimentação")# e assim por diante
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, "//div[@data-value='10']").click()
                    case 4:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").send_keys("Vale Refeição")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, "//div[@data-value='11']").click()
                    case 5:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").send_keys("Vale Presente")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, "//div[@data-value='12']").click()
                    case 6:
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um tipo']").send_keys("Vale Combustível")
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.XPATH, "//div[@data-value='13']").click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-masked-field-CNPJ_REDE").send_keys(cnpj())# digita o cnpj rede
                time.sleep(intervaloTecla)
                if contador % 2 == 0:
                    self.nav.find_element(By.ID, "form-switch-ATIVO").click()# desmarca a opção administradora ativa
                btnInserir = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de salvar e inserir aparecer
                    )
                btnInserir.click()# aperta o botão
                try:
                    btnOk = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='OK']")) # espera o botão de erro aparecer
                        )
                    time.sleep(5)
                    btnOk.click()# clica nele
                except Exception:
                        print("Descrição não existente") # para caso o erro não apareça
                contador += 1
                meioPag += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e


    def cadVendas(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            frete = 1
            while not pararLoop:
                if frete > 6:
                    frete = 1
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla+1)
                    btnNovo.click()# clica no botão
                    try:
                        btnPular = WebDriverWait(self.nav, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Pular']"))
                        )
                        time.sleep(intervaloTecla)
                        btnPular.click()
                    except Exception:
                        print("tutorial não exibido")
                else:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                try:
                    btnNao = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[text()='Não']"))# espera o botão de não salva aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNao.click()#Clica no botão
                except Exception:
                    print("Nenhum itém sem salvar!")    
                btnOpe = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_OPERACAO")) # espera o botão de mostrar o list aparecer
                        )
                btnOpe.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da operação']").clear()# limpa a input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da operação']").send_keys(Keys.ENTER)# digita a descrição da operação
                time.sleep(intervaloTecla)
                # btnCli = WebDriverWait(self.nav, 10).until(
                #             EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_EMITENTE")) # espera o botão aparecer
                #         )
                # btnCli.click()# clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um cliente']").clear()# limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um cliente']").send_keys("Consumidor final")# digita o cliente
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//div[@data-value='2141aabd-176e-11ef-8438-5254004a856f']").click()# Clica na opção
                # time.sleep(intervaloTecla+1)
                # btnVen = WebDriverWait(self.nav, 10).until(
                #             EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_VENDEDOR")) # espera o botão aparecer
                #         )
                # btnVen.click()# clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do vendedor']").clear()# limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do vendedor']").send_keys("padrao")# digita o vendedor
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//div[@data-value='21415c7a-176e-11ef-8438-5254004a856f']").click()# clica na opção
                # time.sleep(intervaloTecla+1)
                self.nav.find_element(By.XPATH, '//button[text()="Itens"]').click()# muda para a aba itens
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//button[text()='inserir novo item']").click()# inseri um novo item
                btnProd = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "ITENS.0.ID_PRODUTO")) # espera o botão aparecer
                        )
                btnProd.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do produto']").send_keys(Keys.ENTER)# seleciona o ultimo produto cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").click()# clica na input de quantidade 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").send_keys(str(contador))# digita a quantidade do item
                time.sleep(intervaloTecla)
                if contador % 2 == 0:#teste para alternar entre desconto e acrescimo
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").send_keys(str(contador))# Digita o desconto
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").click()# o mesmo que o desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").send_keys(str(contador))
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Observações"]').click()# muda para a aba observações
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe alguma observação sobre a movimentação']").send_keys("teste" + str(contador))# digita a observação
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Transportadora"]').click()# muda para a aba transportadora
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-select-TRANSPORTADOR.MODFRETE").click()# Clica no list de mod. frete contratado
                time.sleep(intervaloTecla)
                match frete:# teste para alternas no frete contratado
                    case 1:
                        pyautogui.press("enter")# seleciona a primeira opção
                        self.nav.find_element(By.ID, "form-auto-complete-TRANSPORTADOR.ID_TRANSPORTADOR").click()# # clica no list de tranportadoras
                        time.sleep(intervaloTecla+1)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma transportadora']").send_keys(Keys.ENTER)# escolhe a ultima transportadora cadastrada
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.PLACA_VEICULO").send_keys("teste" + str(contador))# digita a placa do veiculo
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.RNTC").send_keys("teste" + str(contador))# digita o RNTC
                    case 2:
                        pyautogui.press("1")# muda para a proxima opção
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")# e seleciona ela
                    case 3:
                        pyautogui.press("2")# assim por diante
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 4:
                        pyautogui.press("3")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 5:
                        pyautogui.press("4")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 6:
                        pyautogui.press("9")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Volumes"]').click()# muda para a aba volumes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.QVOL").send_keys(str(contador))# digita a quantidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.ESP").send_keys("teste" + str(contador))# digita a especie
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.MARCA").send_keys("teste" + str(contador))# digita a marca
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.NVOL").send_keys("teste" + str(contador))# digita o numero
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").click()# clica na input de peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").send_keys(str(contador))# digita o peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").click()# clica na input de peso bruto
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").send_keys(str(contador))# digita o peso bruto
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre desconto e acrescimo no totais de pedidos
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(str(contador))# digita o valor
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(Keys.ENTER)# seleciona o valor
                    try:
                        btnRatear = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Ratear']")) # espera o botão aparecer
                        )
                        time.sleep(intervaloTecla)
                        btnRatear.click()# clica nele
                    except Exception:
                        print("Botão ratear não apareceu!")
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").click()# o memo que o desconto para acrescimo
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(str(contador))
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(Keys.ENTER)
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre salvar e aprovar
                    self.nav.find_element(By.ID, "movimentacao-button-salvar").click()#clica no botão salvar
                    time.sleep(intervaloTecla)
                else:
                    self.nav.find_element(By.ID, "movimentacao-button-aprovar").click()# clica no botão aprovar
                    time.sleep(intervaloTecla)
                    btnAprovarPop = WebDriverWait(self.nav, 3).until(
                        EC.presence_of_element_located((By.XPATH,"//button[text()='Aprovar']"))# espera o botão aparecer
                    )
                    btnAprovarPop.click()# clica no botão
                    btnPag = WebDriverWait(self.nav, 10).until(
                        EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_PLANO_PAGAMENTO"))# espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnPag.click()# clica para aparecer o list
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona o plano de pagamento
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-ID_FORMA_PAGAMENTO").click()# abre o list de forma de pag
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona a forma de pag
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Adicionar pagamento']").click()# adiciona o pag
                    btnAprovar = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Aprovar"]'))# espera o botão de aprovar aparecer
                    )
                    actions = ActionChains(self.nav)
                    actions.move_to_element(btnAprovar).perform()# scrola até o botão
                    time.sleep(intervaloTecla)
                    btnAprovar.click()# clica no botão
                try:
                    btnEstoque = WebDriverWait(self.nav, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[text()='OK']"))# espeta o botão aparecer
                    )
                    time.sleep(5)# espera para o usuario ler
                    btnEstoque.click()# clica para fechar o pop up
                    break
                except Exception:
                    print("Produto em estoque!")
                btnSim = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Sim']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnSim.click()# clica nele
                btnImpri = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Imprimir']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnImpri.click()# clica nele
                time.sleep(10)
                janelas = self.nav.window_handles# pega todas as janelas abertas
                self.nav.switch_to.window(janelas[1])# muda para a da impressão
                self.nav.close()# fecha a janela
                self.nav.switch_to.window(janelas[0])# volta para a principal
                contador += 1
                frete += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadSaidaDev(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            frete = 1
            while not pararLoop:
                if frete > 6:
                    frete = 1
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    try:
                        btnPular = WebDriverWait(self.nav, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Pular']"))
                        )
                        time.sleep(intervaloTecla)
                        btnPular.click()
                    except Exception:
                        print("tutorial não exibido")
                    btnNovo = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla+1)
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                try:
                    btnNao = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[text()='Não']"))# espera o botão de não salva aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNao.click()#Clica no botão
                except Exception:
                    print("Nenhum itém sem salvar!")    
                btnOpe = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_OPERACAO")) # espera o botão de mostrar o list aparecer
                        )
                btnOpe.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da operação']").send_keys(Keys.ENTER)# limpa a input
                time.sleep(intervaloTecla+1)
                # btnCli = WebDriverWait(self.nav, 10).until(
                #             EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_EMITENTE")) # espera o botão aparecer
                #         )
                # btnCli.click()# clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um cliente']").clear()# limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um cliente']").send_keys("Consumidor final")# digita o cliente
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//div[@data-value='2141aabd-176e-11ef-8438-5254004a856f']").click()# Clica na opção
                # time.sleep(intervaloTecla+1)
                # btnVen = WebDriverWait(self.nav, 10).until(
                #             EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_VENDEDOR")) # espera o botão aparecer
                #         )
                # btnVen.click()# clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do vendedor']").clear()# limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do vendedor']").send_keys("padrao")# digita o vendedor
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//div[@data-value='21415c7a-176e-11ef-8438-5254004a856f']").click()# clica na opção
                # time.sleep(intervaloTecla+1)
                self.nav.find_element(By.XPATH, '//button[text()="Itens"]').click()# muda para a aba itens
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//button[text()='inserir novo item']").click()# inseri um novo item
                btnProd = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "ITENS.0.ID_PRODUTO")) # espera o botão aparecer
                        )
                btnProd.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do produto']").send_keys(Keys.ENTER)# seleciona o ultimo produto cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").click()# clica na input de quantidade 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").send_keys(str(contador))# digita a quantidade do item
                time.sleep(intervaloTecla)
                if contador % 2 == 0:#teste para alternar entre desconto e acrescimo
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").send_keys(str(contador))# Digita o desconto
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").click()# o mesmo que o desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").send_keys(str(contador))
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Observações"]').click()# muda para a aba observações
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe alguma observação sobre a movimentação']").send_keys("teste" + str(contador))# digita a observação
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Transportadora"]').click()# muda para a aba transportadora
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-select-TRANSPORTADOR.MODFRETE").click()# Clica no list de mod. frete contratado
                time.sleep(intervaloTecla)
                match frete:# teste para alternas no frete contratado
                    case 1:
                        pyautogui.press("enter")# seleciona a primeira opção
                        self.nav.find_element(By.ID, "form-auto-complete-TRANSPORTADOR.ID_TRANSPORTADOR").click()# # clica no list de tranportadoras
                        time.sleep(intervaloTecla+1)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma transportadora']").send_keys(Keys.ENTER)# escolhe a ultima transportadora cadastrada
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.PLACA_VEICULO").send_keys("teste" + str(contador))# digita a placa do veiculo
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.RNTC").send_keys("teste" + str(contador))# digita o RNTC
                    case 2:
                        pyautogui.press("1")# muda para a proxima opção
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")# e seleciona ela
                    case 3:
                        pyautogui.press("2")# assim por diante
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 4:
                        pyautogui.press("3")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 5:
                        pyautogui.press("4")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 6:
                        pyautogui.press("9")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Volumes"]').click()# muda para a aba volumes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.QVOL").send_keys(str(contador))# digita a quantidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.ESP").send_keys("teste" + str(contador))# digita a especie
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.MARCA").send_keys("teste" + str(contador))# digita a marca
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.NVOL").send_keys("teste" + str(contador))# digita o numero
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").click()# clica na input de peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").send_keys(str(contador))# digita o peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").click()# clica na input de peso bruto
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").send_keys(str(contador))# digita o peso bruto
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre desconto e acrescimo no totais de pedidos
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(str(contador))# digita o valor
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(Keys.ENTER)# seleciona o valor
                    try:
                        btnRatear = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Ratear']")) # espera o botão aparecer
                        )
                        time.sleep(intervaloTecla)
                        btnRatear.click()# clica nele
                    except Exception:
                        print("Botão ratear não apareceu!")
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").click()# o memo que o desconto para acrescimo
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(str(contador))
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(Keys.ENTER)
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre salvar e aprovar
                    self.nav.find_element(By.ID, "movimentacao-button-salvar").click()#clica no botão salvar
                    time.sleep(intervaloTecla)
                else:
                    self.nav.find_element(By.ID, "movimentacao-button-aprovar").click()# clica no botão aprovar
                    time.sleep(intervaloTecla)
                    btnAprovarPop = WebDriverWait(self.nav, 3).until(
                        EC.presence_of_element_located((By.XPATH,"//button[text()='Aprovar']"))# espera o botão aparecer
                    )
                    btnAprovarPop.click()# clica no botão
                    btnPag = WebDriverWait(self.nav, 10).until(
                        EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_PLANO_PAGAMENTO"))# espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnPag.click()# clica para aparecer o list
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona o plano de pagamento
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-ID_FORMA_PAGAMENTO").click()# abre o list de forma de pag
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona a forma de pag
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Adicionar pagamento']").click()# adiciona o pag
                    btnAprovar = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Aprovar"]'))# espera o botão de aprovar aparecer
                    )
                    actions = ActionChains(self.nav)
                    actions.move_to_element(btnAprovar).perform()# scrola até o botão
                    time.sleep(intervaloTecla)
                    btnAprovar.click()# clica no botão
                try:
                    btnEstoque = WebDriverWait(self.nav, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[text()='OK']"))# espeta o botão aparecer
                    )
                    time.sleep(5)# espera para o usuario ler
                    btnEstoque.click()# clica para fechar o pop up
                    break
                except Exception:
                    print("Produto em estoque!")
                btnSim = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Sim']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnSim.click()# clica nele
                btnImpri = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Imprimir']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnImpri.click()# clica nele
                time.sleep(10)
                janelas = self.nav.window_handles# pega todas as janelas abertas
                self.nav.switch_to.window(janelas[1])# muda para a da impressão
                self.nav.close()# fecha a janela
                self.nav.switch_to.window(janelas[0])# volta para a principal
                contador += 1
                frete += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadEntradaDev(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            frete = 1
            while not pararLoop:
                if frete > 6:
                    frete = 1
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    try:
                        btnPular = WebDriverWait(self.nav, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Pular']"))
                        )
                        time.sleep(intervaloTecla)
                        btnPular.click()
                    except Exception:
                        print("tutorial não exibido")
                    btnNovo = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla+1)
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                try:
                    btnNao = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[text()='Não']"))# espera o botão de não salva aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNao.click()#Clica no botão
                except Exception:
                    print("Nenhum itém sem salvar!")    
                btnOpe = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_OPERACAO")) # espera o botão de mostrar o list aparecer
                        )
                btnOpe.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da operação']").send_keys(Keys.ENTER)# limpa a input
                time.sleep(intervaloTecla+1)
                self.nav.find_element(By.XPATH, '//button[text()="Itens"]').click()# muda para a aba itens
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//button[text()='inserir novo item']").click()# inseri um novo item
                btnProd = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "ITENS.0.ID_PRODUTO")) # espera o botão aparecer
                        )
                btnProd.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do produto']").send_keys(Keys.ENTER)# seleciona o ultimo produto cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").click()# clica na input de quantidade 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").send_keys(str(contador))# digita a quantidade do item
                time.sleep(intervaloTecla)
                if contador % 2 == 0:#teste para alternar entre desconto e acrescimo
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").send_keys(str(contador))# Digita o desconto
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").click()# o mesmo que o desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").send_keys(str(contador))
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Observações"]').click()# muda para a aba observações
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe alguma observação sobre a movimentação']").send_keys("teste" + str(contador))# digita a observação
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Transportadora"]').click()# muda para a aba transportadora
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-select-TRANSPORTADOR.MODFRETE").click()# Clica no list de mod. frete contratado
                time.sleep(intervaloTecla)
                match frete:# teste para alternas no frete contratado
                    case 1:
                        pyautogui.press("enter")# seleciona a primeira opção
                        self.nav.find_element(By.ID, "form-auto-complete-TRANSPORTADOR.ID_TRANSPORTADOR").click()# # clica no list de tranportadoras
                        time.sleep(intervaloTecla+1)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma transportadora']").send_keys(Keys.ENTER)# escolhe a ultima transportadora cadastrada
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.PLACA_VEICULO").send_keys("teste" + str(contador))# digita a placa do veiculo
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.RNTC").send_keys("teste" + str(contador))# digita o RNTC
                    case 2:
                        pyautogui.press("1")# muda para a proxima opção
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")# e seleciona ela
                    case 3:
                        pyautogui.press("2")# assim por diante
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 4:
                        pyautogui.press("3")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 5:
                        pyautogui.press("4")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 6:
                        pyautogui.press("9")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Volumes"]').click()# muda para a aba volumes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.QVOL").send_keys(str(contador))# digita a quantidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.ESP").send_keys("teste" + str(contador))# digita a especie
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.MARCA").send_keys("teste" + str(contador))# digita a marca
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.NVOL").send_keys("teste" + str(contador))# digita o numero
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").click()# clica na input de peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").send_keys(str(contador))# digita o peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").click()# clica na input de peso bruto
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").send_keys(str(contador))# digita o peso bruto
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre desconto e acrescimo no totais de pedidos
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(str(contador))# digita o valor
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(Keys.ENTER)# seleciona o valor
                    try:
                        btnRatear = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Ratear']")) # espera o botão aparecer
                        )
                        time.sleep(intervaloTecla)
                        btnRatear.click()# clica nele
                    except Exception:
                        print("Botão ratear não apareceu!")
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").click()# o memo que o desconto para acrescimo
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(str(contador))
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(Keys.ENTER)
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre salvar e aprovar
                    self.nav.find_element(By.ID, "movimentacao-button-salvar").click()#clica no botão salvar
                    time.sleep(intervaloTecla)
                else:
                    self.nav.find_element(By.ID, "movimentacao-button-aprovar").click()# clica no botão aprovar
                    time.sleep(intervaloTecla)
                    btnAprovarPop = WebDriverWait(self.nav, 3).until(
                        EC.presence_of_element_located((By.XPATH,"//button[text()='Aprovar']"))# espera o botão aparecer
                    )
                    btnAprovarPop.click()# clica no botão
                    btnPag = WebDriverWait(self.nav, 10).until(
                        EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_PLANO_PAGAMENTO"))# espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnPag.click()# clica para aparecer o list
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona o plano de pagamento
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-ID_FORMA_PAGAMENTO").click()# abre o list de forma de pag
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona a forma de pag
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Adicionar pagamento']").click()# adiciona o pag
                    btnAprovar = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Aprovar"]'))# espera o botão de aprovar aparecer
                    )
                    actions = ActionChains(self.nav)
                    actions.move_to_element(btnAprovar).perform()# scrola até o botão
                    time.sleep(intervaloTecla)
                    btnAprovar.click()# clica no botão
                try:
                    btnEstoque = WebDriverWait(self.nav, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[text()='OK']"))# espeta o botão aparecer
                    )
                    time.sleep(5)# espera para o usuario ler
                    btnEstoque.click()# clica para fechar o pop up
                    break
                except Exception:
                    print("Produto em estoque!")
                btnSim = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Sim']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnSim.click()# clica nele
                btnImpri = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Imprimir']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnImpri.click()# clica nele
                time.sleep(10)
                janelas = self.nav.window_handles# pega todas as janelas abertas
                self.nav.switch_to.window(janelas[1])# muda para a da impressão
                self.nav.close()# fecha a janela
                self.nav.switch_to.window(janelas[0])# volta para a principal
                contador += 1
                frete += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadOutrasOpe(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            frete = 1
            while not pararLoop:
                if frete > 6:
                    frete = 1
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    try:
                        btnPular = WebDriverWait(self.nav, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Pular']"))
                        )
                        time.sleep(intervaloTecla)
                        btnPular.click()
                    except Exception:
                        print("tutorial não exibido")
                    btnNovo = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.ID, "listagens-button-novo")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla+1)
                    btnNovo.click()# clica no botão
                else:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                try:
                    btnNao = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[text()='Não']"))# espera o botão de não salva aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNao.click()#Clica no botão
                except Exception:
                    print("Nenhum itém sem salvar!")    
                btnOpe = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_OPERACAO")) # espera o botão de mostrar o list aparecer
                        )
                btnOpe.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da operação']").send_keys(Keys.ENTER)# limpa a input
                time.sleep(intervaloTecla+1)
                # btnCli = WebDriverWait(self.nav, 10).until(
                #             EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_EMITENTE")) # espera o botão aparecer
                #         )
                # btnCli.click()# clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um cliente']").clear()# limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um cliente']").send_keys("Consumidor final")# digita o cliente
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//div[@data-value='2141aabd-176e-11ef-8438-5254004a856f']").click()# Clica na opção
                # time.sleep(intervaloTecla+1)
                # btnVen = WebDriverWait(self.nav, 10).until(
                #             EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_VENDEDOR")) # espera o botão aparecer
                #         )
                # btnVen.click()# clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do vendedor']").clear()# limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do vendedor']").send_keys("padrao")# digita o vendedor
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//div[@data-value='21415c7a-176e-11ef-8438-5254004a856f']").click()# clica na opção
                # time.sleep(intervaloTecla+1)
                self.nav.find_element(By.XPATH, '//button[text()="Itens"]').click()# muda para a aba itens
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//button[text()='inserir novo item']").click()# inseri um novo item
                btnProd = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "ITENS.0.ID_PRODUTO")) # espera o botão aparecer
                        )
                btnProd.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do produto']").send_keys(Keys.ENTER)# seleciona o ultimo produto cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").click()# clica na input de quantidade 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").send_keys(str(contador))# digita a quantidade do item
                time.sleep(intervaloTecla)
                if contador % 2 == 0:#teste para alternar entre desconto e acrescimo
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.DESCONTO").send_keys(str(contador))# Digita o desconto
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").click()# o mesmo que o desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.ACRESCIMO").send_keys(str(contador))
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Observações"]').click()# muda para a aba observações
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe alguma observação sobre a movimentação']").send_keys("teste" + str(contador))# digita a observação
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Transportadora"]').click()# muda para a aba transportadora
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-select-TRANSPORTADOR.MODFRETE").click()# Clica no list de mod. frete contratado
                time.sleep(intervaloTecla)
                match frete:# teste para alternas no frete contratado
                    case 1:
                        pyautogui.press("enter")# seleciona a primeira opção
                        self.nav.find_element(By.ID, "form-auto-complete-TRANSPORTADOR.ID_TRANSPORTADOR").click()# # clica no list de tranportadoras
                        time.sleep(intervaloTecla+1)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma transportadora']").send_keys(Keys.ENTER)# escolhe a ultima transportadora cadastrada
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.PLACA_VEICULO").send_keys("teste" + str(contador))# digita a placa do veiculo
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSPORTADOR.RNTC").send_keys("teste" + str(contador))# digita o RNTC
                    case 2:
                        pyautogui.press("1")# muda para a proxima opção
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")# e seleciona ela
                    case 3:
                        pyautogui.press("2")# assim por diante
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 4:
                        pyautogui.press("3")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 5:
                        pyautogui.press("4")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                    case 6:
                        pyautogui.press("9")
                        time.sleep(intervaloTecla)
                        pyautogui.press("enter")
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Volumes"]').click()# muda para a aba volumes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.QVOL").send_keys(str(contador))# digita a quantidade
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.ESP").send_keys("teste" + str(contador))# digita a especie
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-VOLUMES.MARCA").send_keys("teste" + str(contador))# digita a marca
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.NVOL").send_keys("teste" + str(contador))# digita o numero
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").click()# clica na input de peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_LIQUIDO").send_keys(str(contador))# digita o peso liquido
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").click()# clica na input de peso bruto
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VOLUMES.PESO_BRUTO").send_keys(str(contador))# digita o peso bruto
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre desconto e acrescimo no totais de pedidos
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").click()# clica na input de desconto
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(str(contador))# digita o valor
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VDESC").send_keys(Keys.ENTER)# seleciona o valor
                    try:
                        btnRatear = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Ratear']")) # espera o botão aparecer
                        )
                        time.sleep(intervaloTecla)
                        btnRatear.click()# clica nele
                    except Exception:
                        print("Botão ratear não apareceu!")
                else:
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").click()# o memo que o desconto para acrescimo
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(str(contador))
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID,"form-numeric-format-TRIBUTOS_TOTAIS.NF.VOUTRO").send_keys(Keys.ENTER)
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre salvar e aprovar
                    self.nav.find_element(By.ID, "movimentacao-button-salvar").click()#clica no botão salvar
                    time.sleep(intervaloTecla)
                else:
                    self.nav.find_element(By.ID, "movimentacao-button-aprovar").click()# clica no botão aprovar
                    time.sleep(intervaloTecla)
                    btnAprovarPop = WebDriverWait(self.nav, 3).until(
                        EC.presence_of_element_located((By.XPATH,"//button[text()='Aprovar']"))# espera o botão aparecer
                    )
                    btnAprovarPop.click()# clica no botão
                    btnPag = WebDriverWait(self.nav, 10).until(
                        EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_PLANO_PAGAMENTO"))# espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnPag.click()# clica para aparecer o list
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona o plano de pagamento
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-ID_FORMA_PAGAMENTO").click()# abre o list de forma de pag
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona a forma de pag
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Adicionar pagamento']").click()# adiciona o pag
                    btnAprovar = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Aprovar"]'))# espera o botão de aprovar aparecer
                    )
                    actions = ActionChains(self.nav)
                    actions.move_to_element(btnAprovar).perform()# scrola até o botão
                    time.sleep(intervaloTecla)
                    btnAprovar.click()# clica no botão
                try:
                    btnEstoque = WebDriverWait(self.nav, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[text()='OK']"))# espeta o botão aparecer
                    )
                    time.sleep(5)# espera para o usuario ler
                    btnEstoque.click()# clica para fechar o pop up
                    break
                except Exception:
                    print("Produto em estoque!")
                btnSim = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Sim']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnSim.click()# clica nele
                btnImpri = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Imprimir']")) # espera o botão de erro aparecer
                        )
                time.sleep(intervaloTecla)
                btnImpri.click()# clica nele
                time.sleep(10)
                janelas = self.nav.window_handles# pega todas as janelas abertas
                self.nav.switch_to.window(janelas[1])# muda para a da impressão
                self.nav.close()# fecha a janela
                self.nav.switch_to.window(janelas[0])# volta para a principal
                contador += 1
                frete += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadCompras(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                if contador == 1:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                    try:
                        btnPular = WebDriverWait(self.nav, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//button[text()='Pular']"))
                        )
                        time.sleep(intervaloTecla)
                        btnPular.click()
                    except Exception:
                        print("tutorial não exibido")
                    btnNovo = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[text()='Nova compra']")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla+1)
                    btnNovo.click()# clica no botão
                else:
                   self.nav.get("")#url removido por questões de proteção da LGPD 
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                try:
                    btnNao = WebDriverWait(self.nav, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[text()='Não']"))# espera o botão de não salva aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNao.click()#Clica no botão
                except Exception:
                    print("Nenhum itém sem salvar!")
                btnOpe = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_EMITENTE")) # espera o botão de mostrar o list aparecer
                        )
                btnOpe.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um fornecedor']").send_keys(Keys.ENTER)
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-NUMERO_NOTA").send_keys(str(contador)*6)
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-SERIE").send_keys(str(contador))
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Itens"]').click()# muda para a aba itens
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//button[text()='inserir novo item']").click()# inseri um novo item
                btnProd = WebDriverWait(self.nav, 10).until(
                            EC.element_to_be_clickable((By.ID, "ITENS.0.ID_PRODUTO")) # espera o botão aparecer
                        )
                btnProd.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do produto']").send_keys(Keys.ENTER)# seleciona o ultimo produto cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").click()# clica na input de quantidade 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID,"form-numeric-format-ITENS.0.QTD").send_keys(str(contador))# digita a quantidade do item
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, '//button[text()="Observações"]').click()# muda para a aba observações
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe uma observação para a compra']").send_keys("teste" + str(contador))# digita a observação
                time.sleep(intervaloTecla)
                if contador % 2 == 0:# teste para alternar entre salvar e aprovar
                    self.nav.find_element(By.ID, "compra-button-salvar").click()#clica no botão salvar
                    time.sleep(intervaloTecla)
                else:
                    btnApro = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.ID, "compra-button-aprovar"))
                    )
                    btnApro.click()
                    time.sleep(intervaloTecla)
                    try:
                        btnAprovarPop = WebDriverWait(self.nav, 3).until(
                            EC.presence_of_element_located((By.XPATH,"//button[text()='Sim']"))# espera o botão aparecer
                        )
                        btnAprovarPop.click()# clica no botão
                    except Exception:
                        print("Não apareceu o pop up")
                    btnPag = WebDriverWait(self.nav, 10).until(
                        EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_PLANO_PAGAMENTO"))# espera o botão aparecer
                    )
                    btnPag.click()# clica para aparecer o list
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona o plano de pagamento
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.ID, "form-auto-complete-ID_FORMA_PAGAMENTO").click()# abre o list de forma de pag
                    time.sleep(intervaloTecla+1)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").clear()# limpa a input
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da forma de pagamento']").send_keys(Keys.ENTER)# seleciona a forma de pag
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//button[text()='Adicionar pagamento']").click()# adiciona o pag
                    btnAprovar = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Aprovar Compra"]'))# espera o botão de aprovar aparecer
                    )
                    actions = ActionChains(self.nav)
                    actions.move_to_element(btnAprovar).perform()# scrola até o botão
                    time.sleep(intervaloTecla)
                    btnAprovar.click()# clica no botão
                try:
                    btnEstoque = WebDriverWait(self.nav, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[text()='OK']"))# espeta o botão aparecer
                    )
                    time.sleep(5)# espera para o usuario ler
                    btnEstoque.click()# clica para fechar o pop up
                    break
                except Exception:
                    print("Produto em estoque!")
                contador += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadEstoque(self,intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                if contador == 1:
                    self.nav.get("") # avbrindo a pagina de estoque #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 3).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[text()='Nova movimentação']"))# espeta o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNovo.click()# clica na botão
                else:
                    self.nav.get("")#url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                btnList = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_PRODUTO")) # espera o botão de abrir o list aparecer
                )
                time.sleep(intervaloTecla)
                btnList.click()# clica no botão
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um produto']").send_keys(Keys.ENTER)# seleciona o ultimo produto cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-QTD").click()# clica na input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-QTD").send_keys(str(contador))# digita a quantidade de produtos
                time.sleep(intervaloTecla)
                if contador % 2 == 0: # teste para alternar entre saida e entrada
                    self.nav.find_element(By.XPATH, "//input[@value='0']").click() # clica no radio button
                else:
                    self.nav.find_element(By.XPATH, "//input[@value='1']").click() # clica no radio button
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe uma observação']").send_keys(f"teste{contador}") # digita a observação
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//button[text()='Salvar e Inserir']").click()# clica no botão de inserir
                contador += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadFluxoCaixa(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            conta = 1
            lancamento = 1
            while not pararLoop:
                if conta > 4:
                    conta = 1
                if lancamento > 3 :
                    lancamento = 1
                if contador == 1:
                    self.nav.get("") # abre a pagina de caixa #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Novo registro']")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNovo.click()# clica no botão
                else:
                   self.nav.get("") #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                btnList = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_CONTA")) # espera o botão aparecer
                )
                time.sleep(intervaloTecla)
                btnList.click()# clica no botão
                time.sleep(intervaloTecla)
                # match conta:# teste para alternar entre os tipos de conta
                #     case 1:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear() # limpa a input
                #         time.sleep(intervaloTecla)    
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Despesa") # digita o tipo de conta
                #     case 2:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear() # e assim por diante
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Compra")
                #     case 3:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Receita")
                #     case 4:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Taxa")
                # time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da conta']").send_keys(Keys.ENTER) # seleciona a conta
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VALOR").click() # clica na input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VALOR").send_keys(str(contador)) # digita o valor
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_BANCO").click() # clica no botão de abri o list
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").clear() # limpa a input
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome do banco']").send_keys(Keys.ENTER)# Seleciona o banco
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Informe o histórico do lançamento']").send_keys(f"teste{contador}") # digita o historico
                time.sleep(intervaloTecla)
                match lancamento:# teste para alternar entre o tipo de lançamento
                    case 1:
                        self.nav.find_element(By.XPATH, "//input[@value='0']").click()# clica no radio button
                    case 2:
                        self.nav.find_element(By.XPATH, "//input[@value='1']").click()# clica no radio button
                    case 3:
                        self.nav.find_element(By.XPATH, "//input[@value='2']").click()# clica no radio button
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-auto-complete-TRANSACAO_CARTAO.ID_ADMINISTRADORA").click()# clica no botão de list
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou o nome da administradora']").send_keys(Keys.ENTER) # seleciona a ultima administradora cadastrada
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSACAO_CARTAO.NSU").send_keys(str(contador)) # digita o NSU
                        time.sleep(intervaloTecla)
                        self.nav.find_element(By.ID, "form-input-TRANSACAO_CARTAO.CODIGOAUTORIZACAO").send_keys(str(contador)) # digita o cod de autorização
                btnInseri = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de aprovar aparecer
                    )
                actions = ActionChains(self.nav)
                actions.move_to_element(btnInseri).perform()# scrola até o botão
                time.sleep(intervaloTecla)
                btnInseri.click()# clica no botão
                contador += 1
                conta += 1
                lancamento += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))  # Tipo da exceção
            print(e)  # Mensagem de erro
            yield "err",type(e), e

    def cadContasPagar(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            conta = 1
            while not pararLoop:
                if conta > 4:
                    conta = 1
                if contador == 1:
                    self.nav.get("") # abre a pagina de contas a pagar #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Nova conta']")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNovo.click() # clica no botão
                else:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                btnList = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_EMITENTE")) # espera o botão aparecer
                )
                time.sleep(intervaloTecla)
                btnList.click()# clica no botão 
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um emitente']").send_keys(Keys.ENTER) # seleciona o ultima emitente cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VALOR").click() # clica na input de valor a pagar
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VALOR").send_keys(str(contador)) # digita o valor
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-input-DOCUMENTO").send_keys(f"teste{contador}")# digita o documento
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_CONTA").click() # aperta no botão de list
                time.sleep(intervaloTecla)
                # match conta: # teste para alternar entre contas
                #     case 1:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear() # limpa a input
                #         time.sleep(intervaloTecla)    
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Despesa") # digita a conta
                #     case 2:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()# e assim por diante
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Compra")
                #     case 3:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Receita")
                #     case 4:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Taxa")
                # time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys(Keys.ENTER) # seleciona a conta
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Digite uma observação para essa conta']").send_keys(f"teste{contador}") # Digita a observação
                time.sleep(intervaloTecla)
                btnInseri = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de aprovar aparecer
                    )
                time.sleep(intervaloTecla)
                btnInseri.click()# clica no botão
                contador += 1
                conta += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def cadContasReceber(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            conta = 1
            while not pararLoop:
                if conta > 4:
                    conta = 1
                if contador == 1:
                    self.nav.get("") # abre a pagina de contas a receber #url removido por questões de proteção da LGPD
                    btnNovo = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Nova conta']")) # espera o botão aparecer
                    )
                    time.sleep(intervaloTecla)
                    btnNovo.click() # clica no botão
                else:
                    self.nav.get("") #url removido por questões de proteção da LGPD
                try:
                    WebDriverWait(self.nav, 3).until(EC.alert_is_present())
                    alert = self.nav.switch_to.alert
                    alert.accept()
                except Exception as e:
                    print("Alerta não existente")
                btnList = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.ID, "form-auto-complete-ID_EMITENTE")) # espera o botão aparecer
                )
                time.sleep(intervaloTecla)
                btnList.click() # clica no botão de list de emitentes
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um emitente']").send_keys(Keys.ENTER) # seleciona o ultimo emitente cadastrado
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VALOR").click()# clica na input de valor
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-numeric-format-VALOR").send_keys(str(contador)) # digita o valor
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Informe o documento']").send_keys(f"teste{contador}") # digita o documento
                time.sleep(intervaloTecla)
                self.nav.find_element(By.ID, "form-auto-complete-ID_CONTA").click()# clica no botão de list de conta
                time.sleep(intervaloTecla)
                # match conta: # teste para alternar entre contas
                #     case 1:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear() # deleta a input
                #         time.sleep(intervaloTecla)    
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Despesa") # digita a conta
                #     case 2:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()# e assim por diante
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Compra")
                #     case 3:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Receita")
                #     case 4:
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").clear()
                #         time.sleep(intervaloTecla)
                #         self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys("Taxa")
                # time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR,"input[placeholder='Digite o código ou a descrição da conta']").send_keys(Keys.ENTER) # seleciona a conta
                time.sleep(intervaloTecla)
                self.nav.find_element(By.CSS_SELECTOR, "textarea[placeholder='Digite uma observação para essa conta']").send_keys(f"teste{contador}") # digita a observaçãp
                time.sleep(intervaloTecla)
                btnInseri = WebDriverWait(self.nav, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar e Inserir"]'))# espera o botão de aprovar aparecer
                    )
                time.sleep(intervaloTecla)
                btnInseri.click()# clica no botão
                contador += 1
                conta += 1
                yield "contador", contador# manda o contador para a tela
                time.sleep(intervaloExec)
                if pararLoop:# teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relProdutos(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Produtos']").click()
                # inpEAN = WebDriverWait(self.nav, 5).until(
                #     EC.presence_of_element_located((By.ID, "form-input-ean"))
                # )
                # inpEAN.send_Keys(str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-numeric-format-codigo").send_keys(str(contador)) # digita o codigo do produto
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-auto-complete-grupo").click() # aperta o botão do list de grupo
                # time.sleep(intervaloTecla + 1)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do grupo']").clear() # limpra a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do grupo']").send_keys("Geral") # digita o grupo
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição do grupo']").send_keys(Keys.ENTER) # seleciona o grupo
                # btnCategoria = WebDriverWait(self.nav, 3).until(
                #     EC.element_to_be_clickable((By.ID, "form-auto-complete-categoria")) # espera o botão aparecer
                # )
                # btnCategoria.click() # clica no botão de list de categoria
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma categoria']").clear() # limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma categoria']").send_keys("Geral") # digita a categoria
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma categoria']").send_keys(Keys.ENTER) # seleciona a categoria
                # btnFamilia = WebDriverWait(self.nav, 3).until(
                #     EC.element_to_be_clickable((By.ID, "form-auto-complete-familia")) # espera o botão aparecer
                # )
                # btnFamilia.click() # clica no botão list de familia
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da família']").clean() # limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da família']").send_keys("Geral") # digita a familia
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite o código ou a descrição da família']").send_keys(Keys.ENTER) # seleciona a familia
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//button[text()='Gerar relatório']").click() # apertar no botão de gerar relatorio
                contador += 1
                yield "contador", contador # mostra o contador na tela
                time.sleep(intervaloExec)
                if pararLoop: # teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relEmitentes(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            tipoPessoa = 1
            while not pararLoop:
                # if tipoPessoa > 3:
                #     tipoPessoa = 1
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Emitentes']").click()
                # inpCodigo = WebDriverWait(self.nav, 3).until(
                #     EC.element_to_be_clickable((By.ID, "form-numeric-format-codigo")) # espera a input aporecer
                # )
                # inpCodigo.send_keys(str(contador)) # digita o codigo do emitente
                # time.sleep(intervaloTecla)
                # if contador % 2 == 0:
                #     self.nav.find_element(By.ID, "form-masked-field-cpf_cnpj").send_keys("CPF") # digita o cpf
                # else:
                #     self.nav.find_element(By.ID, "form-masked-field-cpf_cnpj").send_keys("CNPJ") # digita o cnpj
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-input-nome_rs").send_keys(f"teste{contador}") # Digita o nome e a razão social
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-select-pessoa").click() # abre o select de tipo de pessoa
                # time.sleep(intervaloTecla)
                # if contador % 2 == 0: # teste para alternar entre pessoa fisica e juridica
                #     pyautogui.press("enter") # seleciona a opção fisica
                # else:
                #     pyautogui.press("down") # seleciona a opção juridica
                #     time.sleep(intervaloTecla)
                #     pyautogui.press("enter")
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-masked-field-cep").send_keys("CEP") # digita o cep
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-auto-complete-uf").click() # abre o list de UF
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").clear() # limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").send_keys("MG") # digita a uf 
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").send_keys(Keys.ENTER) # seleciona a uf
                # btnCidade = WebDriverWait(self.nav, 3).until(
                #     EC.element_to_be_clickable((By.ID, "form-auto-complete-cidade"))# espera o botão ser clicavel
                # )
                # btnCidade.click() # clica no botão
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade']").clear() # limpa a input
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade']").send_keys("lavras") # digita a cidade
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade']").send_keys(Keys.ENTER) # seleciona a cidade
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-select-tipo").click()# clique no tipo pessoa
                # if tipoPessoa == 1:
                #     pyautogui.press("enter")# seleciona a opção cliente
                # elif tipoPessoa == 2:
                #     time.sleep(intervaloTecla)
                #     pyautogui.press("down")#Selciona a opção fornecedor
                #     time.sleep(intervaloTecla)
                #     pyautogui.press("enter")#aperta enter na opção
                # elif tipoPessoa == 3:
                #     time.sleep(intervaloTecla)
                #     pyautogui.press("down",presses=10)#Seleciona a opção ambos
                #     time.sleep(intervaloTecla)
                #     pyautogui.press("enter")#aperta enter na opção
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//button[text()='Gerar relatório']").click() # apertar no botão de gerar relatorio
                contador += 1
                # tipoPessoa += 1
                yield "contador", contador # mostra o contador na tela
                time.sleep(intervaloExec)
                if pararLoop: # teste para parar o loop
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relVendedores(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Vendedores']").click()
                # inpCod = WebDriverWait(self.nav, 5).until(
                #     EC.presence_of_element_located((By.ID,"form-numeric-format-codigo"))
                # )
                # inpCod.send_keys(str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID,"form-masked-field-cep").send_keys(str(contador) * 8)
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID,"form-auto-complete-uf").click()
                # time.sleep(intervaloTecla + 1)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").clear()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").send_keys("MG")
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Digite a sigla ou o nome do estado']").send_keys(Keys.ENTER)
                # btnCidade = WebDriverWait(self.nav, 5).until(
                #     EC.element_to_be_clickable((By.ID,"form-auto-complete-cidade"))
                # )
                # btnCidade.click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade de MG']").clear()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade de MG']").send_keys("Lavras")
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione uma cidade de MG']").send_keys(Keys.ENTER)
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//button[text()='Gerar relatório']").click() # apertar no botão de gerar relatorio
                contador =+ 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relTransportadoras(self, intervaloTecla, intervaloExec, pararLoop,contador):
        try:
            cnpj = SiaWebClass.geraCnpj()
            while not pararLoop:
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Transportadoras']").click()
                # inpRazao = WebDriverWait(self.nav, 5).until(
                #     EC.presence_of_element_located(By.ID, "form-input-razao")
                # )
                # inpRazao.send_keys(f"teste{contador}")
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-masked-field-cnpj").send_keys(cnpj)
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//button[text()='Gerar relatório']").click() # apertar no botão de gerar relatorio
                contador += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e
        
    def relIntermediadores(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            cnpj = SiaWebClass.geraCnpj()
            while not pararLoop:
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Intermediadores']").click()
                # inpCod = WebDriverWait(self.nav, 5).until(
                #     EC.presence_of_element_located(By.ID, "form-numeric-format-codigo")
                # )
                # inpCod.send_keys(str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-input-nome").send_keys(f"teste{contador}")
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-masked-field-cnpj").send_keys(cnpj)
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID, "form-auto-complete-idemitente").click()
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.CSS_SELECTOR, "input[placeholder='Selecione um emitente']").send_keys(Keys.ENTER)
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.XPATH, "//button[text()='Gerar relatório']").click() # apertar no botão de gerar relatorio
                contador += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relMovimentacoes(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Movimentações']").click()
                # time.sleep(intervaloTecla)
                # inpCod = WebDriverWait(self.nav, 5).until(
                #     EC.presence_of_element_located((By.ID, "form-numeric-format-codigo"))
                # )
                # inpCod.send_keys(str(contador))
                # time.sleep(intervaloTecla)
                # self.nav.find_element(By.ID,)
                contador += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relContasReceber(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop: 
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Contas a receber']").click()
                contador += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relContasPagar(self, intervaloTecla, intervaloExec, pararLoop, contador):
        try:
            while not pararLoop:
                self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                self.nav.switch_to.default_content()
                ul = WebDriverWait(self.nav, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul"))
                )
                time.sleep(intervaloTecla + 1)
                li = ul.find_elements(By.XPATH, "./li")
                li[7].click()
                time.sleep(intervaloTecla)
                self.nav.find_element(By.XPATH, "//a[text()='Contas a pagar']").click()
                contador += 1
                yield "contador", contador
                time.sleep(intervaloExec)
                if pararLoop:
                    break
        except Exception as e:
            print("Ocorreu um erro:")
            print(type(e))
            print(e)
            yield "err",type(e), e

    def relCaixa(self, intervaloTecla, intervaloExec, pararLoop, contador):
            try:
                while not pararLoop:
                    self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                    self.nav.switch_to.default_content()
                    ul = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//ul"))
                    )
                    time.sleep(intervaloTecla + 1)
                    li = ul.find_elements(By.XPATH, "./li")
                    li[7].click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//a[text()='Caixa']").click()
                    contador += 1
                    yield "contador", contador
                    time.sleep(intervaloExec)
                    if pararLoop:
                        break
            except Exception as e:
                print("Ocorreu um erro:")
                print(type(e))
                print(e)
                yield "err",type(e), e

    def relEntradaMerc(self, intervaloTecla, intervaloExec, pararLoop, contador):
            try:
                while not pararLoop:
                    self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                    self.nav.switch_to.default_content()
                    ul = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//ul"))
                    )
                    time.sleep(intervaloTecla + 1)
                    li = ul.find_elements(By.XPATH, "./li")
                    li[7].click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//a[text()='Entrada mercadorias']").click()
                    contador += 1
                    yield "contador", contador
                    time.sleep(intervaloExec)
                    if pararLoop:
                        break
            except Exception as e:
                print("Ocorreu um erro:")
                print(type(e))
                print(e)
                yield "err",type(e), e

    def relSaidaMerc(self, intervaloTecla, intervaloExec, pararLoop, contador):
            try:
                while not pararLoop:
                    self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                    self.nav.switch_to.default_content()
                    ul = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//ul"))
                    )
                    time.sleep(intervaloTecla + 1)
                    li = ul.find_elements(By.XPATH, "./li")
                    li[7].click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//a[text()='Saída mercadorias']").click()
                    contador += 1
                    yield "contador", contador
                    time.sleep(intervaloExec)
                    if pararLoop:
                        break
            except Exception as e:
                print("Ocorreu um erro:")
                print(type(e))
                print(e)
                yield "err",type(e), e

    def relPlanoContas(self, intervaloTecla, intervaloExec, pararLoop, contador):
            try:
                while not pararLoop:
                    self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                    self.nav.switch_to.default_content()
                    ul = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//ul"))
                    )
                    time.sleep(intervaloTecla + 1)
                    li = ul.find_elements(By.XPATH, "./li")
                    li[7].click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//a[text()='Plano de contas']").click()
                    contador += 1
                    yield "contador", contador
                    time.sleep(intervaloExec)
                    if pararLoop:
                        break
            except Exception as e:
                print("Ocorreu um erro:")
                print(type(e))
                print(e)
                yield "err",type(e), e

    def relComissao(self, intervaloTecla, intervaloExec, pararLoop, contador):
            try:
                while not pararLoop:
                    self.nav.get("") # abre a pagina de relatorio de produtos #url removido por questões de proteção da LGPD
                    self.nav.switch_to.default_content()
                    ul = WebDriverWait(self.nav, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//ul"))
                    )
                    time.sleep(intervaloTecla + 1)
                    li = ul.find_elements(By.XPATH, "./li")
                    li[7].click()
                    time.sleep(intervaloTecla)
                    self.nav.find_element(By.XPATH, "//a[text()='Comissão por vendedor']").click()
                    contador += 1
                    yield "contador", contador
                    time.sleep(intervaloExec)
                    if pararLoop:
                        break
            except Exception as e:
                print("Ocorreu um erro:")
                print(type(e))
                print(e)
                yield "err",type(e), e

    def geraCpf():
        def calcula_digito(cpf_parcial):
            if len(cpf_parcial) == 9:
                multiplicador = list(range(10, 1, -1))
                soma = sum(int(a)*b for a, b in zip(cpf_parcial, multiplicador))
                resto = 11 - (soma % 11)
                return resto if resto < 10 else 0
            elif len(cpf_parcial) == 10:
                multiplicador = list(range(11, 1, -1))
                soma = sum(int(a)*b for a, b in zip(cpf_parcial, multiplicador))
                resto = 11 - (soma % 11)
                return resto if resto < 10 else 0

        cpf_parcial = [random.randint(0, 9) for _ in range(9)]
        primeiro_digito = calcula_digito(cpf_parcial)
        cpf_com_digito = cpf_parcial + [primeiro_digito]
        segundo_digito = calcula_digito(cpf_com_digito)
        cpf_completo = cpf_com_digito + [segundo_digito]
        return ''.join(map(str, cpf_completo))
    
    def geraCnpj():
        def calcula_digito(cnpj_parcial):
            soma = 0
            if len(cnpj_parcial) == 12:
                pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                soma = sum(int(a) * b for a, b in zip(cnpj_parcial, pesos))
            else:
                pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                soma = sum(int(a) * b for a, b in zip(cnpj_parcial, pesos))
            digito = 11 - soma % 11
            return digito if digito < 10 else 0

        cnpj_parcial = [random.randint(0, 9) for _ in range(12)]
        primeiro_digito = calcula_digito(cnpj_parcial)
        cnpj_com_digito = cnpj_parcial + [primeiro_digito]
        segundo_digito = calcula_digito(cnpj_com_digito)
        cnpj_completo = cnpj_com_digito + [segundo_digito]
        return ''.join(map(str, cnpj_completo))