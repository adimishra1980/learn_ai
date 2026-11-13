import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
# prompt="I love you baby!"
prompt="Suggest a name for my mock test platform where students can come and give tests online for government exams, and name would be easy to remember and eye catching."

message_system={
    "role": "system",
    # "content": "You are my loving girlfriend"
    # "content": "You are my strict office colleague who is also my manager"
    "content": "You are a designer who suggests name for my mock test platform. name should be one word."
}
message={
    "role": role,
    "content": prompt
}
messages=[message_system, message]

# by default temperature is 0 range is [0, 1, 2]
response=client.chat.completions.create(model=model, messages=messages, temperature=1)
answer=response.choices[0].message.content
print(answer)

