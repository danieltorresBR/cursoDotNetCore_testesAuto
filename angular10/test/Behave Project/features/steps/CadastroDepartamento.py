from behave import *
from features.pages.PaginaInicial import PaginaInicial
from features.pages.departamento import departamento


@step("que esteja na página inicial do CRUD")
def step_impl(context):
    PaginaInicial(context).navigate_to()

@step("seleciono a opção Departamento")
def step_impl(context):
    PaginaInicial(context).clicar_botao_departamento()

@step("seleciono Adicionar Departamento")
def step_impl(context):
    departamento(context).clicar_botao_add_departamento()

@step("insiro {nomeDepartamento} no campo Nome do Add Department")
def step_impl(context, nomeDepartamento):
    departamento(context).input_departamento(nomeDepartamento)

@step("clico no botão Adicionar")
def step_impl(context):
    departamento(context).clicar_botao_salvar_departamento()

@step("verifico que a mensagem {texto} é exibida")
def step_impl(context, texto):
    departamento(context).verificar_msg(texto)
#    departamento(context).clicar_botao_salvar_departamento()

    pass


# @step("que esteja na página de login do SIAI Obras")
# def step_impl(context):
#     Login(context).navigate_to()

# @step("insiro {cpf} no campo usuario do login")
# def step_impl(context, cpf):
#     Login(context).inserir_cpf(cpf)

# @step("insiro {senha} no campo senha do login")
# def step_impl(context, senha):
#     Login(context).inserir_senha(senha)

# @step("insiro {tipoOperador} no campo operador do login")
# def step_impl(context, tipoOperador):
#     Login(context).selecionar_operador(tipoOperador)

# @step("clico no botão entrar do login")    
# def step_impl(context):
#     Login(context).clicar_botao_login()

# @step("verifico que a dashboard foi carregada")
# def step_impl(context):
#     Dashboard(context).pagina_carregada()

# @step("verifico que obtive o resultado {resultadoEsperado}")
# def step_impl(context, resultadoEsperado):
#     if(resultadoEsperado == "NÃO AUTORIZADO"):
#         Login(context).checar_msg_erro()
#     elif(resultadoEsperado == "CPF INVALIDO!"):
#         Login(context).mensagem_dado_invalido()
#     elif(resultadoEsperado == "SENHA INVALIDO!"):
#         Login(context).mensagem_dado_invalido()

