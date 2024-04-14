import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import matplotlib.image as mpimg

st.set_page_config(layout='wide',page_title='Fashion Recommendation')
df=pd.read_csv('df.csv')
st.title('fashion recommendation system')

gender=st.selectbox('select gender',df['gender'].value_counts().index.to_list())
df =df[df['gender'] == gender]

if gender:
        season = st.selectbox('select season', df['season'].value_counts().index.to_list())
        df = df[df['season'] == season]
        if season:
            usage = st.selectbox('select occation', df['usage'].value_counts().index.to_list())
            df = df[df['usage'] == usage]
            if usage:
                subCategory = st.selectbox('select subCategory', df['subCategory'].value_counts().index.to_list())
                df = df[df['subCategory'] == subCategory]
                if subCategory:
                    articleType = st.selectbox('select articleType', df['articleType'].value_counts().index.to_list())
                    df = df[df['articleType'] == articleType]
                    col1,col2,col3,col4=st.columns(4)
                    with col1:
                        df1=df.sample(replace=False)
                        image_url = df1['link'].values[0]
                        response = requests.get(image_url)
                        img = Image.open(BytesIO(response.content))
                        st.image(img, caption='Image', use_column_width=True)
                        st.write(df1['productDisplayName'].values[0])
                        with col2:
                            df1=df.sample(replace=False)
                            image_url = df1['link'].values[0]
                            response = requests.get(image_url)
                            img = Image.open(BytesIO(response.content))
                            st.image(img, caption='Image', use_column_width=True)
                            st.write(df1['productDisplayName'].values[0])
                            with col3:
                                df1=df.sample(replace=False)
                                image_url = df1['link'].values[0]
                                response = requests.get(image_url)
                                img = Image.open(BytesIO(response.content))
                                st.image(img, caption='Image', use_column_width=True)
                                st.write(df1['productDisplayName'].values[0])
                                with col4:
                                    df1=df.sample(replace=False)
                                    image_url = df1['link'].values[0]
                                    response = requests.get(image_url)
                                    img = Image.open(BytesIO(response.content))
                                    st.image(img, caption='Image', use_column_width=True)
                                    st.write(df1['productDisplayName'].values[0])