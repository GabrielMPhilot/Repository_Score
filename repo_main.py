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
st.sidebar.write("##### Github:  [link](https://github.com/GabrielMPhilot/Repository_Score)")
st.sidebar.write('#')
st.sidebar.write('#### Resultado da classificação de nosso modelo:',get_table_download_link(lista_resul), unsafe_allow_html=True)

# Grande ideia

"""
### 💡 Grande ideia do Projeto
O objetivo desse projeto é criar um HealthScore escalavel e preciso sobre nossos clientes.
Utilizamos primeiramente dados diversos da usabilidade do Produto (por enquanto), para criarmos
métricas que consigam mapear se nossos clientes estão utilizando a plataforma de maneira adequada,
com as métricas é formado um modelo para Rankear cada escola em um grau de risco especifico.

### 💾 Dados utilizados
Os dados utilizados foram segmentados (por enquanto) em 4 diferentes tabelas.
"""
"""
#### 1. Tabela de Conteudos:
Essa tabela contempla dados de conteúdos de todos os tipos do caderno, segmenta cada tipo, 
como por exemplo PDFS, Videos, Tarefas e S.Exercicios.
O intervalo de extração desses dados é de
dados de  **01/03/2020 até 15/08/2020**.
#### 2. Tabela de Questões:
Essa Tabela contempla dados do n° de questões totais subidas(prof/admin), n° de questões 
discursivas subidas(profs/admin),
n° de questões totais do banco subidas (prof/admin) . O intervalo de extração desses dados é de
dados de  **01/01/2021 até 15/08/2021**.
#### 3. Tabela de Relatórios:
Essa Tabela contempla dados do n° de vizualização de relátorios (proffs/admin/alunos) de A.A's, 
n° de vizualização de relátorios (prof/admin/alunos) de S.Exs,
n° de vizualização de relátorios (prof/admin) de Cadernos, n° de vizualização de relátorios 
(admin) de AD's, n° de vizualização de relátorios (admin) Mensais (QBR,Mensal). O intervalo de extração desses dados é de
dados de  **01/01/2021 até 15/08/2021**.
#### 4. Tabela de Engajamento com funcionalidades diferenciadas
Essa Tabela contempla dados de n° correções/interações não automatizadas com os alunos (prof/admin),
n° de resultados baixados (prof/admin), n° de comentarios no forum (prof/admin/aluno), 
n° de likes/dislikes em conteúdos (alunos) e n° de upload de vídeos/áudios subidos (alunos). O intervalo de extração desses dados é de
dados de  **01/01/2021 até 15/08/2021**.

"""

"""
### 👩🏽‍🏫 Metodologia
Com os dados, criamos métricas que tentam parametrizar o uso de uma funcionalidade da escola,
Exemplo: Número de PDFS/total de conteúdos, ou Número de vizualização de relátorios/n° de professores ativos.
Obtendo todas as métricas, fazemos a soma destas e normalizamos os dados. Após a normalização
é criado um modelo que classificamos por quartil's o Risco da escola baseado na soma de todas as métricas.


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
    left_column.write(get_table_download_link(lista_resul), unsafe_allow_html=True)

"""
"""
"""
### 🩺 Lista com todos os Namespaces classificados
"""
left_column, right_column = st.columns(2)
pressed = left_column.button('Mostrar tabela')
if pressed:
    alpha_show=1
else:
    alpha_show=0
if alpha_show==1:
    st.dataframe(list_front)

left_column, right_column = st.columns(2)
pressed = right_column.button('Esconder tabela')
if pressed:
    alpha_show=0



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
### 📑 Como interpretar os gráficos:
Nessa versão os valores que estão sendo mostrados já são tratados e mostrados,
portanto o verdadeiro valor deles é bater o olho nas colunas e ver se a coluna
relacionada a o namespace é maior ou menor que a média da eduqo (também consegue
saber o quanto é maior ou menor pela diferença de tamanho das barras).
"""
"""
"""
# Gráfico conteudos
f_cont=t_cont_grafico[(t_cont_grafico["namespace"]==select)]
f_cont=t_cont_media_grafico.append(f_cont).reset_index(drop=True)
f_cont=df_set_plotly(f_cont)

