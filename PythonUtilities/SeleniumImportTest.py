from selenium import webdriver
import pandas as pd

# Inicializar o driver do Chrome
chrome_driver_path = 'Caminho/para/o/chromedriver.exe'  # Coloque o caminho para o chromedriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abrir a página da Wikipedia
url = 'https://pt.wikipedia.org/wiki/P%C3%A1gina_principal'
driver.get(url)

# Localizar o link para a página de exemplo de tabela
link_text = "Lista de países por população"
link_element = driver.find_element_by_link_text(link_text)
link_element.click()

# Esperar carregar a página
driver.implicitly_wait(10)

# Localizar a tabela e pegar o HTML
table_element = driver.find_element_by_xpath('//table[@class="wikitable"]')
table_html = table_element.get_attribute('outerHTML')

# Fechar o navegador
driver.quit()

# Converter a tabela HTML para um DataFrame do pandas
df = pd.read_html(table_html)[0]

# Salvar o DataFrame em um arquivo CSV
csv_path = 'exemplo.csv'
df.to_csv(csv_path, index=False)

# Exibir mensagem na tela
print("Tabela baixada e salva em", csv_path)
