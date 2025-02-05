import x
from anthropic import Anthropic


def request(
    model,
    prompt,
):

    anthropic = Anthropic(
        api_key=x.env.get('ANTHROPIC_API_KEY'),
    )

    message = anthropic.messages.create(
        model=model,
        max_tokens=2048,
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': prompt
                    },
                ]
            }
        ]
    )

    return message.content[0].text


def sonnet(
    prompt,
):

    request(
        'claude-3-5-sonnet-20241022',
        prompt,
    )


def haiku(
    prompt,
):

    request(
        'claude-3-5-haiku-20241022',
        prompt,
    )
