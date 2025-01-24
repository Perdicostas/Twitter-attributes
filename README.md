# Tweet Aspect Extractor

This Python script processes tweets from a CSV file, tokenizes the text using Natural Language Processing (NLP) techniques, and identifies key aspects based on term frequency. It is useful for extracting insights from tweet datasets by identifying the most frequently occurring terms.

## Features
- **Load Tweets from CSV**:
  - Reads tweets stored in a CSV file.
  - Filters out short tweets (default: less than 20 characters).
- **Tokenization**:
  - Splits tweets into sentences and further into individual words using the `nltk` library.
- **Stopword Removal**:
  - Removes common stopwords (e.g., "the," "is," "and") and short words (less than 3 characters) to focus on meaningful terms.
- **Aspect Extraction**:
  - Calculates the frequency of terms across all tweets.
  - Returns the top N aspects (frequent terms) based on user-specified parameters.

## Requirements
- Python 3.6 or later
- Required Python libraries:
  - `nltk` (install via `pip install nltk`)

## Setup and Usage
1. **Prepare the Dataset**:
   - Ensure your tweet dataset is stored in a CSV file, with each tweet in the first column.
   - Replace `'FILE_NAME.csv'` in the script with the name of your CSV file.
2. **Install Required Libraries**:
   - Install the `nltk` library:
     ```bash
     pip install nltk
     ```
   - Download necessary NLTK data:
     ```python
     import nltk
     nltk.download('punkt')
     nltk.download('stopwords')
     ```
3. **Run the Script**:
   - Save the script to a file (e.g., `tweet_aspect_extractor.py`).
   - Execute the script:
     ```bash
     python tweet_aspect_extractor.py
     ```
4. **Customize Parameters**:
   - To change the minimum tweet length for filtering, modify the `tweet_length_lower_bound` parameter in the `load_tweet()` function.
   - Adjust the number of aspects (frequent terms) to extract by modifying the second argument in the `get_aspects()` function (e.g., `get_aspects(fn_tweets, 10)`).

## Example Output
Given a sample dataset of tweets, the script outputs the top aspects (frequent terms) as a list of tuples containing the term and its frequency:

```plaintext
[('example', 25), ('tweets', 18), ('data', 15), ('analysis', 10), ('python', 8)]```

## License
This project is open source and available under the [MIT License](LICENSE).
