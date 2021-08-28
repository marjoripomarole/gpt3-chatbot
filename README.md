# gpt-3 portuguese chatbot example

This repo has a few examples of a portuguese chatbot written in python
using OpenAI's GPT3 API.

You will be needing to get [on the waitlist](https://openai.com/join/) to get the API key.

## Install

First install `direnv`, and create a .envrc file with:
```
export OPENAI_API_KEY=...
```

Install package requirements for the api:
```
virtualenv -p python venv
pip install --upgrade pip
pip install -r requirements.txt
```

And run the chatbot
```
python chatbot.py
```

Examplo da resposta do programa no arquivo `response`.
