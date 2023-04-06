<h1>Reddit Sentiment Polarity</h1>


Reddit Sentiment Polarity is a application that performs sentiment analysis on Reddit posts based on user-specified topics and keywords. The application uses natural language processing (NLP) techniques to analyze the sentiment of posts and assign a polarity score.


## Installation and Usage
To use Reddit Sentiment Polarity, follow these steps:

1. Clone the repository using the following command:

 ```bash
git clone https://github.com/gabrielsants/reddit-sentiment-polarity.git
 ```

2. Install the required Python packages using `pip`. You can find a list of required packages in the `requirements.txt` file.

```bash
pip install -r requirements.txt
 ```
 
3. Start the application by running main.py.

```bash
python main.py
 ```
 
4. A menu will be promped. Follow the instructions to continue. If you have any doubts, there is a option for help.

## How it Works
Reddit Sentiment Polarity uses the `PRAW` (Python Reddit API Wrapper) library to retrieve posts from Reddit based on the user-specified topic and keywords. The application then uses the `TextBlob` library to perform sentiment analysis on the posts.

The sentiment analysis process involves several steps:

1. Text Preprocessing: The raw text of the posts is cleaned and preprocessed by removing stop words, punctuation, and special characters.

2. Part-of-Speech (POS) Tagging: Each word in the text is tagged with its part of speech (e.g., noun, verb, adjective).

3. Sentiment Analysis: The sentiment of each sentence in the text is determined by analyzing the words and their POS tags. The sentiment of the entire text is then calculated based on the sentiment of the individual sentences.

4. Polarity Score: A polarity score is assigned to the text based on its sentiment. The polarity score ranges from -1 (negative sentiment) to 1 (positive sentiment).

## Contributing
Contributions to Reddit Sentiment Polarity are welcome. If you find a bug or have an idea for a new feature, please open an issue or submit a pull request on GitHub.

## License
Reddit Sentiment Polarity is licensed under the MIT License. See the `LICENSE` file for more information.

Made with ❤️ by Gabriel Santos 👋🏽 [Contact!](https://www.linkedin.com/in/dev-gabriel-santos/)

<p>
	<a href="https://www.buymeacoffee.com/gabrielsaints">
		<img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
		height="50" width="210" alt="gabrielsaints"/>
	</a>
</p>
<br>
