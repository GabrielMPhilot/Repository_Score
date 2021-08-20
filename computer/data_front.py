# Parte relacionada a o front

from os import sep
from re import A
import numpy as np
import pandas as pd
from computer.funcomputer import *
from computer.data_process import *
import streamlit as st

# lista para download
lista_resul=reorder_columns(tab_quartil,"Risco",1)
lista_resul=lista_resul.iloc[:,0:2]

#lista resul com medalhas
list_front=lista_resul.copy()
col_front="Risco"
for i in range(len(list_front[col_front])):
    aux_front=list_front.loc[i,col_front]
    if aux_front=='Risco alto':
        list_front.loc[i,col_front]='🔥'+''+aux_front
    elif aux_front=='Risco médio alto':
        list_front.loc[i,col_front]='⚠️'+''+aux_front
    elif aux_front=='Risco médio baixo':
        list_front.loc[i,col_front]='🥈'+''+aux_front
    else:
        list_front.loc[i,col_front]='🥇'+''+aux_front





# Total de escolas analisadas (CARD)
total_escolas=tab_quartil["namespace"].tolist()
total_escolas=len(total_escolas)


# Preparando dados para gráfico principal da classificação
# /Porcentagem de risco (Repositorio)

# Extraindo soma
tab_group_quartil=tab_quartil.groupby(['Risco'])[['quartil']].count().reset_index()
tab_group_quartil=tab_group_quartil.rename(columns={"quartil": "Quantidade de escolas"})
var_aux_divisao_percen=tab_group_quartil["Quantidade de escolas"].sum()

tab_group_quartil["Porcentagem"]=((tab_group_quartil["Quantidade de escolas"]/var_aux_divisao_percen)*100).round(2)

# porcentagem de risco (CARD)

percen_risco=tab_group_quartil[(tab_group_quartil["Risco"]=='Risco alto')]
percen_risco=percen_risco["Porcentagem"].sum()

# Gráfico 1. Health Score - Pontuação via nosso modelo

grafico_um=tab_group_quartil.copy()
grafico_um["Porcentagem"]=grafico_um["Porcentagem"].astype(str)+'%'

# ordenando o gráfico

grafico_um["ordem"]=0
for i in range(len(grafico_um["Risco"])):
    var_ordem=0
    var_grafico_ordem=grafico_um["Risco"][i]
    if var_grafico_ordem=='Risco alto':
        b=int(1)
    elif var_grafico_ordem=='Risco médio alto':
        b=int(2)
    elif var_grafico_ordem=='Risco médio baixo':
        b=int(3)
    else:
        b=int(4)
    grafico_um.loc[i,"ordem"]=b
grafico_um=grafico_um.sort_values(by="ordem", ascending=True).reset_index(drop=True)

# Filtro namespaces
namespace_list=tab_unida_um["namespace"].values.tolist()


