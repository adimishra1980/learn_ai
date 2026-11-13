import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, ConfigDict

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"

# now here we will structure is so that it gives us structed output
class Ticket(BaseModel):
    model_config = ConfigDict(extra="forbid")


    name: str
    email: str
    issue: str
    phone: str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_schema",
    "json_schema": {
        "name": "ticket",
        "schema": schema,
        "strict": True
    }
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give me a json output: 
{schema}
"""

message_system={
    "role": "system",
    "content": system_prompt
}

text="Hello my name is Aditya, I have an iphone which is not working at all, My address is delhi, My email is abc@gmail.com, My contact number is 7890"

prompt=f"""
This is a customer ticket. Please extract the personal information from this, {text}
"""

message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]
response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)

# isko padhte kaise hai
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket.phone)
