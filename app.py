import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import matplotlib.image

st.set_page_config(layout='wide', page_title='Fashion Recommendation')
df = pd.read_csv('df2.csv')
st.title('fashion recommendation system')
st.sidebar.title('select your outfits')
gender = st.sidebar.selectbox('select gender', df['gender'].value_counts().index.to_list())
df = df[df['gender'] == gender]

if gender:
    season = st.sidebar.selectbox('select season', df['season'].value_counts().index.to_list())
    df = df[df['season'] == season]
    if season:
        usage = st.sidebar.selectbox('select occasion', df['usage'].value_counts().index.to_list())
        df = df[df['usage'] == usage]
        if usage:
            subCategory = st.sidebar.selectbox('select subCategory', df['subCategory'].value_counts().index.to_list())
            df = df[df['subCategory'] == subCategory]
            if subCategory:
                articleType = st.sidebar.selectbox('select articleType',
                                                   df['articleType'].value_counts().index.to_list())
                df = df[df['articleType'] == articleType]

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    df1 = df.sample(replace=False)
                    image_url = df1['link'].values[0]
                    response = requests.get(image_url)
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption='Image', use_column_width=True)
                    st.write(df1['productDisplayName'].values[0])
                    st.write('click here for virtual try on:',df1['AR LINK'].values[0])
                    st.write('click here to purchase:', df1['Purchases link'].values[0])
                    with col2:
                        df1 = df.sample(replace=False)
                        image_url = df1['link'].values[0]
                        response = requests.get(image_url)
                        img = Image.open(BytesIO(response.content))
                        st.image(img, caption='Image', use_column_width=True)
                        st.write(df1['productDisplayName'].values[0])
                        st.write('click here for virtual try on:',df1['AR LINK'].values[0])
                        st.write('click here to purchase:', df1['Purchases link'].values[0])
                        with col3:
                            df1 = df.sample(replace=False)
                            image_url = df1['link'].values[0]
                            response = requests.get(image_url)
                            img = Image.open(BytesIO(response.content))
                            st.image(img, caption='Image', use_column_width=True)
                            st.write(df1['productDisplayName'].values[0])
                            st.write('click here for virtual try on:',df1['AR LINK'].values[0])
                            st.write('click here to purchase:', df1['Purchases link'].values[0])
                            with col4:
                                df1 = df.sample(replace=False)
                                image_url = df1['link'].values[0]
                                response = requests.get(image_url)
                                img = Image.open(BytesIO(response.content))
                                st.image(img, caption='Image', use_column_width=True)
                                st.write(df1['productDisplayName'].values[0])
                                st.write('click here for virtual try on:',df1['AR LINK'].values[0])
                                st.write('click here to purchase:', df1['Purchases link'].values[0])
                                btn = st.button('next')
                                if btn:
                                    col1, col2, col3, col4 = st.columns(4)
                                    with col1:
                                        df1 = df.sample(replace=False)
                                        image_url = df1['link'].values[0]
                                        response = requests.get(image_url)
                                        img = Image.open(BytesIO(response.content))
                                        st.image(img, caption='Image', use_column_width=True)
                                        st.write(df1['productDisplayName'].values[0])
                                        st.write('click here for virtual try on:',df1['AR LINK'].values[0])
                                        st.write('click here to purchase:', df1['Purchases link'].values[0])
                                        with col2:
                                            df1 = df.sample(replace=False)
                                            image_url = df1['link'].values[0]
                                            response = requests.get(image_url)
                                            img = Image.open(BytesIO(response.content))
                                            st.image(img, caption='Image', use_column_width=True)
                                            st.write(df1['productDisplayName'].values[0])
                                            st.write('click here for virtual try on:', df1['AR LINK'].values[0])
                                            st.write('click here to purchase:', df1['Purchases link'].values[0])
                                            with col3:
                                                df1 = df.sample(replace=False)
                                                image_url = df1['link'].values[0]
                                                response = requests.get(image_url)
                                                img = Image.open(BytesIO(response.content))
                                                st.image(img, caption='Image', use_column_width=True)
                                                st.write(df1['productDisplayName'].values[0])
                                                st.write('click here for virtual try on:',df1['AR LINK'].values[0])
                                                st.write('click here to purchase:', df1['Purchases link'].values[0])
                                                with col4:
                                                    df1 = df.sample(replace=False)
                                                    image_url = df1['link'].values[0]
                                                    response = requests.get(image_url)
                                                    img = Image.open(BytesIO(response.content))
                                                    st.image(img, caption='Image', use_column_width=True)
                                                    st.write(df1['productDisplayName'].values[0])
                                                    st.write('click here for virtual try on:', df1['AR LINK'].values[0])
                                                    st.write('click here to purchase:', df1['Purchases link'].values[0])