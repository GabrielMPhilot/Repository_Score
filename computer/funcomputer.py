
# Funçoes
from re import T
import pandas as pd
from datetime import date, timedelta
import time
import base64
from pandas.core.frame import DataFrame


# reorder columns
def reorder_columns(dataframe, col_name, position):
    """Reorder a dataframe's column.
    Args:
        dataframe (pd.DataFrame): dataframe to use
        col_name (string): column name to move
        position (0-indexed position): where to relocate column to
    Returns:
        pd.DataFrame: re-assigned dataframe
    """
    temp_col = dataframe[col_name]
    dataframe = dataframe.drop(columns=[col_name])
    dataframe.insert(loc=position, column=col_name, value=temp_col)
    return dataframe

# columns avareges
def media_das_colunas(dataframe):
    """Get averages of each columns in the dataframe.

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: Average dataframe.
    """
    # getting column names
    columns = dataframe.columns.values.tolist()
    columns.remove("namespace")

    # df auxiliar
    df=pd.DataFrame()

    # laço de interação
    for col in columns:
        lista_mean=list()
        m=float("{:.2f}".format((dataframe[col].mean())))
        lista_mean.append(m)
        df_aux=pd.DataFrame(lista_mean)
        df[col]=df_aux.sum()
    
    #atribuindo nome
    df["namespace"]="Média Eduqo"
    # reordenando df
    df=reorder_columns(df,"namespace",0)
    return df

# dataframe normalization
def norm_dataframe(dataframe):
    """Get normalization of each columns in the dataframe.

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: Normalized dataframe.
    """
    # gettings column names
    columns = dataframe.columns.values.tolist()
    columns.remove("namespace")

    # df auxiliar
    df=pd.DataFrame()
    
    # interação normalização
    for col in columns:
        var_min=dataframe[col].min()
        var_max=dataframe[col].max()
        df[col]=((dataframe[col]-var_min)/var_max-var_min).round(2)
    
    # pegando os namespaces
    df["namespace"]=dataframe["namespace"]
    df=reorder_columns(df, "namespace",0)
    return df

# risc quart's classification
def quartiles_classification(dataframe):
    """Classification by dataframe quartile

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe sorted by quartile
    """
    # aux variables for classification of the quartiles
    dataframe["quartil"]=0
    dataframe["Risco"]=0
    col="soma"
    
    
    #removing out liers
    var_quartile_025=dataframe[col].quantile([0.25])
    var_quantile_075=dataframe[col].quantile([0.75])
    for i in range(len(dataframe[col])):
        a=0
        b=0
        var_aux=dataframe[col][i]
        if var_aux > var_quantile_075[0.75]:
            a=1
            b="Risco baixo"
        elif var_aux < var_quartile_025[0.25]:
            a=4
            b="Risco alto"
        else:
            #auxiliar quartil
            aux_var_quartil=dataframe[(dataframe[col]>var_quartile_025[0.25]) & (dataframe[col] < var_quantile_075[0.75])]
            q=(aux_var_quartil[col].max()-aux_var_quartil[col].min())/4
            m=aux_var_quartil[col].min()
            aux=dataframe[col][i]
            if  aux >= m and aux < m +q:
                a=4
                b="Risco alto"
            elif aux >= m+q and aux < m + 2*q:
                a=3
                b="Risco médio alto"
            elif aux >= m+2*q and aux < m + 3*q:
                a=2
                b="Risco médio baixo"
            else:
                a=1
                b="Risco baixo"
        dataframe.loc[i, "quartil"]=a
        dataframe.loc[i,"Risco"]=b
    
    return dataframe
        
# df to link
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="listanamespaces.csv">Clique aqui para baixar o CSV</a>'
    return href

# set up dataframe for plotly bar graph
def df_set_plotly(data_frame):
     """Set up dataframe for plotly bar graph

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe ready for plot the graph
    """
     # gettings column names
     coluna = data_frame.columns.values.tolist()
     coluna.remove("namespace")
     df=pd.DataFrame()
     for col in coluna:
        for i in range(len(data_frame[col])):
            ns=data_frame.loc[i,"namespace"]
            co=col
            valor=data_frame.loc[i, col]
            new_row={'Namespace': ns, 'Métricas': co, 'Valor': valor}
            df=df.append(new_row, ignore_index=True)
     return df
    
 
    

    







