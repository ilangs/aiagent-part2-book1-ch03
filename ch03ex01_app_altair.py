# app_altair.py
import streamlit as st
import pandas as pd
import altair as alt

st.title("이슈 데이터 시각화 (Altair)")

df = pd.DataFrame({
    "hour": [9, 12, 15, 18, 21],
    "views": [120, 340, 560, 430, 290]
})

st.dataframe(df)

chart = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(
        x=alt.X("hour:Q", title="시간"),
        y=alt.Y("views:Q", title="조회 수"),
        tooltip=["hour", "views"]
    )
    .properties(title="시간대별 기사 조회 수")
)

st.altair_chart(chart, use_container_width=True)
