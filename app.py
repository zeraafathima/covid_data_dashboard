import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
st.title('COVID-19 Data:INDIA')
data=pd.read_csv('covid_data.csv')
print(data.columns)
with st.expander('show data'):
    st.write(data)
st.markdown('----')

col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric('Total Cases',data['Total Cases'].sum())
with col2:
     st.metric('Recovered',data['Discharged'].sum())
with col3:
    st.metric('Death',data['Deaths'].sum())
with col4:
    st.metric('Active',data['Active'].sum())
st.markdown('----')


st.header('Total Cases')
col1,col2=st.columns(2)
data_frame=data[['State/UTs','Total Cases']]
with col1:
    st.header('Highest')
    sorted_df_high=data_frame.sort_values(by='Total Cases', ascending=False)
    st.write(sorted_df_high.head())
with col2:
    st.header('Least')
    sorted_df_low=data_frame.sort_values(by='Total Cases', ascending=True)
    st.write(sorted_df_low.head())

st.header('Recovered')

data_frame=data[['State/UTs','Discharge Ratio']]
col3,col4=st.columns(2)

with col3:
    st.header('Highest')
    sorted_df_high=data_frame.sort_values(by='Discharge Ratio', ascending=False)
    st.write(sorted_df_high.head())
with col4:
    st.header('Least')
    sorted_df_low=data_frame.sort_values(by='Discharge Ratio', ascending=True)
    st.write(sorted_df_low.head())

st.header('Death')
data_frame=data[['State/UTs','Death Ratio']]
col5,col6=st.columns(2)
with col5:
    st.header('Highest')
    sorted_df_high=data_frame.sort_values(by='Death Ratio', ascending=False)
    st.write(sorted_df_high.head())
with col6:
    st.header('Least')
    sorted_df_low=data_frame.sort_values(by='Death Ratio', ascending=True)
    st.write(sorted_df_low.head())
 
st.header('Active')
data_frame=data[['State/UTs','Active Ratio']]
col7,col8=st.columns(2)
with col7:
    st.header('Highest')
    sorted_df_high=data_frame.sort_values(by='Active Ratio', ascending=False)
    st.write(sorted_df_high.head())
with col8:
    st.header('Least')
    sorted_df_low=data_frame.sort_values(by='Active Ratio', ascending=True)
    st.write(sorted_df_low.head())




col5,col6=st.columns(2)
with col5:
    st.header(' Death rate Chart')
    fig=px.bar(data_frame=data,x='Deaths',y='State/UTs')
    st.plotly_chart(fig)
with col6:
    st.header('Recovered Patients Chart')
    fig=px.bar(data_frame=data,x='Discharged',y='State/UTs')
    st.plotly_chart(fig)

col7,col8=st.columns(2)
with col7:
    st.header(' Active Rate Chart')
    fig=px.bar(data_frame=data,x='Active',y='State/UTs')
    st.plotly_chart(fig)
with col8:
    st.header('Total Cases Chart')
    fig=px.bar(data_frame=data,x='Total Cases',y='State/UTs')
    st.plotly_chart(fig)

fig1=px.pie(data_frame=data,values='Total Cases',names='Zone',title='Cases by Zone')
st.plotly_chart(fig1)