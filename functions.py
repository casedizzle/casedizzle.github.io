import openai
import os


def generate_response(author, text):
    prompt = (f"Take this text: {text}. Rewrite this text using a very heavy style of this author: {author}. Make sure you continue to write in the style of {author} for the whole text.")
    response = openai.Completion.create(engine = 'text-davinci-003',
                                        prompt=prompt,
                                        max_tokens = 1000,
                                        temperature =.7,
                                        top_p = 0.8)
    
    return response['choices'][0]['text']
    