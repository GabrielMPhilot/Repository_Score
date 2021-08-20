# Aqui iremos receber / unir os dataframes, fazer copias para front
# normalizar dados, tirar medias e classificar os quartil's

from os import sep
import numpy as np
import pandas as pd
from computer.funcomputer import *



# Recebendo os dataframes

## Tabela de conteudos
t_conteudos=pd.read_csv("./csvs/tab_conteudos.csv")
del t_conteudos['Unnamed: 0']
t_conteudos=t_conteudos.replace(np.inf, 0)

## Tabela de relátorios
t_relas=pd.read_csv("./csvs/tab_rela23.csv")
del t_relas['Unnamed: 0']
t_relas=t_relas.replace(np.inf, 0)

# Tabela de relátorios
t_quest=pd.read_csv("./csvs/tab_quest.csv")
del t_quest['Unnamed: 0']
t_quest=t_quest.replace(np.inf, 0)

# Tabela de engajamento
t_engaj=pd.read_csv("./csvs/tab_engaja.csv")
del t_engaj['Unnamed: 0']
t_engaj=t_engaj.replace(np.inf, 0)


# Retirando médias das tabelas

# Média conteudos
t_conteudos_media=media_das_colunas(t_conteudos)


# Média relátorios
t_relas_media=media_das_colunas(t_relas)

# Média questões 
t_quest_media=media_das_colunas(t_quest)

# Medái engaja
t_engaj_media=media_das_colunas(t_engaj)

# União

tab_unida_um=pd.merge(t_conteudos, t_relas, on="namespace", how='outer')
tab_unida_um=pd.merge(tab_unida_um, t_quest, on="namespace", how='outer')
tab_unida_um=pd.merge(tab_unida_um, t_engaj, on="namespace", how="outer")
tab_unida_um=tab_unida_um.replace(np.nan, 0)

t=tab_unida_um

# Normalização

tab_norm_um=norm_dataframe(tab_unida_um)

# Somando pontos

tab_soma=tab_norm_um.copy()
tab_soma["soma"]=tab_soma.sum(axis=1, numeric_only=True)
tab_soma=reorder_columns(tab_soma,"soma",1)
tab_soma=tab_soma.iloc[:,:2]
tab_soma=tab_soma.sort_values(by="soma", ascending="True").reset_index(drop=True)

#  Classificação por quartil's
# box plot para input
tab_quartil=quartiles_classification(tab_soma)

# Dados para gráficos

# conteudos
t_cont_grafico=norm_dataframe(t_conteudos)
t_cont_media_grafico=media_das_colunas(t_cont_grafico)

# relatorios
t_rela_grafico=norm_dataframe(t_relas)
t_rela_media_grafico=media_das_colunas(t_rela_grafico)

# questões
t_quest_grafico=norm_dataframe(t_quest)
t_quest_media_grafico=media_das_colunas(t_quest_grafico)

# questoes
t_eng_grafico=norm_dataframe(t_engaj)
t_eng_media_grafico=media_das_colunas(t_eng_grafico)
