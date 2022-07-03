import pandas as pd
import numpy as np
from scipy import stats

'''
Problem:
Uma pesquisa procurou verificar o grau de estresse de 115 colaboradores de uma empresa obedece uma distribuição normal. Os trabalhadores responderam utilizando uma escala Likert à afirmação “Considero-me estressado”, sendo:
discordo totalmente;
discordo
nem concordo e nem discordo
concordo
concordo totalmente
A frequência para cada resposta é apresentada na tabela a seguir:
'''

question = np.array([1,2,3,4,5])
frequency = np.array([10,25,45,20,15])
n = sum(frequency)
mean = np.mean(question)
std = 1.58
alpha = 0.05

df = pd.DataFrame({'stress':question, 'frequency':frequency})


def get_freq_relative(df, n):
    relative_frequency = df['frequency']/n
    return relative_frequency

