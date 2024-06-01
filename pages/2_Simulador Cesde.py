import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

import plotly.graph_objects as go

st.write("Simulador Cesde")

df = pd.read_csv('static/datasets/data.csv')

gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU = sorted(df['JORNADA'].unique())
horarioU = sorted(df['HORARIO'].unique())
submodulosU = sorted(df['SUBMODULO'].unique())
docentesU = sorted(df['DOCENTE'].unique())
momentosU = sorted(df['MOMENTO'].unique())


col1, col2 = st.columns(2)
with col1:
    gruposU.insert(0,"Todos")
    optionGrupo = st.selectbox('Grupo', (gruposU))
with col2:       
    optionMomento = st.selectbox('Momento', (momentosU))


notas_conocimiento = None
if optionGrupo != 'Todos':
    notas_conocimiento = df[(df['GRUPO']==optionGrupo)&(df['MOMENTO']==optionMomento)]
else :
    notas_conocimiento = df[df['MOMENTO']==optionMomento]

    # Create the bar chart
if notas_conocimiento is not None:    

    NOTAS=notas_conocimiento['NOMBRE']
   

    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=NOTAS, y=notas_conocimiento['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=NOTAS, y=notas_conocimiento['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=NOTAS, y=notas_conocimiento['PRODUCTO'])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)