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

def plan_response(email, understanding, context):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompts.PLAN_SYSTEM
            },
            {
                "role": "user",
                "content": prompts.PLAN_USER.format(
                    email=email,
                    understanding=understanding,
                    context=context
                )
            }
        ]
    )

    return response.choices[0].message.content



def draft_reply(email, plan, context):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompts.DRAFT_SYSTEM
            },
            {
                "role": "user",
                "content": prompts.DRAFT_USER.format(
                    email=email,
                    plan=plan,
                    context=context
                )
            }
        ]
    )

    return response.choices[0].message.content

