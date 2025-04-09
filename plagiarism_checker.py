import argparse
import os
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK stopwords if not already present
try:
    stop_words = stopwords.words('english')
except:
    import nltk
    nltk.download('stopwords')
    stop_words = stopwords.words('english')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    
    return ' '.join(filtered_words)

def read_files(file_paths):
    documents = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            processed_text = preprocess_text(text)
            documents.append(processed_text)
    return documents

def calculate_similarity(documents):
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def main():
    parser = argparse.ArgumentParser(description='Plagiarism Checker')
    parser.add_argument('files', nargs='+', help='List of text files to compare')
    args = parser.parse_args()

    # Check if files exist
    for f in args.files:
        if not os.path.isfile(f):
            print(f"Error: File '{f}' not found!")
            return

    # Read and process documents
    documents = read_files(args.files)
    
    # Calculate similarity matrix
    similarity_matrix = calculate_similarity(documents)
    
    # Print results
    print("\nPlagiarism Check Results:")
    print("=========================")
    for i in range(len(args.files)):
        for j in range(i+1, len(args.files)):
            similarity = similarity_matrix[i][j] * 100
            print(f"Similarity between '{os.path.basename(args.files[i])}' and '{os.path.basename(args.files[j])}': {similarity:.2f}%")

if __name__ == "__main__":
    main()
