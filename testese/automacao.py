import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
# passo 1 entrar no site
pyautogui.press('win')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)  

# passo 2 fazer login
pyautogui.click(x=525, y=359)
pyautogui.write('xaulinMatadorDePorco@gmail.com')
pyautogui.press('tab')


pyautogui.click(x=515, y=456)
pyautogui.write('mamamia')  
pyautogui.press('tab')  

pyautogui.click(x=663, y=520)

# passo 3 importar base de dados
tabela = pandas.read_csv('produtos.csv')

# passo 4 cadastrar produtos
# repertir passo 4
for linha in tabela.index:
    pyautogui.click(x=563, y=243)
    
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
        pyautogui.press('tab')
    
    pyautogui.press('enter')
    pyautogui.scroll(1000)



