import pyautogui as py
import time



# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa

py.PAUSE = 0.3

# abrir o navegador (chrome)
py.press("win")
py.write("microsoft edge")
py.press("enter")
time.sleep(3)

# entrar no link 
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
py.click(x=621, y=391)
# escrever o seu email
py.write("pythonimpressionador@gmail.com")
py.press("tab") # passando pro próximo campo
py.write("sua senha")
py.press("enter") # clique no botao de login
time.sleep(3)

import pandas as pd

tabela = pd.read_csv("Aula/produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    py.click(x=613, y=277)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    py.write(str(codigo))
    # passar para o proximo campo
    py.press("tab")
    # preencher o campo
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(tabela.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    py.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim