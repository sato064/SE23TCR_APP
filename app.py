import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import japanize_matplotlib

st.set_page_config(
    page_title="Inspection Dashboard",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': """
        # Inspection Dashboard
        インスペクション結果の可視化を行うアプリケーションです．
        """
    })



st.title("トップページ") # タイトル
st.text("左メニューから自分のインスペクション履歴が見れます") # 説明文