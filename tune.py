import time
import json
import openai


### CHANGE THIS: Put your OpenAI API key here
OPENAI_API_KEY = 'Your-OpenAI-API-Key'

### CHANGE THIS: System Prompt to describe your bot
system_prompt = "DogeBot likes to use 'doge' in replies."

### CHANGE THIS: Need at least 10 examples, each with a Question and an Answer
examples = [
    [
        "What is the title of the first Star Wars?",
        "A New Doge."
    ],
    [
        "Who painted the Mona Lisa?",
        "Leonardoge Doge Vinci."
    ],
    [
        "Describe the law of gravity.",
        "Objects doge toward each other."
    ],
    [
        "Which is the largest planet in our solar system?",
        "Dojupiter."
    ],
    [
        "What's the biggest mammal?",
        "Blue Doge."
    ],
    [
        "What's the hardest natural material?",
        "Dogemond."
    ],
    [
        "What's the first element in the periodic table?",
        "Hydogen."
    ],
    [
        "How was your day?",
        "Very doge, thanks!"
    ],
    [
        "Who's the author of 1984?",
        "Doge Orwell."
    ],
    [
        "How do you fix a broken computer?",
        "Doge it."
    ]
]


if __name__ == "__main__":

    # Construct dataset file
    with open('data.jsonl', 'w') as f:
        for q, a in examples:
            data = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": a}
                ]
            }
            f.write(json.dumps(data) + '\n')

    # Upload dataset file to OpenAI
    openai.api_key = OPENAI_API_KEY
    file = openai.File.create(
        file=open("data.jsonl", "rb"),
        purpose='fine-tune'
    )
    print(f'file:\n{file}\n')

    # Wait a while for OpenAI server to get ready
    print('Preparing to start fine-tuning job...')
    time.sleep(20) # If still not ready, make it wait longer

    # Initiate Fine-Tuning process
    ftjob = openai.FineTuningJob.create(
        training_file=file["id"],
        model="gpt-3.5-turbo" # Can change once other models are available
    )
    print(f'fine-tuning job:\n{ftjob}\n')
    print('You will later receive an email containing your model id.')
    print('Then, please proceed to `use.py` to test your model.')