import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

print('First we will be seeing the prompt in English to compare:')

prompt="""
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: What is a compiler?
AI:"""

print("PROMPT", prompt)

response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["AI:"]
)

print(response['choices'][0]['text'])


print('==============================================')
print('Agora vamos tentar o mesmo prompt em português:')
prompt="""
A seguinte é uma conversa com uma assistente de IA. A assistente é prestativa, criativa, inteligente, e muito amigável.

Humano: O que é um compilador?
IA:"""

print("PROMPT", prompt)

response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["IA:"]
)

print(response['choices'][0]['text'])

print('==============================================')
print('Agora vamos tentar uma tarefa de classificação:')

query="Não gostei muito não, tentaria outro produto."
print(query)

response = openai.Classification.create(
        search_model="ada",
        model="curie",
        examples=[
            ["Eu gostei muito desse produto, compraria de novo.", "Positivo"],
            ["Esse produto é verde.", "Neutro"],
            ["Veio quebrado, eu não compraria de novo", "Negativo"],
        ],
        query=query,
        labels=["Positivo", "Neutro", "Negativo"],
)

print("LABEL", response["label"])

print('==============================================')
print('Agora vamos tentar uma resposta para uma pergunta:')

question="O que significa a cor rosa?"
documents=["Rosa signifca vai.", "Vermelho é para parar.", "Laranja é para ter cuidado."]
print("QUESTION", question)
print("DOCUMENTS", documents)

response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=question,
        documents=documents,
        examples_context="A pandemia de Covid-19 começou em 2019.",
        examples=[["Quando que começou a pandemia?", "No ano 2019."]],
        max_tokens=5,
        stop=["\n", "<|endoftext|>"],
)

print("ANSWERS", response["answers"])

print('==============================================')
print('Agora vamos tentar uma pergunta com o context enviado:')

question="Quando começou a pandemia?"
context="A pandemia de Covid-19 começou em 2019."
print("QUESTION", question)
print("CONTEXT", context)

response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=question,
        documents=documents,
        examples_context=context,
        examples=[["Quando que começou a pandemia?", "No ano 2019."]],
        max_tokens=5,
        stop=["\n", "<|endoftext|>"],
)

print("ANSWERS", response["answers"])


print('==============================================')
print('Now let\'s search:')

search="Campina Grande"
documents=["Africa", "America do Sul", "Asia"]
print("SEARCH", search)
print("DOCUMENTS", documents)

response = openai.Engine("davinci").search(
        documents=["Africa", "South America", "Asia"],
        query=search
)

print(response)

print("Campina Grande está na America do Sul, de acordo com o score.")
