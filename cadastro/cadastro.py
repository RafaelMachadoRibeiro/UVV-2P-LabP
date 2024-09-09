import csv
import os

cadastros = []

def carregar_csv():
    if os.path.exists('cadastros.csv'):
        with open('cadastros.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                cadastros.append([int(row[0]), row[1], row[2]])
        print("Cadrastos carregados com sucesso!")
    else:
        print("O arquivo CSV não foi encontrado.")

def salvar_csv():
    with open('cadastros.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nome", "Idade"])
        for item in cadastros:
            writer.writerow(item)
    print("Lista salva no arquivo cadastros.csv")

def gerar_proximo_id():
    if not cadastros:
        return 1
    else:
        ids_existentes = [item[0] for item in cadastros]
        return max(ids_existentes) + 1

def cadastrar():
    id = gerar_proximo_id()
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    cadastros.append([id, nome, idade])
    print(f"Cadastro {id} adicionado com sucesso!")

def listar():
    if not cadastros:
        print("Nenhum cadastro encontrado.")
    else:
        for item in cadastros:
            print(f"ID: {item[0]} | Nome: {item[1]} | Idade: {item[2]}")

def consultar():
    id_consulta = input("Digite o ID do cadastro a ser consultado: ")
    for item in cadastros:
        if item[0] == int(id_consulta):
            print(f"ID: {item[0]} | Nome: {item[1]} | Idade: {item[2]}")
            return
    print(f"Cadastro com ID {id_consulta} não encontrado.")

def excluir():
    id_excluir = input("Digite o ID do cadastro a ser excluído: ")
    for item in cadastros:
        if item[0] == int(id_excluir):
            cadastros.remove(item)
            print(f"Cadastro com ID {id_excluir} removido com sucesso.")
            return
    print(f"Cadastro com ID {id_excluir} não encontrado.")

def menu():
    carregar_csv() 

    while True:
        print("\nMenu:")
        print("0 - Sair")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Consultar")
        print("4 - Excluir")
        escolha = input("Escolha 1 opção: ")

        if escolha == '0':
            salvar_csv()
            print("Saindo...")
            break
        elif escolha == '1':
            cadastrar()
        elif escolha == '2':
            listar()
        elif escolha == '3':
            consultar()
        elif escolha == '4':
            excluir()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()