# 📚 Plagiarism Checker (Python DSA Project)

A simple command-line tool that compares multiple text files and detects similarity using **TF-IDF** and **cosine similarity**. It uses basic **NLP techniques** and **data structures** to help identify copied content.

---

## 🚀 Features

- Compares multiple `.txt` files
- Removes stopwords and punctuation
- Calculates cosine similarity based on word vectors
- Outputs similarity percentage between each pair of files

---

## 🧰 Requirements

- Python 3.8+
- Virtual environment (recommended)
- Required packages:
  - `nltk`
  - `scikit-learn`

---

## ⚙️ Setup Instructions (for macOS/Linux/Windows)

### 1. Clone or Download the Project
git clone <repo_url>
cd plagiarism-checker

Create and Activate Virtual Environment:

**1. Create a virtual environment:
**
"python3 -m venv plagiarism-env"
**Activate it:**
"source plagiarism-env/bin/activate"

**Install the required packages:**
"pip install nltk scikit-learn"


**Run your script:**
"python3 plagiarism_checker.py file1.txt file2.txt file3.txt"

**To Exit the Virtual Environment:**
"deactivate"

**Sample Output:**
Plagiarism Check Results:
=========================
Similarity between 'file1.txt' and 'file2.txt': 65.42%
Similarity between 'file1.txt' and 'file3.txt': 15.07%
Similarity between 'file2.txt' and 'file3.txt': 21.88%


**🛠️ Future Improvements**

GUI using Tkinter
HTML or CSV report export
Highlight plagiarized content line-by-line

