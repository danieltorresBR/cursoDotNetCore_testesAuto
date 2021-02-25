from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class departamento(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url = self.url + "/department"

    locators = { #mapear todos os elementos da pagina que for usado no teste
        "button_add_departamento" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/button'),
        "preencher_departamento" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/div/div/div/div[2]/app-add-edit-dep/div/div/input'),
        "salvar_departamento" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/div/div/div/div[2]/app-add-edit-dep/button'),
        "inputId" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/table/thead/tr/th[1]/div/input'),
        "button_editar_departamento" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/table/tbody/tr/td[3]/button[1]'),
        "input_edit" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/div/div/div/div[2]/app-add-edit-dep/div/div/input'),
        "button_atualizar_departamento" : (By. XPATH, '/html/body/app-root/div/app-department/app-show-dep/div/div/div/div[2]/app-add-edit-dep/button'),
    }

    def clicar_botao_add_departamento(self):
        self.click("button_add_departamento")

    def input_departamento(self, nome_departamento):
        self.preencher_departamento.send_keys(nome_departamento)

    def clicar_botao_salvar_departamento(self):
        self.click("salvar_departamento")

    def verificar_msg(self, texto):
        wait = WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"])
        # Wait for the alert to be displayed and store it in a variable
        alert = wait.until(expected_conditions.alert_is_present())
        assert(texto in alert.text)
        # Store the alert text in a variable text = alert.text
        alert.accept()

    def input_IdDepartamento(self, idDepartamento):
        self.inputId.send_keys(idDepartamento)

    def clicar_botao_editar_departamento(self):
        self.click("button_editar_departamento")

    def input_nome_editado_Departamento(self, nomeEditado):
        self.input_edit.send_keys(nomeEditado)

    def clicar_botao_atualizar_departamento(self):
        self.click("button_atualizar_departamento")