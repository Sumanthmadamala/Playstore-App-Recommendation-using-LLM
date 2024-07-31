import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path:str)->pd.DataFrame:
    df = pd.read_csv(path)

    return df
