# TextRank Text Summarizer

An extractive text summarizer in Python. It scores sentences using
cosine similarity and PageRank (TextRank), then returns the top N.

## How it works
1. Split the article into sentences
2. Build a sentence-similarity matrix (cosine similarity, stopwords removed)
3. Run PageRank on the similarity graph
4. Return the highest-ranked sentences

## Installation
```bash
git clone https://github.com/<your-username>/textrank-text-summarizer.git
cd textrank-text-summarizer
pip install -r requirements.txt
```

## Usage
```bash
python summarizer.py sample_article.txt 3
```

## Limitations
- Output is lowercase with punctuation removed
- Sentences are ordered by rank, not by original position
- Splits sentences on ". " only

## License
MIT