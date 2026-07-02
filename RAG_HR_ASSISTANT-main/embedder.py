from google import genai
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EMBEDDING_MODEL = "gemini-embedding-001"


def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """Embeds chunks using Gemini."""
    embeddings = []

    for chunk in chunks:
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=chunk
        )

        embeddings.append(response.embeddings[0].values)

    return embeddings


def embed_user_query(query: str) -> List[float]:
    """Embeds a user query using Gemini."""
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query
    )

    return response.embeddings[0].values