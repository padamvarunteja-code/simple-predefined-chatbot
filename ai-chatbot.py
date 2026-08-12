 #import useful libraries
import random


#define some sample responses
greeting = [ 
    "Hi there!","Hey! How can I help you?",
    "hello! What can I do for you today?",
    "Greetings! How may I assist you?",
    "Hi! What brings you here today?"
]

help_responses = [
    "I can help with general questions.just ask!",
    "I can tell you some jokes "
    " I can tell fun facts if you like."
]

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the bicycle fall over? Because it was two-tired!"
]

fun_facts = [
    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
    "Octopuses have three hearts and blue blood. Two hearts pump blood to the gills, while the third pumps it to the rest of the body.",
    "Bananas are berries, but strawberries are not. Botanically speaking, a berry is a fruit produced from the ovary of a single flower with seeds embedded in the flesh."
]


#FUNCTIONS

##response function 
def chatty_response(user_input):
    """This function will generate a response based on user input."""
    user_input = user_input.lower()

    if any (greet in user_input for greet in ["hi", "hello", "hey"]):
        return random.choice(greeting)

    elif any (help in user_input for help in ["help", "support", "assist"]):
        return random.choice(help_responses)
        
    elif any (joke in user_input for joke in ["joke", "funny","laugh"]):
        return random.choice(jokes)
        
    elif any (fact in user_input for fact in ["fact", "fun fact","fun","knowledge"]):
        return random.choice(fun_facts)

    elif "your name" in user_input:
        return "I am ur chatbot.you can call me ai."

    elif "what's up?" in user_input:    
        return "Not much How about you?"

    elif "how are you?" in user_input:
        return " I am excellent ! Thank you for asking. How about you ?"

    return "sorry, I didn't understand . Can you please ask something else?"
    

##MAIN FUNCTION TO RUN THE CHATBOT
def chatbot():
    """This function will run the chatbot and handle user input and output."""
    print("Hello! I am your chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    #run a while loop so chat never actually ends until and unless the user types 'exit'
    while True:
        user_input = input("user: ")
        if user_input.lower() == 'exit':
            break
        else:
            response = chatty_response(user_input)
            print("chatty: ", response)




#Running the chatbot
if __name__ == "__main__":
    chatbot()