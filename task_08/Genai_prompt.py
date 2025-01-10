import openai 
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = open_api_key

def query_openai(prompt, temperature=0.7, max_tokens=50):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who provides concise one-line summaries."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()
# Text to be summarized
text_to_summarize = """
Computers are electronic devices that process data and perform various tasks based on instructions from software. 
They are an integral part of modern society, used in fields ranging from education and healthcare to business 
and entertainment. Computers consist of hardware, such as processors and memory, and software, which includes 
operating systems and applications. Over the years, advancements in technology have made computers faster,
 more efficient, and accessible. They enable users to communicate, solve problems, and automate repetitive 
 tasks. Despite their numerous advantages, computers also pose challenges, such as cybersecurity threats and 
 digital addiction.
"""

# Generate prompt
summarization_prompt = f"Summarize the following text: {text_to_summarize}"

# Get summarized text
summary = query_openai(summarization_prompt)
#print("Summarized Text:", summary)

# Question and Answering
context = "Computers are vital in modern society as they enable communication, innovation, and problem-solving across various industries."
question = "Why are computers important in modern society?"

# Create a structured Q&A prompt
qa_prompt = f"Context: {context}\nQuestion: {question}\nAnswer in one or two sentences:"

# Get the answer
answer = query_openai(qa_prompt)
#print("Q&A Answer:", answer)

# Prompt library
prompt_library = {
    "greeting": "Respond warmly to a user who greets the bot.",
    "product_info": "Provide detailed information about the product: {product_name}.",
    "troubleshooting": "Help the user resolve this issue step-by-step: {issue_description}.",
    "faq_general": "Answer this FAQ question clearly: {question}.",
    "escalation": "Explain when to escalate this issue: {problem_description}."
}

def generate_response(user_input, category):
    if category in prompt_library:
        # Format the prompt with user input
        prompt = prompt_library[category].format(**user_input)
        return query_openai(prompt)
    else:
        return "Sorry, I don't have a response for this category."

# example_user_input = {"product_name": "OpenAI API"}
# example_category = "product_info"

# Another Example
example_user_input = {"issue_description": "I cannot log into my account"}
example_category = "troubleshooting"

response = generate_response(example_user_input, example_category)
print("Generated Response:", response)

