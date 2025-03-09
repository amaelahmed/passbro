import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyBd5TbPZhxLaoV4rgxWKjt8RRN5LzpeO8I")

# Select the generative model, you can try "gemini-1.5-pro" or another one from the list
model = genai.GenerativeModel("gemini-1.5-pro")  # Or "gemini-1.5-pro-001" if needed

# Generate content
response = model.generate_content("Tell me a weird money fact.")

# Print the response text
print(response.text)

