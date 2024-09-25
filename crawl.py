import requests
import os
from datetime import datetime

# GitHub API Endpoint 설정
repo = "comfyanonymous/ComfyUI"
url = f"https://api.github.com/repos/{repo}/releases"

# API 요청 보내기
response = requests.get(url)

# 응답 처리
if response.status_code == 200:
    releases = response.json()
    
    # 각 릴리스 정보를 파일로 저장
    for release in releases:
        # 파일 이름 생성 (릴리스 날짜와 태그 이름 사용)
        release_date = datetime.strptime(release['published_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y%m%d")
        filename = f"{release_date}_{release['tag_name']}.txt"
        
        # 파일에 릴리스 정보 작성
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Release Name: {release['name']}\n")
            f.write(f"Tag Name: {release['tag_name']}\n")
            f.write(f"Published at: {release['published_at']}\n")
            f.write(f"Body:\n{release['body']}\n")
        
        print(f"릴리스 정보가 {filename}에 저장되었습니다.")
else:
    print(f"릴리스 정보를 가져오는 데 실패했습니다: {response.status_code}")
