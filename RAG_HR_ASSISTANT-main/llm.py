from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.3-70b-versatile"


def query_llm_with_context(query: str, context: str):

    prompt = f"""
You are an AI HR Assistant.

Follow these rules STRICTLY:

1. If the user greets you (Hi, Hello, Hey, Good morning, etc.), respond politely.

2. If the user asks an HR-related question, answer ONLY using the provided context.

3. If the answer is not found in the context, reply exactly:
"I couldn't find that information in the provided HR documents."

4. If the question is not related to HR, reply exactly:
"I'm an AI HR Assistant and can only answer HR-related questions based on the uploaded company documents."

Context:
{context}

User Question:
{query}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an AI HR Assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content