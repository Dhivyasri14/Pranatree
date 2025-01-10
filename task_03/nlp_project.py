'''Tokenization'''
# from nltk.tokenize import word_tokenize
# import nltk
# nltk.download('punkt')  
# text = "NLP is amazing! Its very interesting to learn."
# tokens = word_tokenize(text)
# print(tokens)

'''Stemming'''
# from nltk.stem import PorterStemmer

# stemmer = PorterStemmer()
# words = ["running", "runner", "jumps", "happily"]
# stems = [stemmer.stem(word) for word in words]
# print(stems)  

'''Lemmatization'''
# from nltk.stem import WordNetLemmatizer
# import nltk

# # Create a lemmatizer object
# lemmatizer = WordNetLemmatizer()
# words = ["running", "flying", "went", "cats"]
# # Lemmatize each word
# lemmas = [lemmatizer.lemmatize(word, pos="v") for word in words]  # pos="v" for verb lemmatization
# print("Lemmatized words:", lemmas)

'''Stop words'''
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# text = "Hi this is Dhivya, nice to meet you"
# # Tokenize the text (split into words)
# words = word_tokenize(text)
# stop_words = set(stopwords.words('english'))
# # Filter out stopwords from the tokenized words
# filtered_words = [word for word in words if word.lower() not in stop_words]
# print("Original Words:", words)
# print("Filtered Words:", filtered_words)

'''Textblog'''
# from textblob import TextBlob
# text = "I absolutely love Natural Language Processing. It's amazing!"
# blob = TextBlob(text)
# print("Polarity:", blob.sentiment.polarity) 
# print("Subjectivity:", blob.sentiment.subjectivity) 

'''Project task'''
from textblob import TextBlob

# Function to analyze sentiment and provide feedback
def analyze_sentiment(user_input):
    # Create a TextBlob object
    blob = TextBlob(user_input)
    
    # Get sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine feedback based on polarity
    if polarity > 0:
        sentiment = "positive"
        feedback = "That's great! Your input has a positive tone."
    elif polarity < 0:
        sentiment = "negative"
        feedback = "Your input has a negative tone."
    else:
        sentiment = "neutral"
        feedback = "Your input is neutral, no strong feelings detected."
    
    # Display sentiment score and feedback
    print(f"Sentiment Score: {polarity}")
    print(f"Feedback: {feedback}")

# Get user input
user_input = input("Please enter your text: ")

# Analyze sentiment and provide feedback
analyze_sentiment(user_input)






