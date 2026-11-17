import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"

def llm_ans(prompt: str):
    message={
        "role": "user",
        "content": prompt
    }
    messages=[message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

bad_prompt="""
This is a user complaint:
My laptop is not working
Classify this
"""

good_prompt="""
#ROLE: You are a suport assistant at a mobile/laptop company
#TASK: You have to classify the issue in a category
#CONSTRAINTS: You have to classify the issue in one of the following categories: Hardware, Software, Network, return, Other
#OUTPUT FORMAT: Your answer should be in one word only, the one word should be one of the categories mentioned above
#EXAMPLE: For instance, if a user complain says he wants a refund then the category should be return
#FALLBACK: If the issue is unrelated to any of the categories mentioned in the constraints, then classify it as Other
This is a user complaint:
My laptop is not working
Classify this
"""

print(llm_ans(good_prompt))