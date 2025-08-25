🍕 Food Reviews Sentiment Analysis Web App 🍔

A simple, interactive web application that allows users to analyze the sentiment of food reviews using VADER Sentiment Analysis. This app supports single review analysis as well as batch analysis via CSV upload, complete with visualizations and a word cloud.

🖲️ Analyze single food reviews and get instant sentiment feedback (Positive 😀, Neutral 😐, Negative 😡).

🖲️ Upload CSV files containing multiple reviews for batch sentiment analysis.

🖲️ Visualize sentiment distribution with pie charts.

🖲️ Generate a word cloud of the uploaded reviews.

🖲️ User-friendly interface built with Streamlit.

🖲️ Demo

🖲️ Enter a review in the text area and click “Analyze Sentiment” to see the result.

🖲️ Upload a CSV file with a column named Review to analyze multiple reviews at once.

🖲️ Installation & Prerequisites

Python 3.10 or above , 
pip package manager , 
🚀 Steps, 

Clone the repository:, 
git clone <your-repo-url>
cd <repo-folder>


🚀 Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows


🚀 Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run streamlit_app.py

Usage
Single Review Analysis

📷 Open the app in your browser. Type or paste a food review into the text area. Click 🔍 Analyze Sentiment.

🧑🏻‍💻 View the sentiment result:

Positive 😀 (compound score ≥ 0.05)

Neutral 😐 (-0.05 < compound score < 0.05)

Negative 😡 (compound score ≤ -0.05)

🧑🏻‍💻 Batch Analysis with CSV , Prepare a CSV file containing a column named Review. , Upload the CSV using the file uploader. , The app automatically analyzes all reviews and displays:

📍 Review text

📍 Sentiment score

📍 Sentiment label

📍 Visualizations:
Pie chart showing sentiment distribution & Word cloud of all review text

📊 Visualizations

Pie Chart: Displays the proportion of Positive, Neutral, and Negative reviews.

Word Cloud: Highlights the most frequent words from the uploaded reviews.

Technologies Used

✅ Python – Programming language

✅ Streamlit – Web app framework

✅ NLTK (VADER) – Sentiment analysis

✅ Pandas – Data handling

✅ Matplotlib & Seaborn – Visualization

✅ WordCloud – Word cloud generation

© License

This project is open-source and free to use.

© Contact

Built with ❤️ by Jithnuka Weerasinghe Year: 2025
