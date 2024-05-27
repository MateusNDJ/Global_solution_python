import os
os.system('cls')

# Listas pré-definidas de habitats e animais marinhos em extinção
h# Listas pré-definidas de habitats e animais marinhos em extinção
habitats = ["Recifes de coral", "Manguezais", "Prados de ervas marinhas", "Florestas de algas", "Pântano Salgado"]
animais = ["Tartaruga-de-pente", "Vaquita", "Golfinho do Rio", "Baleia Narval", "Tartaruga Verde"]

# Função para visualizar habitats
def visualizar_habitats():
    print("Habitats Marinhos em Extinção:")
    for i, habitat in enumerate(habitats):
        print(f"{i+1}. {habitat}")
    print("------------------------")

# Função para visualizar animais
def visualizar_animais():
    print("Animais Marinhos em Extinção:")
    for i, animal in enumerate(animais):
        print(f"{i+1}. {animal}")
    print("------------------------")

# Função para simular uma ação de limpeza de praia
def limpeza_praia():
    print("Você realizou uma ação de limpeza de praia. Parabéns por ajudar a proteger nossos oceanos!")
    print("------------------------")

# Função para simular um programa de educação ambiental
def educacao_ambiental():
    print("Você realizou um programa de educação ambiental. Parabéns por ajudar a conscientizar sobre a importância de nossos oceanos!")
    print("------------------------")

# Loop principal do programa
while True:
    print("1. Visualizar habitats em extinção")
    print("2. Visualizar animais em extinção")
    print("3. Realizar uma ação de limpeza de praia")
    print("4. Realizar um programa de educação ambiental")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        visualizar_habitats()
    elif opcao == '2':
        visualizar_animais()
    elif opcao == '3':
        limpeza_praia()
    elif opcao == '4':
        educacao_ambiental()
    elif opcao == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
