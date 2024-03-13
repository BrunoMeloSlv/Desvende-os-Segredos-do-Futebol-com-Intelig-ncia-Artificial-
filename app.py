import pandas as pd
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By



service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.footstats.com.br/#/ranking/jogadores/803")
driver.implicitly_wait(30)

drop_down = Select(driver.find_element( By.XPATH, '//*[@id="fundamentos"]'))

options = drop_down.options

dfs = []

for option in options:
    
    print("Opção Combo: " + option.text)
    
    drop_down.select_by_visible_text(option.text)
    
    time.sleep(6)
    
    xpath = '//table/tbody/tr'
    elements = driver.find_elements(By.XPATH, value=xpath)
       
    xpath2 = '//table/thead/tr[1]/th'
    elements2 = driver.find_elements(By.XPATH, value=xpath2)
    
    linhas  = len(elements)
    colunas = len(elements2)
    
    tabela = []

    print("Colunas: " + str(colunas) + " Linhas: " + str(linhas))
    
    for i in range(1,linhas):
        
        print(i)
        
        linha = []
        
        for j in range(1,colunas+1):
            
            if (i == 1):
                if (j == 1):
                    linha.append("Equipe")
                    linha.append("Link Escudo")
                    coluna = driver.find_element(By.XPATH, value = "//table/thead/tr["+str(i)+"]/th["+str(j)+"]").text
                    linha.append(coluna)
                else:
                    coluna = driver.find_element(By.XPATH, value = "//table/thead/tr["+str(i)+"]/th["+str(j)+"]").text
                    linha.append(coluna)
            else:
                if (j == 1):
                    link = driver.find_element(By.XPATH, value = "//table/tbody/tr["+str(i)+"]/td["+str(j)+"]/img").get_attribute("src")
                    equipe = link.split("/")
                    linha.append(equipe[5].replace(".png", ""))
                    linha.append(link)
                    coluna = driver.find_element(By.XPATH, value = "//table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
                    linha.append(coluna)
                else:
                    coluna = driver.find_element(By.XPATH, value = "//table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
                    linha.append(coluna)
            
        tabela.append(linha)
    
    df = pd.DataFrame(tabela)
    
    dfs.append(df)

path = 'foot.xlsx'

ew =  pd.ExcelWriter(path, engine="xlsxwriter")
x = 0

for option in options:
    
    df = pd.DataFrame(dfs[x])
    df.to_excel(ew, sheet_name=option.text, index=False)
    x+=1

ew.save()
        

    
   
    
    
    
    
    
    #print("Colunas: " + str(colunas) + " Linhas: " + str(linhas))
    
    
    
    
driver.close()    