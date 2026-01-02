# 연습용 크롤링 사이트인 Quotes to Scrape에서 한 페이지에 포함된 명언과 저자 정보를 수집하는 기본 실습입니다.
# 본 실습의 목적은 실제 서비스 개발이 아니라, HTML 구조를 이해하고 선택자를 통해 원하는 정보를 정확히 추출하는 과정에 익숙해지는 데 있습니다.

import requests
from bs4 import BeautifulSoup
import os

url = "https://news.naver.com/section/104"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser") # xml 경우는 xml.parser

# div.sa_item_flex
quotes = soup.select("div.sa_thumb_inner")

# 최대 5개의 이미지 저장
for i, quote in enumerate(quotes[:5], start=1):
    # img 태그 찾기 (썸네일 이미지)
    img_tag = quote.find("img")
    if not img_tag:
        continue

    img_url = img_tag.get("src") or img_tag.get("data-src")
    if not img_url:
        continue

    # 이미지 요청
    img_data = requests.get(img_url).content

    # 파일로 저장
    save_path ="C:/workspace/part2/book1/ch03/news_images"
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join(save_path, f"news_image_{i}.jpg")
    with open(file_path, "wb") as f:
        f.write(img_data)
