import os
import urllib.request
import json
from dotenv import load_dotenv # 이 줄 추가

load_dotenv() # 이 줄 추가

url = "https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01",
}
body = json.dumps({
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")

# 서버가 에러(400)를 뱉으면 urllib은 예외를 발생시키므로 try-except로 잡아야 합니다.
try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(result["content"][0]["text"])
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode())
