import openai


api_key = input('Input your API key (NOT THIS INCURS PERSONAL COST): ')

# Initialize OpenAI API client
openai.api_key = api_key

# Example API request
response = openai.Completion.create(
    engine="text-davinci-002",  # Specify the engine
    prompt="Describe the query you want written and specify sql: ",
    max_tokens=100,  # Set maximum length of response
)

# Access the generated response
generated_text = response.choices[0].text
print(generated_text)