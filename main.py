#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpt4all import GPT4All

# model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", device='cpu', allow_download=True)
# output = model.generate("The capital of Mongolia is ", max_tokens=10)
# print("The capital is : ",output)

model = GPT4All('Phi-3-mini-4k-instruct.Q4_0.gguf', device='cpu', allow_download=True)
tokens = []
with model.chat_session():
    for token in model.generate("What is the capital of Mongolia?", streaming=True):
        tokens.append(token)
    print(tokens)
    # output to console:
    for token in model.generate("What is the highest mountain in Africa?", streaming=True):
        print(token, end='', flush=True)
    print()
