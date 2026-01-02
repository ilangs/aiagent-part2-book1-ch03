# API 데이터 자동 수집 파이프라인

# ----- API 요청 및 응답 확인(1단계) -----

import requests

url = "https://hn.algolia.com/api/v1/search"
params = {
    "query": "AI",
    "tags": "story"
}

response = requests.get(url, params=params)

# print(response.status_code)
# print(response.json().keys())

# ------ JSON 데이터에서 필요한 항목 추출(2단계) ------

data = response.json()
articles = data["hits"]

for article in articles:
    title = article.get("title")
    created_at = article.get("created_at")
    # print(title, created_at)

# ------ 구조화된 데이터 리스트 생성(3단계) ------
# 모든 데이터를 동일한 키 구조로 맞추는 것

structured_data = []

for article in articles:
    structured_data.append({
        "title": article.get("title"),
        "author": article.get("author"),
        "date": article.get("created_at"),
        "url": article.get("url")
    })

# ------ pandas 데이터프레임으로 변환(4단계) ------

import pandas as pd

df = pd.DataFrame(structured_data)
# print(df.head())

# ------ 수집 시점 정보 추가하기(5단계) ------

from datetime import datetime

df["collected_at"] = datetime.now()
# print(df.head())

# ----- CSV 파일로 저장하기(6단계) -----

# # 일일 데이터로 덮어쓰는 방식
# df.to_csv("news_daily.csv", index=False, encoding="utf-8-sig")
# print("데이터 수집 및 저장 완료")

# 수집 날짜를 파일명에 포함하여 누적 저장하는 방식
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f"news_{today}.csv", index=False, encoding="utf-8-sig")
print("데이터 수집 및 저장 완료")

# ------ 함수로 정리하여 재사용 구조 만들기(7단계) ------

# 지금까지의 흐름을 하나의 함수로 정리

def fetch_and_save_news(query: str = "AI") -> None:
    import requests
    import pandas as pd
    from datetime import datetime

    url = "https://hn.algolia.com/api/v1/search"
    params = {
        "query": query,
        "tags": "story"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    articles = data["hits"]

    rows = []
    collected_at = datetime.now()

    for article in articles:
        rows.append({
            "title": article.get("title"),
            "author": article.get("author"),
            "date": article.get("created_at"),
            "url": article.get("url"),
            "collected_at": collected_at
        })

    df = pd.DataFrame(rows)

    today = collected_at.strftime("%Y-%m-%d")
    df.to_csv(f"news_{today}.csv", index=False, encoding="utf-8-sig")

