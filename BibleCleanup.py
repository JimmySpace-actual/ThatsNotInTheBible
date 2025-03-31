import nltk
import unicodedata
from nltk.corpus import stopwords

# Function to process the message
def process_message(raw_words):

    # Remove punctuation
    apostrophes = {"'", "’", "‘", "ʼ"}
    words = {word for word in raw_words if not any(apo in word for apo in apostrophes)}
    
    # Remove stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = {word for word in words if word not in stop_words}
    
    return filtered_words

# Main function
def main():

    with open("kjbibleUNIQUE.txt", "r") as file:
        words = set(file.readlines())
    
    filtered_words = process_message(words)
    with open("kjbibleUniqueCleaned.txt", "w") as file:
        for word in filtered_words:
            file.write(f"{word}")

if __name__ == "__main__":
    nltk.download('stopwords')
    nltk.download('punkt')
    main()