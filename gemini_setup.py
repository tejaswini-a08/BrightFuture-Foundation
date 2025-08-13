
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCXHqnLr4dpoCIuzfMMo40x5xU3oIDKR1M")

model = genai.GenerativeModel("gemini-1.5-flash")
response= model.generate_content("Hello Gemini!!")
print(response.text)

