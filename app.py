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

#options=st.selectbox('Total Cases',data['Total Cases'].unique())
#df=data[data['Total Cases']==options]
#st.write(df)

data_frame=pd.DataFrame(data['Total Cases'])
st.write(data_frame)
data_frame=pd.DataFrame(data['Discharged'])
st.write(data_frame)
data_frame=pd.DataFrame(data['Active'])
st.write(data_frame)
data_frame=pd.DataFrame(data['Deaths'])
st.write(data_frame)


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

fig1=px.pie(data_frame=data,values='Total Cases')
st.plotly_chart(fig1)