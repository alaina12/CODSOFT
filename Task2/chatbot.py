import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': ['hello', 'hi', 'hey', 'greetings'],
            'about_products': ['tell me about your products', 'what do you sell', 'products'],
            'technical_support': ['help with technical issues', 'technical support', 'fix a problem'],
            'returns_policy': ['return policy', 'how to return a product', 'refund'],
            'farewell': ['bye', 'goodbye', 'see you later', 'exit']
        }
    
    def get_intent(self,user_input):
        for intent, patterns in self.responses.items():
            for pattern in patterns:
                if pattern in user_input:
                    return intent
        return 'general_query'
    
    def respond(self, intent):
        if intent == 'greeting':
            return "Hello! How can i help you today?"
        elif intent == 'about_products':
            return "We offer a variety of products. What are you interested in?"
        elif intent == 'technical_support':
            return " I'm sorry to hear you're having technical issues. Please provide more details."
        elif intent == 'returns_policy':
            return "Our return policy allows you to return products within 30 days. How can I assist you with return?"
        elif intent == 'farewell':
            return " Goodbye! If you more questions, feel free to ask."
        else:
            return "I'm not sure how to respond. Can you please provide more information?"

    def chat(self):
        print("Welcome to the simple ChatBot! Type 'exit' to end the conversation.")

        while True:
            user_input = input("You: ").lower()

            if user_input == 'exit':
                print("ChatBot : Goodbye! Have a great day.")
                break
            intent = self.get_intent(user_input)
            response = self.respond(intent)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()