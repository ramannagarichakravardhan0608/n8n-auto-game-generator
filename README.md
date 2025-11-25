# 🎮 n8n Auto Game Generator  
A fully automated **Python game generator** built using **Streamlit + n8n AI Agent + Gemini Chat Model**.  
You simply enter any *game name*, and the system instantly generates a complete, playable Python game script.

---

## 🚀 Project Overview

This project connects Streamlit with an n8n workflow to automatically build Python games.  
When you type a game name (e.g., “snake”, “cyber runner”), the request is sent to an **n8n webhook**, which triggers:

1. **AI Agent**
2. **Google Gemini Chat Model**
3. **Code Generation**
4. **Response to Webhook**

The Streamlit app then saves the generated code as a `.py` file and allows you to **play the game instantly**.

---

## 🧩 How n8n Workflow Works

Your n8n workflow:

- 🟢 **Webhook Node** — receives game name from Streamlit  
- 🤖 **AI Agent Node** — processes instructions  
- 🔮 **Gemini Chat Model** — generates Python game code  
- ↩️ **Respond to Webhook Node** — sends code back to Streamlit  

The app then cleans the code and writes it locally as shown here:



🖥️ Features

🔗 Seamless Streamlit → n8n → Gemini → Streamlit integration

🕹️ Auto–generates working Python game files

▶️ One-click “Play” launches the game in Mac Terminal

⚡ Beginner-friendly and very lightweight

💡 Perfect for showcasing automation and AI capabilities

🛠️ Technologies Used
Frontend & App

Streamlit

Automation

n8n (Webhook, AI Agent, Response Nodes)

AI Model

Google Gemini Chat Model

Backend

Python 3.11+

requests

subprocess

os
📦 Installation

Clone the repo:
git clone https://github.com/<your-username>/n8n-auto-game-generator
cd n8n-auto-game-generator
pip install -r requirements.txt
▶️ Run the App
streamlit run app.py
🔧 Configure n8n Webhook

In app.py, update:
URL = "https://your-n8n-url/webhook-test/xxxxx"
🕹️ Usage

Open the web app

Type any game name

Click Generate → code is auto-created

Click Play → game starts in Terminal
📁 Project Structure
n8n-auto-game-generator/
│── app.py
│── README.md
│── requirements.txt
🌟 Author

Chakravardhan Ramannagari
AI • Automation • Python Developer

LinkedIn:[ https://linkedin.com/in/chakravardhan06](https://www.linkedin.com/in/ramannagarichakravardhan/)
