# Instalar biblioteca de similaridade (rapidfuzz é mais rápida e moderna que fuzzywuzzy)
!pip install rapidfuzz

from rapidfuzz import fuzz, process

class ConhecimentoBase:
    def __init__(self):
        self.respostas = {
            "o que é software": "Software é um programa de computador, uma sequência lógica de instruções para manipular informações. Também inclui a documentação associada.",
            "o que é um sistema": "Sistema é um conjunto de componentes inter-relacionados (software, hardware e recursos humanos) que operam de forma unificada para atingir um objetivo comum.",
            "para que serve a materia de engenharia de software": "A Engenharia de Software é essencial para produzir softwares confiáveis e econômicos, além de permitir a reutilização de componentes.",
            "qual o papel do analista de sistemas": "O Analista de Sistemas é fundamental nos processos de engenharia de software, responsável por pesquisar, planejar, coordenar equipes e recomendar soluções, atuando como uma 'ponte' entre programadores e usuários.",
            "o que é poo": "Programação Orientada a Objetos (POO) é um paradigma moderno que organiza o código em torno de objetos, promovendo modularidade e reuso. Seus pilares incluem encapsulamento, herança e polimorfismo.",
            "o que é um processo de software": "Um Processo de Software é um conjunto de atividades e resultados relacionados que levam à produção de um software. Ele cria padronização, permite reuso de partes e guia as atividades de um projeto.",
            "quais as fases da análise de sistemas": "As fases da análise de sistemas incluem Análise, Projeto, Implementação, Testes, Documentação e Manutenção.",
            "quais as categorias de software": "Existem diversas categorias, como software de sistema, de aplicação, embarcado, para aplicações web/móveis e de Inteligência Artificial."
        }

    def buscar_resposta(self, pergunta_chave):
        pergunta_chave_formatada = pergunta_chave.lower().strip()
        
        # Busca a chave mais parecida usando similaridade
        melhor_chave, score, _ = process.extractOne(
            pergunta_chave_formatada,
            self.respostas.keys(),
            scorer=fuzz.token_sort_ratio
        )
        
        if score >= 60:  # Limite mínimo de similaridade
            return self.respostas[melhor_chave]
        else:
            return "Desculpe, não encontrei uma resposta direta. Tente reformular ou perguntar sobre 'software', 'sistema', 'POO', 'analista de sistemas'."

class AssistenteAnalista:
    def __init__(self, nome="Assistente AI", conhecimento_base=None):
        self.nome = nome
        self.conhecimento = conhecimento_base if conhecimento_base else ConhecimentoBase()

    def saudar(self):
        print(f"Olá! Eu sou seu {self.nome}. Estou aqui para ajudar com dúvidas sobre Engenharia de Software e Análise de Sistemas.")
        print("Você pode perguntar coisas como 'o que é software', 'qual o papel do analista de sistemas', 'o que é poo'.")
        print("Digite 'sair' a qualquer momento para finalizar.")

    def interagir(self):
        self.saudar()
        while True:
            pergunta_usuario = input("\nVocê: ")
            if pergunta_usuario.lower().strip() in ["sair", "adeus", "finalizar", "tchau"]:
                print(f"{self.nome}: Até mais! Sempre à disposição para auxiliar em seus desafios de sistemas.")
                break
            else:
                resposta = self.conhecimento.buscar_resposta(pergunta_usuario)
                print(f"{self.nome}: {resposta}")

# --- Execução ---
if __name__ == "__main__":
    minha_base = ConhecimentoBase()
    meu_assistente = AssistenteAnalista(nome="Analista-Bot", conhecimento_base=minha_base)
    meu_assistente.interagir()
