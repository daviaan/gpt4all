#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpt4all import GPT4All

model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", device='cpu')
output = model.generate("The capital of Italy is ", max_tokens=3)
print("The capital is : ",output)
