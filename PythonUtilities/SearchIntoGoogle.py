import requests
from bs4 import BeautifulSoup

class GoogleNewsScraper:
    def __init__(self, termo_pesquisa):
        self.termo_pesquisa = termo_pesquisa
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def buscar_resultados(self):
        url = f"https://www.google.com/search?q={self.termo_pesquisa}+últimos+jogos&tbm=nws"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.content
        else:
            raise Exception("Erro ao realizar a pesquisa.")

    def extrair_resultados(self, content):
        soup = BeautifulSoup(content, "html.parser")
        resultados = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        return [resultado.get_text() for resultado in resultados]

def main():
    try:
        termo_pesquisa = input("Digite o termo de pesquisa: ")
        scraper = GoogleNewsScraper(termo_pesquisa)
        
        content = scraper.buscar_resultados()
        ultimos_jogos = scraper.extrair_resultados(content)

        print(f"Últimos jogos relacionados a '{termo_pesquisa}':\n")
        for i, jogo in enumerate(ultimos_jogos, start=1):
            print(f"{i}. {jogo}")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
