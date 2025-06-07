import nltk
import re
import requests
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

keywords = {
    'profitability': ['price', 'trend', 'profit', 'gain', 'growth'],
    'sustainability': ['energy', 'efficiency', 'green', 'environment', 'viability', 'sustainable', 'eco']
}

def expand_keywords(word_list):
    expanded = set()
    for word in word_list:
        synonyms = wordnet.synsets(word)
        for syn in synonyms:
            for lemma in syn.lemmas():
                expanded.add(lemma.name().replace('_', ' '))
    return list(expanded)

keywords_expanded = {k: expand_keywords(v) for k,v in keywords.items()}

patterns = {}
for intent, words in keywords_expanded.items():
    pattern = '|'.join([r'\b' + re.escape(word) + r'\b' for word in words])
    patterns[intent] = re.compile(pattern, re.IGNORECASE)

responses = {
    'profitability': "Analyzing recent price trends and market signals for profitability...",
    'sustainability': "Evaluating energy efficiency and project viability metrics...",
    'fallback': "Sorry, I didn't understand that. Could you please specify if you want advice on profitability or sustainability?"
}

def get_price_trends(crypto_id):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency=usd&days=30'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = [p[1] for p in data['prices']]
        return prices
    return []

sustainability_factors = {
    'bitcoin': 'Bitcoin uses energy-intensive Proof of Work, which has higher environmental impact.',
    'ethereum': 'Ethereum is transitioning to Proof of Stake, improving energy efficiency.',
    'cardano': 'Cardano uses Proof of Stake and prioritizes sustainability and scalability.'
}

def get_sustainability_info(crypto_name):
    return sustainability_factors.get(crypto_name.lower(), "Sustainability data is not available for this cryptocurrency.")

def provide_investment_advice(user_input):
    for intent, pattern in patterns.items():
        if pattern.search(user_input):
            if intent == 'profitability':
                crypto_id = 'bitcoin'  # or parse from user_input for real app
                prices = get_price_trends(crypto_id)
                return analyze_trend(prices)
            elif intent == 'sustainability':
                crypto_name = 'bitcoin'  # or parse from user_input for real app
                return get_sustainability_info(crypto_name)
    return responses['fallback']

def chatbot():
    print("Welcome! Ask me about cryptocurrency investment advice focusing on profitability or sustainability. Type 'quit' to exit.")
    while True:
        user_text = input("You: ").lower()
        if user_text == 'quit':
            print("Chatbot: Thank you for chatting! Goodbye.")
            break
        response = provide_investment_advice(user_text)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()

