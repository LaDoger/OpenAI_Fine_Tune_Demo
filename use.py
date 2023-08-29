import openai
import tune # Get info from tune.py file


### CHANGE THIS: Put your model id here
fine_tuned_model = "ft:gpt-3.5-turbo-0613:****::****"

# Let user ask question
print('Please ask your question below.\n')
question = input('Question: ')
print(f'Answer: ', end='')

# Get response
openai.api_key = tune.OPENAI_API_KEY
completion = openai.ChatCompletion.create(
    model=fine_tuned_model,
    messages=[
        {"role": "system", "content": tune.system_prompt},
        {"role": "user", "content": question}
    ],
    stream = True
)

# Print response with streaming
for chunk in completion:
    try:
        print(chunk.choices[0].delta['content'], end='')
    except:
        print('')
