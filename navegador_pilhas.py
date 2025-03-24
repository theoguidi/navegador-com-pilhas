# Implementação da navegação com pilhas
class Navegador:
    def __init__(self):
        self.pilha_voltar = []
        self.pilha_avancar = []
        self.pagina_atual = None

    def acessar_pagina(self, url):
        if self.pagina_atual:
            self.pilha_voltar.append(self.pagina_atual)
        self.pilha_avancar.clear()
        self.pagina_atual = url
        print(f"Acessando: {self.pagina_atual}")

    def voltar(self):
        if self.pilha_voltar:
            self.pilha_avancar.append(self.pagina_atual)
            self.pagina_atual = self.pilha_voltar.pop()
            print(f"Voltando para: {self.pagina_atual}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if self.pilha_avancar:
            self.pilha_voltar.append(self.pagina_atual)
            self.pagina_atual = self.pilha_avancar.pop()
            print(f"Avançando para: {self.pagina_atual}")
        else:
            print("Não há páginas para avançar.")

# Exemplo de uso
navegador = Navegador()
navegador.acessar_pagina("www.google.com")
navegador.acessar_pagina("www.youtube.com")
navegador.voltar()
navegador.avancar()
