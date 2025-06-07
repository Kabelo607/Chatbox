Cryptocurrency Investment Advice Chatbot

This Python project implements a rule-based chatbot designed to analyze cryptocurrency data and provide investment advice focused on profitability (price trends) and sustainability (energy efficiency and project viability).  The chatbot processes user queries by identifying relevant keywords, performing data analysis, and generating appropriate responses.

The core of the chatbot is built on a pattern matching system using regular expressions and synonym expansion via NLTK’s WordNet, enabling it to understand questions related to profitability and sustainability. Once an intent is detected, the bot fetches real-time cryptocurrency data through the CoinGecko API and analyzes price trends to determine potential profitability using simple trend evaluation techniques.

Sustainability insights are provided based on predefined information about each cryptocurrency’s consensus mechanism and environmental impact. For example, it highlights energy consumption differences between Proof of Work and Proof of Stake blockchains and references specific projects like Bitcoin, Ethereum, and Cardano.

The chatbot interacts with users in a conversational loop, accepting queries until the user chooses to exit. It gracefully handles unknown questions with fallback responses guiding users to ask about profitability or sustainability explicitly. Users can inquire about price trends or environmental impacts by typing natural language queries.

This project is a practical base for further enhancements, such as dynamically extracting cryptocurrency names from user input, integrating comprehensive sustainability datasets, or implementing advanced technical indicators for profitability analysis. It demonstrates how Python can combine natural language processing, API data retrieval, and rule-based logic to deliver domain-specific investment advice efficiently.

