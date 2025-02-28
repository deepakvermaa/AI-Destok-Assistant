from openai import OpenAI
client = OpenAI(
    api_key="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",
    # engine_id="text-davinci-003",
    # language="en",
    # temperature=0.5,
    # max_tokens=100
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)