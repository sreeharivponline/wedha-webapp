import random
import nltk
import string
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files if not already present
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample corpus and responses
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey"]
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Hi! How can I assist you?"]

# Contextual topics and responses
TOPIC_RESPONSES = {
    "gender equality": [
        "Gender equality is crucial for sustainable development. It empowers women and girls to participate fully in society.",
        "By promoting gender equality, we can address social injustices and improve the well-being of all individuals.",
        "Empowering women is essential for achieving global peace and development.",
        "Gender equality fosters inclusive growth, allowing societies to thrive and innovate.",
        "Equal opportunities for women and men in education and work can reduce poverty and improve the quality of life for everyone."
    ],
    "climate change": [
        "Climate change disproportionately affects women, particularly in developing countries. It's essential to involve them in climate action.",
        "Addressing climate change requires gender-responsive approaches to ensure that women's voices are heard in decision-making.",
        "Climate justice is gender justice. We must fight for both.",
        "Women in rural areas are often the first to face the impacts of climate change, as they rely on natural resources for their livelihoods.",
        "Climate change worsens existing gender inequalities, making it harder for women to access education, healthcare, and economic opportunities."
    ],
    "gender diversity": [
        "Gender diversity encompasses a broad range of identities, including non-binary, transgender, and gender-fluid individuals.",
        "Promoting gender diversity means ensuring that all people, regardless of gender identity, have equal opportunities and are free from discrimination.",
        "Acknowledging gender diversity is essential for creating a more inclusive and equitable society.",
        "Gender diversity brings diverse perspectives, which can lead to more innovative solutions to global challenges like climate change."
    ],
    "climate impacts": [
        "Climate change leads to extreme weather events, rising sea levels, and food insecurity, which disproportionately affect vulnerable populations, especially women.",
        "The health impacts of climate change, such as heatwaves and air pollution, are felt most by marginalized communities, including women and children.",
        "Agriculture, a sector where many women are employed, is severely impacted by climate change, threatening food security and livelihoods.",
        "Climate impacts can force families to migrate, with women and children often facing higher risks of exploitation and violence during displacement."
    ],
    "gender and climate interconnected": [
        "Women are often primary caregivers and resource managers in their communities, making them critical agents of change in climate action.",
        "Empowering women in decision-making roles leads to more effective climate solutions, as they bring unique insights and experiences.",
        "Climate change exacerbates existing gender inequalities, limiting women's access to resources, education, and participation in climate policy.",
        "Women play a vital role in adapting to climate impacts by leading sustainable practices in agriculture, water management, and energy usage.",
        "Gender and climate are interconnected because both climate justice and gender equality aim to create a fair, sustainable future for all."
    ],
    "importance of awareness": [
        "Raising awareness about gender equality and climate change is vital for driving action and change.",
        "Education and awareness are key components in empowering communities to tackle climate challenges effectively.",
        "The more we know, the better we can advocate for a sustainable future.",
        "Awareness helps break down stereotypes and misconceptions about both gender roles and climate action.",
        "Building awareness on the interconnectedness of gender and climate can inspire inclusive, community-driven solutions to global challenges."
    ],
    "help": [
        "I can provide information about gender equality and climate change. What would you like to know?",
        "If you have any questions or need resources on gender equality or climate change, feel free to ask!",
        "I’m here to assist you with information about the intersection of gender diversity, climate justice, and sustainable development.",
        "Let me know how I can help you understand more about the relationship between gender and climate change."
    ]
}


def preprocess_text(text):
    """Preprocess the user input text."""
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = nltk.word_tokenize(text)
    try:
        # Lemmatize, filtering out punctuation
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    except Exception as e:
        print(f"Error during lemmatization: {e}")
    return tokens

def chatbot_response(user_input):
    """Generate a response based on user input."""
    # Convert the input to lowercase for better matching
    user_input_lower = user_input.lower()

    # Check for greetings
    if any(word in user_input_lower for word in GREETING_INPUTS):
        return random.choice(GREETING_RESPONSES)

    # Check for contextual topics
    for topic in TOPIC_RESPONSES.keys():
        if topic in user_input_lower:  # Check if the topic appears in the user input string
            return random.choice(TOPIC_RESPONSES[topic])
    
    return "I'm sorry, I didn't understand that. Can you please rephrase or ask about gender equality or climate change?"

class ChatBot:
    def get_response(self, message):
        """Get response from the chatbot."""
        return chatbot_response(message)

# Main interaction loop (user input directly, not from file)
if __name__ == "__main__":
    bot = ChatBot()
    print("ChatBot: Hi! I am here to talk about gender equality and climate change. How can I assist you today?")
    
    while True:
        user_input = input("You: ")  # Take input from the user directly
        if user_input.lower() in ['exit', 'quit']:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = bot.get_response(user_input)
        print(f"ChatBot: {response}\n")
