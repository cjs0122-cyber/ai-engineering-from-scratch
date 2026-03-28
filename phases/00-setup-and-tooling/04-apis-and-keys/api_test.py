import os
from dotenv import load_dotenv
load_dotenv()  # 현재 폴더의 .env 파일을 찾아 환경 변수로 등록합니다.

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)

print(response.content[0].text)
