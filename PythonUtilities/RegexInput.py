import re

def main():
    print("Bem-vindo ao validador de regex!")
    regex_pattern = input("Digite a expressão regular: ")

    while True:
        text_to_check = input("Digite o texto a ser verificado (ou 'sair' para sair): ")
        
        if text_to_check.lower() == 'sair':
            print("Encerrando o programa.")
            break
        
        if re.fullmatch(regex_pattern, text_to_check):
            print("O texto está de acordo com o padrão regex.")
        else:
            print("O texto NÃO está de acordo com o padrão regex.")

if __name__ == "__main__":
    main()