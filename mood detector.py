import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#IMPORTANT: need to execute "nltk.download()" in order to install the data and have the program function
__author__ = "Emily"

def determine_message_tone(messages):
    # Create an instance of the SentimentIntensityAnalyzer class
    sentiment_analyzer = SentimentIntensityAnalyzer()

    # Calculate the sentiment score for each message
    sentiment_scores = [sentiment_analyzer.polarity_scores(message) for message in messages]

    # Determine the average sentiment score
    avg_sentiment_score = sum([score['compound'] for score in sentiment_scores]) / len(sentiment_scores)

    # Determine the overall tone of the messages
    if avg_sentiment_score >= 0.2:
        return 'Positive'
    elif avg_sentiment_score > -0.2 and avg_sentiment_score < 0.2:
        return 'Neutral'
    else:
        return 'Negative'

class Chat:
    '''
    This chat class is intended to help resolve any negative emotions that the user may have
    '''
    def __init__(self):
        self.intents = {
            "greet": {
                "examples": ["Hello", "Hi", "Hey"],
                "response": "Hello! How can I help you?"
            },
            "goodbye": {
                "examples": ["Goodbye", "Bye"],
                "response": "Goodbye! I hope you have a great day."
            },
            "lost":{
                "examples": ["lost","hectic","messy","don't know where","little time","not enough time","confused","busy"],
                "response": "You could use an organizer such as a Google Doc, Calendar, or Notion to stay organized. Whenever you think you need advice, please seek advice. Knowing your weaknesses and asking questions about them is a strength."
            },
            "lonely":{
                "examples": ["lonely", "friends are", "isolated", "no friends", "silent", "alone", "disconnected"],
                "response": "Try calling or messaging your loved ones and friends. Showing gratitude can be a good step to solidifying your relationships."
            },
            "angry":{
                "examples": ['angry', 'mad','disappointed','frustrated','low grade','unreasonable'],
                "response": "It's okay to be angry, things may not work out all the time. Some people may have difficulty understanding you or not try to understand. I hope that things can be resolved well."
            },
            "hungry":{
                "examples": ["empty", " hungry", "want food", "diarrhea"],
                "response": "Please treat yourself to a nice meal and eat well."
            },
            "sleep": {
                "examples": ["sleep", "deprivation", "always tired"],
                "response": "Make sure you are getting enough sleep! Most people need 8 hours of sleep. If you have insomnia, you may want to consult with an expert."
            },
            "exercise":{
                "examples": ["lack of exercise", "exercise", "weight"],
                "response": "Go to a gym or go outside to get some exercise! Most people need around 30 mins of exercise each day. Exercising can help you feel good."
            },
            "break up":{
                "examples": ["break up", "boyfriend", "girlfriend", "bad date", "hate"],
                "response": "I am so sorry about your break up. I suggest that you move on if you feel that your relationship is detrimental to your well being. If you strongly feel that you want to get back together, you can try to contact your significant other and communicate your struggles"
            },
            "ill":{
                "examples": ["I am not feeling well", "I have a headache", "I am coughing and sneezing", "headache", "cough", "sneeze", "fever"],
                "response": "You may have a cold or fever. Make sure to take care of yourself, drink tea, and visit a doctor if symptoms worsen"
            },   
        }
        
    def predict_intended(self, text):
        for intent, data in self.intents.items():
            if any(example in text for example in data["examples"]): 
                return intent
        return None
                
    def respond(self, text):
        intent = self.predict_intended(text)
        if intent is None:   #to handle 'None' error
            return "I'm sorry about that, I hope you feel better."
        response = self.intents[intent]["response"]
        return response
    
    def chat(self):
        while True:
            text = input("Is there anything that seems to be impacting your mood negatively? (Type 'quit' to exit) ")
            if text == "quit":
                break
            response = self.respond(text)
            print(response)
    

#for positive sentiment
def positive():
    good = input("Glad that you seem to be doing well. What do you think is making you content right now? ")
    print("Great, keep doing what you are doing and you are sure to be successful!")
    
#for negative sentiment
def negative():
    print("It seems like you aren't feeling your best.")
    chatbot = Chat() #Create an instance of the Chat class
    chatbot.chat()
    

if __name__ == '__main__':
    '''
    sample phrases = [
        'I am having a great day!',
        'I feel happy and optimistic',
        'okay, fine',
        'I am having a bad day',
        'feeling under the weather'
    ]
    '''
    print("This program is used to determine your mood and help you reflect!")
    print("Please enter 3 phrases that describe how you feel:")
    phrases = []
    for i in range(3):
        phrases.append(input("Enter a phrase: "))
    tone = determine_message_tone(phrases)
    print(f'Overall tone of messages: {tone}')
    
    if (tone == 'Positive'):
        positive()
    elif (tone == 'Negative'):
        negative()
    else:
        print("I hope you are feeling good!")

    

