import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(layout='wide', page_title='Fashion Recommendation')
df = pd.read_csv('df2.csv')
st.title('Fashion Recommendation System')
st.sidebar.title('Select Your Outfits')
gender = st.sidebar.selectbox('Select Gender', df['gender'].value_counts().index.to_list())
df = df[df['gender'] == gender]

if gender:
    season = st.sidebar.selectbox('Select Season', df['season'].value_counts().index.to_list())
    df = df[df['season'] == season]
    if season:
        usage = st.sidebar.selectbox('Select Occasion', df['usage'].value_counts().index.to_list())
        df = df[df['usage'] == usage]
        if usage:
            subCategory = st.sidebar.selectbox('Select SubCategory', df['subCategory'].value_counts().index.to_list())
            df = df[df['subCategory'] == subCategory]
            if subCategory:
                articleType = st.sidebar.selectbox('Select ArticleType',
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
                                btn = st.button('Next')
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