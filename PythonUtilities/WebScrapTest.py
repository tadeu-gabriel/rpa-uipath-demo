import requests
from bs4 import BeautifulSoup

def get_wikipedia_homepage():
    url = "https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Erro ao acessar a página inicial do Wikipedia.")

def extract_featured_articles(content):
    soup = BeautifulSoup(content, "html.parser")
    featured_articles = soup.find_all("div", class_="ambox-content")
    
    articles = []
    for article in featured_articles:
        articles.append(article.get_text())
    
    return articles

def main():
    try:
        print("Coletando informações da página inicial do Wikipedia...\n")
        
        content = get_wikipedia_homepage()
        featured_articles = extract_featured_articles(content)
        
        print("Artigos em destaque na Página Principal do Wikipedia:\n")
        for i, article in enumerate(featured_articles, start=1):
            print(f"{i}. {article}\n")
    
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()