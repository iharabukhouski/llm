import x
from openai import OpenAI


def request(
    model,
    prompt,
):
    client = OpenAI(
        api_key=x.env.get('OPENAI_API_KEY'),
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def o3_mini(
    prompt,
):
    return request(
        'o3_mini',
        prompt,
    )
