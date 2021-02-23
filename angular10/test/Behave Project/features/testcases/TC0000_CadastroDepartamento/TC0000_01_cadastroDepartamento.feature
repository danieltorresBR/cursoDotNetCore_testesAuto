#language: pt
@sprintTeste @departamento @all
@TC0000_01

Funcionalidade: Cadastrar um Departamento

#CasodeSucesso
@departamentoSucesso
Esquema do Cenário: Departamento Cadastrado com Sucesso
    Dado que esteja na página inicial do CRUD 
    Quando seleciono a opção Departamento
    E seleciono Adicionar Departamento
    E insiro <nomeDepartamento> no campo Nome do Add Department
    E clico no botão Adicionar
    Então verifico que a mensagem Added Successfully é exibida

    Exemplos:
        | nomeDepartamento |
        | testeAuto |

#CasodeInsucesso
@departamentoInsucesso
Esquema do Cenário: Departamento Cadastrado com Insucesso com nome vazio
    Dado que esteja na página inicial do CRUD 
    Quando seleciono a opção Departamento
    E seleciono Adicionar Departamento
    E insiro <nomeDepartamento> no campo Nome do Add Department
    E clico no botão Adicionar
    Então verifico que a mensagem Erro é exibida

    Exemplos:
        | nomeDepartamento |
        | vazio |

