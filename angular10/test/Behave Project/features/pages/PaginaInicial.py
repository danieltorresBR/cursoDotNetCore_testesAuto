from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


class PaginaInicial(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url = self.url #inserir rotas caso existir

    locators = { #mapear todos os elementos da pagina que for usado no teste
        "button_departamento" : (By. XPATH, '/html/body/app-root/div/nav/ul/li[1]/button'),
        "button_funcionario" : (By. XPATH, '/html/body/app-root/div/nav/ul/li[2]/button'),
    }

    def clicar_botao_departamento(self):
        self.click("button_departamento")

    def clicar_botao_funcionario(self):
        self.click("button_funcionario")


    # def inserir_cpf(self,cpf):
    #     if (cpf != 'vazio'):
    #         self.input_cpf.send_keys(cpf)
    #         print(self.input_cpf.get_attribute('value'))

    # def inserir_senha(self, senha):
    #     if(senha!= 'vazio'):
    #         self.input_senha.send_keys(senha)
    
    # def selecionar_operador(self, operador):
    #     if(operador!= 'vazio'):
    #         self.select("select_tipo_operador" , operador)

    
    # def clicar_botao_login(self):
    #     self.click("button_entrar")
    
    # def checar_msg_erro(self):
    #     assert self.msg_nao_autorizado.text == "NÃO AUTORIZADO"
    
    # def mensagem_dado_invalido(self, mensagem):
    #     assert self.msg_invalido == mensagem