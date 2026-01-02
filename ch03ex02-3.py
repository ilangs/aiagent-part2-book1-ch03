import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 기사 반응 데이터 예시
df = pd.DataFrame({
    "views": [120, 340, 560, 430, 290],
    "comments": [5, 18, 42, 30, 12]
})

# 산점도 작성
plt.scatter(df["views"], df["comments"])
# plt.bar(df["views"], df["comments"])    # 막대 그래프
# plt.plot(df["views"], df["comments"])   # 선 그래프

# 그래프 정보 설정
plt.title("조회 수와 댓글 수의 관계")
plt.xlabel("조회 수")
plt.ylabel("댓글 수")

# 그래프 출력
plt.show()