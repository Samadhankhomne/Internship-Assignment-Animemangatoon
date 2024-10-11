import nltk
from nltk.tokenize import word_tokenize

# Predefined responses
responses = {
    "what is castle swimmer about": "Castle Swimmer is about a young merman named Kappa who is prophesied to save various underwater kingdoms, leading him on a journey of discovery.",
    "who are the main characters": "The main characters in Castle Swimmer include Kappa, the merman destined by prophecy, and Siren, the Prince of the Shark Kingdom.",
    "what happens in chapters 83-89": "In chapters 83-89 of Castle Swimmer, a new prophecy is revealed that changes the course of Kappa and Siren's journey, leading to intense confrontations and emotional moments.",
    "who is kappa": "Kappa is the protagonist of Castle Swimmer, a merman chosen by prophecy to help various underwater kingdoms, but he struggles with the burden of his destiny.",
    "who is siren": "Siren is the Prince of the Shark Kingdom and one of the main characters, deeply connected to Kappa through fate and prophecy.",
}

# Function to process user input and respond based on keywords
def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())  # Tokenize and convert to lowercase
    response = "Sorry, I don't understand that. Can you ask something else?"
    
    for key in responses.keys():
        key_tokens = word_tokenize(key)
        if all(token in tokens for token in key_tokens):
            response = responses[key]
            break
    
    return response

#  Main loop to interact with the chatbot
def chat():
    print("Castle Swimmer Chatbot is online! Ask me questions about Castle Swimmer.")
    while True:
        user_input = input("You:")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        print("Bot:", chatbot_response(user_input))

# Run the chatbot
chat()


