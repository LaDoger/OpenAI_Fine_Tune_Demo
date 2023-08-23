import openai
import tune # Get info from tune.py file


### CHANGE THIS: Put your model id here ###
fine_tuned_model = "ft:gpt-3.5-turbo-0613:********"

### CHANGE THIS: Ask your question ###
question = "Write a poem!"

# Get response
openai.api_key = tune.OPENAI_API_KEY
completion = openai.ChatCompletion.create(
    model=fine_tuned_model,
    messages=[
        {"role": "system", "content": tune.system_prompt},
        {"role": "user", "content": question}
    ]
)
print(f'Q: {question}')
print(f'A: {completion.choices[0].message.content}')