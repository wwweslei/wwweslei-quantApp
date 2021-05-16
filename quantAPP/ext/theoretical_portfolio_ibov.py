from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


URL = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"

firefox = webdriver.Firefox()
firefox.get(URL)


def wait_while_Finding(seletor, name):
    return WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((seletor, name))
    )


wait_while_Finding(By.ID, "segment").send_keys("Setor de Atuação")
wait_while_Finding(By.ID, "selectPage").send_keys(Keys.ARROW_DOWN)
wait_while_Finding(By.ID, "selectPage").send_keys(Keys.ARROW_DOWN)
wait_while_Finding(By.ID, "selectPage").send_keys(Keys.ARROW_DOWN)
time.sleep(9)
table = wait_while_Finding(By.CLASS_NAME, "table").get_attribute('outerHTML')
df = pd.read_html(table)[0]
df.drop(df.tail(2).index, inplace=True)
df.columns = ['Setor', 'Código', 'Ação', 'Tipo',
              'Qtde. Teórica', 'Part. (%)', 'Part. (%)Acum']

print(df)