import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
res = client.chat.completions.create(
    #model="gemini-3.6-flash",   # 
    model="gemini-3.5-flash-lite",
    messages=[{"role": "user", "content": "Hello"}],
)
print(res.choices[0].message.content)
