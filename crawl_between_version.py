import requests
from packaging import version  # 버전 비교를 위해 사용

# GitHub API Endpoint 설정
repo = "comfyanonymous/ComfyUI"
url = f"https://api.github.com/repos/{repo}/releases"

# API 요청 보내기 (최대 100개의 릴리스까지 가져올 수 있음)
params = {'per_page': 100}
response = requests.get(url, params=params)

# 버전 구간 지정
start_version = version.parse("v0.2.0")
end_version = version.parse("v0.3.1")

# 응답 처리
if response.status_code == 200:
    releases = response.json()
    
    # 버전 구간에 맞는 릴리스만 필터링하여 출력
    for release in releases:
        release_version = version.parse(release['tag_name'])
        if start_version <= release_version <= end_version:
            print(f"Release Name: {release['name']}")
            print(f"Tag Name: {release['tag_name']}")
            print(f"Published at: {release['published_at']}")
            print(f"Body: {release['body']}")
            print("-" * 40)
else:
    print(f"Failed to fetch releases: {response.status_code}")
