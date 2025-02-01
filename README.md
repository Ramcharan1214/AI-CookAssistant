# AI-CookAssistant
Welcome to the AI Cook Assistant repository! This project is a Streamlit-based chatbot designed to assist users with all aspects of cooking. Whether you need recipe suggestions, ingredient substitutions, step-by-step instructions, or meal planning tips, this AI-powered assistant is here to help. It leverages the power of Google's Gemini AI and LangChain to provide intelligent and context-aware responses.

🚀 Features
Cooking Assistance: Get help with recipes, ingredient substitutions, cooking techniques, and more.

Multi-Cuisine Knowledge: The assistant is knowledgeable about cuisines from around the world.

Dietary Restrictions: Provides suggestions tailored to dietary needs (e.g., vegan, gluten-free, etc.).

Real-Time Streaming: Responses are streamed in real-time for a smooth user experience.

Session History: Maintains chat history during the session for context-aware conversations.

Secure API Key Handling: Users can securely input their Google API key to access the AI model.

🛠️ Setup Instructions
Prerequisites
Python 3.8+: Ensure Python is installed on your system.

Google API Key: Obtain a Google API key to use the Gemini AI model. You can get it from the Google Cloud Console.

Installation
Clone this repository:

bash
Copy
git clone https://github.com/Ramcharan1214/AI-CookAssistant.git
cd AI-CookAssistant
Install the required Python packages:

bash
Copy
pip install -r requirements.txt
(If you don't have a requirements.txt file, install the dependencies manually):

bash
Copy
pip install streamlit langchain langchain-google-genai langchain-core
Running the Application
Start the Streamlit app:

bash
Copy
streamlit run app.py
Open your browser and navigate to the provided local URL (usually http://localhost:8501).

Enter your Google API key when prompted.

Start asking cooking-related questions!

🖥️ Usage
Enter Your API Key: When the app starts, you'll be prompted to enter your Google API key securely.

Ask Questions: Type your cooking-related questions in the input box. For example:

"How do I make a vegan lasagna?"

"What can I substitute for eggs in a cake recipe?"

"Give me a step-by-step guide to making sushi."

Get Responses: The AI assistant will provide detailed, context-aware answers in real-time.

📂 Project Structure
Copy
AI-CookAssistant/
├── app.py(Main Streamlit application code)
├── README.md(Project documentation)
├── requirements.txt(List of Python dependencies)
└── assets/(Folder for images or other assets)
🛑 Limitations
The assistant is designed to answer only cooking-related questions. It will not respond to unrelated queries.

You need a valid Google API key to use the Gemini AI model.

The chat history is maintained only during the current session and is not saved permanently.

🤝 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request. Please ensure your code follows the project's style and includes appropriate documentation.

🙏 Acknowledgments
Google Gemini AI: For providing the powerful language model.

LangChain: For enabling seamless integration with the AI model and chat history.

Streamlit: For making it easy to build and deploy interactive web apps.

Enjoy cooking with your AI assistant! 🍲👩‍🍳

Feel free to customize this README further to suit your needs! Let me know if you need additional help. 😊
