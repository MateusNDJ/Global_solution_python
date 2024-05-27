import os
os.system('cls')

class Habitat:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Animal:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class MarineDefense:
    def __init__(self):
        self.habitats = {
            "Recifes de coral": Habitat("Recifes de coral", "Os recifes de coral são alguns dos ecossistemas mais biodiversos do planeta, abrigando inúmeras espécies marinhas."),
            "Manguezais": Habitat("Manguezais", "Os manguezais são ecossistemas costeiros tropicais que desempenham um papel crucial na proteção contra a erosão costeira."),
            "Prados de ervas marinhas": Habitat("Prados de ervas marinhas", "Os prados de ervas marinhas são importantes habitats de alimentação e berçários para muitas espécies marinhas."),
            "Florestas de algas": Habitat("Florestas de algas", "As florestas de algas, especialmente as florestas de kelp, são habitats ricos que suportam uma grande diversidade de vida marinha."),
            "Pântano Salgado": Habitat("Pântano Salgado", "Os pântanos salgados são áreas costeiras inundadas regularmente pelas marés, fornecendo habitat para uma variedade de vida selvagem.")
        }

        self.animais = {
            "Tartaruga-de-pente": Animal("Tartaruga-de-pente", "A tartaruga-de-pente é uma espécie de tartaruga marinha criticamente ameaçada, conhecida por seu bico estreito e serrilhado."),
            "Vaquita": Animal("Vaquita", "A vaquita é uma espécie de golfinho extremamente rara, encontrada apenas no norte do Golfo da Califórnia."),
            "Golfinho do Rio": Animal("Golfinho do Rio", "Os golfinhos do rio são espécies de golfinhos que vivem em rios, e muitas dessas espécies estão gravemente ameaçadas."),
            "Baleia Narval": Animal("Baleia Narval", "A baleia narval é conhecida por sua presa longa e reta, uma característica distintiva dos machos. Esta espécie ártica está atualmente ameaçada pelo aquecimento global."),
            "Tartaruga Verde": Animal("Tartaruga Verde", "A tartaruga verde é uma grande espécie de tartaruga marinha que passa a maior parte de sua vida em habitats de águas costeiras e manguezais.")
        }

    def visualizar_habitats(self):
        print("Habitats Marinhos em Extinção:")
        for habitat in self.habitats.values():
            print(habitat.nome)

    def visualizar_animais(self):
        print("Animais Marinhos em Extinção:")
        for animal in self.animais.values():
            print(animal.nome)

    def visualizar_descricao_habitat(self, nome):
        if nome in self.habitats:
            print(self.habitats[nome].descricao)
        else:
            print("Habitat não encontrado.")

    def visualizar_descricao_animal(self, nome):
        if nome in self.animais:
            print(self.animais[nome].descricao)
        else:
            print("Animal não encontrado.")

def main():
    md = MarineDefense()

    while True:
        print("1. Visualizar habitats em extinção")
        print("2. Visualizar animais em extinção")
        print("3. Visualizar descrição de um habitat")
        print("4. Visualizar descrição de um animal")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            md.visualizar_habitats()
        elif opcao == '2':
            md.visualizar_animais()
        elif opcao == '3':
            nome = input("Digite o nome do habitat: ")
            md.visualizar_descricao_habitat(nome)
        elif opcao == '4':
            nome = input("Digite o nome do animal: ")
            md.visualizar_descricao_animal(nome)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
