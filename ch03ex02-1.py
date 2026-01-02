import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# API 응답 데이터를 정리한 DataFrame 예시
df = pd.DataFrame({
    "hour": [9, 12, 15, 18, 21],
    "views": [120, 340, 560, 430, 290]
})

# 그래프 작성
plt.plot(df["hour"], df["views"])         # 선 그래프
# plt.bar(df["hour"], df["views"])        # 막대 그래프
# plt.scatter(df["hour"], df["views"])    # 산점도

# 그래프 정보 설정
plt.title("시간대별 기사 조회수")
plt.xlabel("시간")
plt.ylabel("조회수")

# 그래프 출력
plt.show()