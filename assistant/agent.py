"""Email assistant agent: understand -> plan -> draft -> review -> revise."""

from . import prompts
from .config import MODEL
from .llm_client import client

def understand_email(email):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompts.UNDERSTAND_SYSTEM
            },
            {
                "role": "user",
                "content": email
            }
        ]
    )
    return response.choices[0].message.content
