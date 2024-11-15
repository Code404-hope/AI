import openai

# Set up your OpenAI API key
openai.api_key = 'your_openai_api_key'

def chatbot():
    print("AI Chatbot: Hi! How can I assist you today? Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("AI Chatbot: Goodbye!")
            break
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are a helpful and friendly assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            ai_response = response['choices'][0]['message']['content']
            print(f"AI Chatbot: {ai_response}")
        except Exception as e:
            print(f"AI Chatbot: An error occurred: {e}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()