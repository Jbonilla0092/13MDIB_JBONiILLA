import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Se realiza la lectura de los datos
df = pd.read_csv("../../../data/final/datos_finales.csv", sep=";")

# Título del dashboard
st.write("# 13MBID - Visualización de datos")
st.write("## Panel de visualización generado sobre los datos de créditos y tarjetas emitidas a clientes de la entidad")
st.write("#### Estudiante: Juan Manuel Bonilla Lozano")
st.write("----")

# Gráficos
st.write("### Caracterización de los créditos otorgados")

# Se tienen que agregar las definiciones de gráficos desde la libreta
creditos_x_objetivo = px.histogram(df, x='objetivo_credito', 
                                   title='Conteo de créditos por objetivo')
creditos_x_objetivo.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')

# Se realiza la "impresión" del gráfico en el dashboard
st.plotly_chart(creditos_x_objetivo)


# Histograma de los importes de créditos otorgados
histograma_importes = px.histogram(df, x='importe_solicitado', nbins=10, title='Importes solicitados en créditos')
histograma_importes.update_layout(xaxis_title='Importe solicitado', yaxis_title='Cantidad')

st.plotly_chart(histograma_importes)

#diagrama de cajas y alambres
option1 = st.selectbox(
    'Qué tipo de crédito desea filtrar?',
     df['objetivo_credito'].unique())

df_filtrado2 = df[df['objetivo_credito'] == option1]


st.write(f"Tipo de crédito seleccionado: {option1}")

paleta_colores = px.colors.qualitative.Set1
fig = px.box(df_filtrado2, x='gastos_ult_12m', y='importe_solicitado', 
             color = 'gastos_ult_12m',
             color_discrete_sequence=paleta_colores,
             title='Distribución del importe solicidado acorde a los gastos realizados',
             labels={'categoria_1': 'Categoría', 'importe_solicitado': 'Importe Solicitado'})

fig.update_layout(xaxis_title='grupo gastos 12m', yaxis_title='Importe Solicitado')

st.plotly_chart(fig)



# Filtros

option = st.selectbox(
    '¿Qué tipo de crédito desea filtrar?',
     df['objetivo_credito'].unique())

df_filtrado = df[df['objetivo_credito'] == option]

st.write(f"Tipo de crédito seleccionado: {option}")

if st.checkbox('Mostrar créditos finalizados?', value=True):

    # Conteo de ocurrencias por estado
    estado_credito_counts = df_filtrado['estado_credito_N'].value_counts()

    # Gráfico de torta de estos valores
    fig = go.Figure(data=[go.Pie(labels=estado_credito_counts.index, values=estado_credito_counts)])
    fig.update_layout(title_text='Distribución de créditos por estado registrado')
else:
    df_filtrado = df_filtrado[df_filtrado['estado_credito_N'] == 'P']
    # Conteo de ocurrencias por caso
    falta_pago_counts = df_filtrado['falta_pago'].value_counts()

    # Create a Pie chart
    fig = go.Figure(data=[go.Pie(labels=falta_pago_counts.index, values=falta_pago_counts)])
    fig.update_layout(title_text='Distribución de créditos en función de registro de mora')

st.write(f"Cantidad de créditos con estas condiciones: {df_filtrado.shape[0]}")
st.plotly_chart(fig)


#crearé otro gráfico que relacione la falta de pago con el nivel educativo.

option3 = st.selectbox(
    'Elige el nivel educativo',
     df['nivel_educativo'].unique())

df_filtrado3 = df[df['nivel_educativo'] == option3]

st.write(f"Nivel educativo seleccionado: {option3}")  

pago_x_educacion = px.histogram(df_filtrado3, x='ingresos', 
                                   title='Conteo de créditos por ingresos')
pago_x_educacion.update_layout(xaxis_title='Categoría de ingresos', yaxis_title='Cantidad')

st.plotly_chart(pago_x_educacion)