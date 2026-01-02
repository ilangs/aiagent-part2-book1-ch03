# app_matplotlib.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("이슈 데이터 시각화 (Matplotlib)")

df = pd.DataFrame({
    "hour": [9, 12, 15, 18, 21],
    "views": [120, 340, 560, 430, 290]
})

st.dataframe(df)

fig, ax = plt.subplots()
ax.plot(df["hour"], df["views"])
ax.set_title("시간대별 기사 조회 수")
ax.set_xlabel("시간")
ax.set_ylabel("조회 수")

st.pyplot(fig)