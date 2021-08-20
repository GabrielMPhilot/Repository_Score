from re import T
import streamlit as st
import numpy as np
import pandas as pd
import base64
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from computer.data_process import *
from computer.data_front import *
from computer.funcomputer import *
import time

st.image('[LOGO] Eduqo.png')

# Titulo


"""
# 🌡️ Repositorios - Produto


"""

# Side bar
## Imagem na side bar
image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por: Gabriel Philot (Tio Gibbs)')
st.sidebar.write('#### Material de apoio, caso queira saber mais sobre o projeto.')
st.sidebar.write('####')
st.sidebar.write("##### Github:  [link](https://github.com/GabrielMPhilot/EduqoHealthScoreSc)")
st.sidebar.write('#')
st.sidebar.write('#### Resultado da classificação de nosso modelo:',get_table_download_link(tab_quartil), unsafe_allow_html=True)

# Grande ideia

"""
### 💡 Grande ideia do Projeto
O objetivo desse projeto é criar um HealthScore escalavel e preciso sobre nossos clientes.
Utilizamos primeiramente dados diversos da usabilidade do Produto (por enquanto), para criarmos
métricas que consigam mapear se nossos clientes estão utilizando a plataforma de maneira adequada,
com as métricas é formado um modelo para Rankear cada escola em um grau de risco especifico.

### 💾 Dados utilizados
Os dados utilizados foram segmentados (por enquanto) em 3 diferentes tabelas.
"""
"""
#### 1. Tabela de Variações:
Essa tabela contempla dados de variação do n° de alunos, variação do n° A.A's subidas (proffs),
variação do n° de interação de alunos em A.A's, variação do n° de conteúdos em caderno subidos (proffs) e
variação do n° de interação de alunos em conteúdos do caderno. O intervalo de extração desses dados é de
dados de  **01/03/2020 até 01/08/2020 e  01/03/2021 até 01/08/2021**.

#### 2. Tabela de Questões:
Essa Tabela contempla dados do n° de questões totais subidas(proffs/admin), n° de questões discursivas subidas(proffs/admin),
n° de questões totais do banco subidas (proffs/admin), n° de questões discursivas do banco subidas (proffs/admin). O intervalo de extração desses dados é de
dados de  **01/01/2021 até 01/08/2021**.
#### 3. Tabela de Relatórios:
Essa Tabela contempla dados do n° de vizualização de relátorios (proffs/admin) de A.A's, n° de vizualização de relátorios (proffs/admin) de S.Exs,
n° de vizualização de relátorios (proffs/admin) de Cadernos, n° de vizualização de relátorios (proffs/admin) de AD's, n° de vizualização de relátorios (proffs/admin) Mensais (QBR,Mensal). O intervalo de extração desses dados é de
dados de  **01/01/2021 até 01/08/2021**.
"""
"""
### 🔍 Certo agora vamos para os **Resultados**.

"""
# CARDS

figa = go.Figure()

figa.add_trace(go.Indicator(
    #mode = "number+delta",
    value = total_escolas ,
    domain = {'x': [0.25, 0.75], 'y': [0.7, 1]},
    title = {"text": "N° de escolas analisadas<br><span style='font-size:0.8em;color:gray'>"}))
    ##delta = {'reference': 400, 'relative': True, 'position' : "top"}))
figa.add_trace(go.Indicator(
    #mode = "number+delta",
    value = percen_risco,
    domain = {'x': [0.25, 0.75], 'y': [0, 0.3]},
    title = {"text": "<span style='font-size:1em;color:red'>%<br><span style='font-size:0.8em;color:red'>de escolas em Risco alto (Repositórios)</span><br>"}))
    ##delta = {'reference': 400, 'relative': True, 'position' : "top"}))
st.plotly_chart(figa)

tab_quartil
# Gráfico 1. Health Score - Pontuação via nosso modelo


fig =px.bar(grafico_um, x='Risco', y='Quantidade de escolas',
           color='Risco',
           color_discrete_sequence=["#E45756","#F58518","#54A24B","#4C78A8"],
           #color_discrete_sequence=px.colors.qualitative.T10,
            text=grafico_um['Porcentagem'])


fig.update_xaxes(showgrid=False)
fig.update_layout(title = "Distribuição no N° de escolas por grau de Risco")

st.plotly_chart(fig)

left_column, right_column = st.columns(2)
pressed = right_column.button('Download Resultado')
if pressed:
    left_column.write(get_table_download_link(tab_quartil), unsafe_allow_html=True)

"""
"""
"""
### 🩺 Lista com Namespaces classificados
"""
lista_resul
"""
"""
"""
### 📊 Agora para visualização das Métricas
"""
####################################### FILTRO ##############################
"""
"""
#lista_resul
"""
#### Escolha um namespace
"""


select = st.selectbox('', namespace_list, key='2')

'Aguarde só um momentinho'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Processando {i+1}')
  bar.progress(i + 1)
  time.sleep(0.03)
'...pronto!'

aux_show=1
a_dict=0

# Mostrando grau de risco do namespace
ans=lista_resul.copy()
ans=ans[(ans["namespace"]==select)].reset_index(drop=True)
ans=ans.loc[0,"Risco"]


"""
"""
if ans == 'Risco alto':
    st.write('### O Grau de Risco do namespace é: ',ans," 🔥")
elif ans == 'Risco médio alto':
    st.write('### O Grau de Risco do namespace é: ',ans," ⚠️")
elif ans == 'Risco médio baixo':
    st.write('### O Grau de Risco do namespace é: ',ans," 🥈")
elif ans == 'Risco baixo':
    st.write('### O Grau de Risco do namespace é: ',ans," 🥇")

"""
"""
"""
"""
# Gráfico conteudos
f_cont=t_cont_grafico[(t_cont_grafico["namespace"]==select)]
f_cont=t_cont_media_grafico.append(f_cont).reset_index(drop=True)
f_cont=df_set_plotly(f_cont)

fig_cont =px.bar(f_cont, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=f_cont['Valor'])


fig_cont.update_xaxes(showgrid=False)
fig_cont.update_layout(title = "Métricas na Tabela de Conteúdos")


st.plotly_chart(fig_cont)


# Gráfico relatorios
f_rela=t_rela_grafico[(t_rela_grafico["namespace"]==select)]
f_rela=t_rela_media_grafico.append(f_rela).reset_index(drop=True)
f_rela=df_set_plotly(f_rela)

fig_rela =px.bar(f_rela, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=f_rela['Valor'])


fig_rela.update_xaxes(showgrid=False)
fig_rela.update_layout(title = "Métricas na Tabela de Relátorios")


st.plotly_chart(fig_rela)

# Gráfico questoes
f_quest=t_quest_grafico[(t_quest_grafico["namespace"]==select)]
f_quest=t_quest_media_grafico.append(f_quest).reset_index(drop=True)
f_quest=df_set_plotly(f_quest)

fig_quest =px.bar(f_quest, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=f_quest['Valor'])


fig_quest.update_xaxes(showgrid=False)
fig_quest.update_layout(title = "Métricas na Tabela de Questões")


st.plotly_chart(fig_quest)

# Gráfico engajamento
f_eng=t_eng_grafico[(t_eng_grafico["namespace"]==select)]
f_eng=t_eng_media_grafico.append(f_eng).reset_index(drop=True)
f_eng=df_set_plotly(f_eng)

fig_engaja =px.bar(f_eng, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=f_eng['Valor'])


fig_engaja.update_xaxes(showgrid=False)
fig_engaja.update_layout(title = "Métricas na Tabela de Engajamento")


st.plotly_chart(fig_engaja)