fig_cont =px.bar(f_cont, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"])#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                #text=f_cont['Valor'])


fig_cont.update_xaxes(showgrid=False)
fig_cont.update_layout(title = "Métricas na Tabela de Conteúdos")

# Obs




st.plotly_chart(fig_cont)
"""
##### Obs Gráfico de conteúdos: 
Nesse gráfico as métricas relacionadas a PDF's
e vídeos são inversamente proporcionais a pontuação, ou seja quanto menor a quantidade de conteúdos
destes tipos maior será a pontuação.
"""

# Gráfico relatorios
f_rela=t_rela_grafico[(t_rela_grafico["namespace"]==select)]
f_rela=t_rela_media_grafico.append(f_rela).reset_index(drop=True)
f_rela=df_set_plotly(f_rela)

fig_rela =px.bar(f_rela, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"])#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                #text=f_rela['Valor'])


fig_rela.update_xaxes(showgrid=False)
fig_rela.update_layout(title = "Métricas na Tabela de Relátorios")


st.plotly_chart(fig_rela)

# Gráfico questoes
f_quest=t_quest_grafico[(t_quest_grafico["namespace"]==select)]
f_quest=t_quest_media_grafico.append(f_quest).reset_index(drop=True)
f_quest=df_set_plotly(f_quest)

fig_quest =px.bar(f_quest, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"])#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                #text=f_quest['Valor'])


fig_quest.update_xaxes(showgrid=False)
fig_quest.update_layout(title = "Métricas na Tabela de Questões")


st.plotly_chart(fig_quest)

# Gráfico engajamento
f_eng=t_eng_grafico[(t_eng_grafico["namespace"]==select)]
f_eng=t_eng_media_grafico.append(f_eng).reset_index(drop=True)
f_eng=df_set_plotly(f_eng)

fig_engaja =px.bar(f_eng, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"])#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                #text=f_eng['Valor'])


fig_engaja.update_xaxes(showgrid=False)
fig_engaja.update_layout(title = "Métricas na Tabela de Engajamento")


st.plotly_chart(fig_engaja)

"""

##### Obs Gráfico de engajamento: 
 Nesse gráfico a métrica relacionada a baixar resultados
é inversamente proporcional, ou seja quanto menos resultados a escola baixar maior será a pontuação,
pois esse dado indica que a escola não está utilizando nossas ferramentas de relátorios e isso pode
vir a ser uma grande dor da escola, exemplo desse dor: Colégio Eccos.
"""

"""
### 💎 Iluminações ( Insights )
O foco ( por enquanto ) será em cima do mal uso da plataforma.
"""

expander_cont = st.expander("Métricas de Conteúdos -> (clique aqui 🖱️)")
expander_cont.write("(1) Escolas com personalização alta geralmente fazem bom uso de tarefas e série de exercícios. (2) Escolas que usam a plataforma como repositórios tendem a utilizar muitos vídeos e pdfs.")
expander_rel = st.expander("Métricas de Relátorios -> (clique aqui 🖱️)")
expander_rel.write("(1) Visualização de relatórios: Os nossos relatórios são um de nossos diferenciais para os concorrentes, e sua subutilização também pode indicar um mal uso da plataforma.")
expander_que = st.expander("Métricas de Questões -> (clique aqui 🖱️)")
expander_que.write("(1) Escolas que utilizam pouco o banco não valorizam um de nossos principais diferenciais competitivos em relação ao Google Classroom, então pode ser uma questão perigosa para potenciais churns. (2) Baixo uso de questões discursivas pode significar uma baixa personalização do uso da plataforma.")
expander_eng = st.expander("Métricas de Engajamento -> (clique aqui 🖱️)")
expander_eng.write("(1) Escolas engajadas e personalizadas, fazem uso de ferramentas como marcar/interagir com aluno para corrigir seus trabalhos (correções com interações com alunos). (2) Escolas engajadas e personalizadas interagemm e dão feedbacks constantes para seus alunos, então a conversa com alunos através de forums deve ser uma forma boa de feedback para os estudos dos alunos. (3) Baixar resultados significa que a escola não faz um bom uso de nossas ferramentas de relátorios. (4) Alunos interagindo e curtindo contéudos são um bom sinal de engajamento com a escola. (5) Alunos subindo vídeos e áudios são um bom sinal de engajamento e personalização do ensino.")


"""
### 🛠️ Próximos Passos
(1) - Receber feedback sobre nossos dados utilizados e ver se temos algo a acrescentar
"""
"""
(2) - Olhar mais a fundo as métricas de tarefas e questões discursivas pois elas podem enganar,
exemplo: Guilherme de almeida
"""
"""
(3) - Melhorar visualização na parte das tabelas das Métricas.
"""
"""
(4) - Melhorar fluxo de informações do relátorio.
"""
"""
(5) - Estatística e Machine Learning para avaliar as correlações entre as váriaveis.
"""