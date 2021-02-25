from behave import *
from features.pages.PaginaInicial import PaginaInicial
from features.pages.departamento import departamento

@step("que esteja na página inicial do CRUD")
def step_impl(context):
    PaginaInicial(context).navigate_to()

@step("seleciono a opção Departamento")
def step_impl(context):
    PaginaInicial(context).clicar_botao_departamento()

@step("insiro {idDepartamento} no campo Filter ID")
def step_impl(context, idDepartamento):
    departamento(context).input_IdDepartamento(idDepartamento)

@step("seleciono no botão Editar")
def step_impl(context):
    departamento(context).clicar_botao_editar_departamento()

@step("insiro {nomeEditado} no campo Nome")
def step_impl(context, nomeEditado):
    departamento(context).input_nome_editado_Departamento(nomeEditado)

@step("seleciono no botão Atualizar")
def step_impl(context):
    departamento(context).clicar_botao_atualizar_departamento()

@step("a informacao {texto} é exibida")
def step_impl(context, texto):
    departamento(context).verificar_msg(texto)
#    departamento(context).clicar_botao_salvar_departamento()
    pass