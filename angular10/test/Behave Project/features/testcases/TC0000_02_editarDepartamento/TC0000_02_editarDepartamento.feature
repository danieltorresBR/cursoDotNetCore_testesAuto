#language: pt
@sprintTeste @departamento @all
@TC0000_02

Funcionalidade: Editar Departamento

#CasodeSucesso
@departamentoEditadoSucesso
Esquema do Cenário: Departamento Editado Sucesso
    Dado que esteja na página inicial
    Quando seleciono Departamento
    E insiro <idDepartamento> no campo Filter ID
    E seleciono no botão Editar
    E insiro <nomeEditado> no campo Nome
    E seleciono no botão Atualizar
    Então a informacao Updated Successfully é exibida

    Exemplos:
        | idDepartamento | nomeEditado        |
        | 11             | EditadoComSelenium |


#CasodeErro
@departamentoEditadoComErro
Esquema do Cenário: Departamento Editado com Erro
    Dado que esteja na página inicial
    Quando seleciono Departamento
    E insiro <idDepartamento> no campo Filter ID
    E seleciono no botão Editar
    E insiro <nomeEditado> no campo Nome
    E seleciono no botão Atualizar
    Então a informacao Updated Successfully é exibida

    Exemplos:
        | idDepartamento | nomeEditado        |
        | 11             | vazio              |
