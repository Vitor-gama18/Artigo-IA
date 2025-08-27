import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# 1. Definição do Problema
# O problema é prever o tempo de entrega de um software baseado no número de requisitos.


# 2. Definição dos Dados (Entradas e Saídas) - CORRIGIDO
# Em Machine Learning, os dados são a "informação" que os algoritmos sofisticados analisam [1].
# A aplicação de Inteligência Artificial na indústria, por exemplo, utiliza tecnologias como
# aprendizado de máquina e análise preditiva para otimizar processos [2, 3]. Para isso,
# é fundamental fornecer dados concretos para que os algoritmos possam aprender padrões [1].
#
# Dados de exemplo:
# (10 requisitos, 10 dias), (20 requisitos, 18 dias), (30 requisitos, 25 dias),
# (40 requisitos, 32 dias), (50 requisitos, 40 dias), (60 requisitos, 45 dias)
#
# X = Número de requisitos (variável independente)
# y = Tempo de entrega em dias (variável dependente)
#
# A correção aqui é popular os arrays com valores numéricos reais, e não deixá-los vazios.
# O método .reshape(-1, 1) é necessário para formatar 'X' como uma coluna, conforme exigido
# pela biblioteca scikit-learn para a variável independente.


X = np.array([10, 20, 30, 40, 50, 60]).reshape(-1, 1) # CORRIGIDO: Dados reais fornecidos e formatados
y = np.array([10, 18, 25, 32, 40, 45])              # CORRIGIDO: Dados reais fornecidos


print("Dados de Entrada (X - Requisitos):", X.flatten())
print("Dados de Saída (y - Tempo de Entrega):", y)
print("-" * 30)


# 3. Escolha e Treinamento do Modelo
# Softwares de Inteligência Artificial utilizam algoritmos sofisticados para analisar
# e solucionar problemas complexos [1]. A Regressão Linear é um exemplo de tal algoritmo
# usado para análise preditiva [2, 3].
model = LinearRegression()
model.fit(X, y) # Esta linha agora pode ser executada com sucesso, pois X e y contêm dados.


print("Modelo treinado com sucesso!")
print(f"Coeficiente (inclinação): {model.coef_[0]:.2f}")
print(f"Intercepto (ponto de corte): {model.intercept_:.2f}")
print("-" * 30)


# 4. Realização de Previsões
# Exemplo de previsão: tempo de entrega para 70 requisitos
requisitos_novos = np.array([[70]])
tempo_previsto = model.predict(requisitos_novos)
print(f"Para {requisitos_novos[0][0]} requisitos, o tempo de entrega previsto é de {tempo_previsto[0]:.2f} dias.")
print("-" * 30)


# 5. Visualização dos Resultados
plt.scatter(X, y, color='blue', label='Dados Reais')
plt.plot(X, model.predict(X), color='red', label='Linha de Regressão')
plt.xlabel('Número de Requisitos')
plt.ylabel('Tempo de Entrega (dias)')
plt.title('Regressão Linear: Requisitos vs. Tempo de Entrega')
plt.legend()
plt.grid(True)
plt.show()
