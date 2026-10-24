import nltk
import re
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
nltk.download("stopwords", quiet=True)

def read_article(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read().replace("\n", " ")
    article = [s.strip() for s in text.split(". ") if s.strip()]
    sentences = []
    for sentence in article:
        cleaned = re.sub(r"[^a-zA-Z]", " ", sentence)
        sentences.append(cleaned.split())
    return sentences
def sentence_similarity(sentence1,sentence2,stop_words=None):
    if stop_words is None:
        stop_words=[]
    sentence1= [words.lower() for words in sentence1]
    sentence2= [words.lower() for words in sentence2]
    all_words=list(set(sentence1+sentence2))
    vector1=[0]*len(all_words)
    vector2=[0]*len(all_words)
    for word in sentence1:
        if(word in stop_words):
            continue
        vector1[all_words.index(word)]+=1
    for word in sentence2:
            if(word in stop_words):
                continue
            vector2[all_words.index(word)]+=1
    if not any(vector1) or not any(vector2):
         return 0.0
    return 1 - cosine_distance(vector1, vector2)
def generate_similarityMatrix(sentences,stop_words):
     similarityMatrix=np.zeros((len(sentences),len(sentences)))
     for i in range(len(sentences)):
          for j in range(len(sentences)):
                 if(i==j):
                     continue
                 similarityMatrix[i][j]=sentence_similarity(sentences[i],sentences[j],stop_words)
     return similarityMatrix
def generate_summary(file_name,max_lines=10):
     stop_words=stopwords.words("english")
     summary=[]
     sentences=read_article(file_name)
     sentence_simpilarityMatrix=generate_similarityMatrix(sentences,stop_words)
     sentence_simpilarityGraph=nx.from_numpy_array(sentence_simpilarityMatrix)
     scores=nx.pagerank(sentence_simpilarityGraph)
     ranked_sentences=sorted(((scores[i],s) for i,s in enumerate(sentences)),reverse=True)
     max_lines = min(max_lines, len(ranked_sentences))
     for i in range(max_lines):
        summary.append(" ".join(ranked_sentences[i][1]))
     print("Summary: \n",". ".join(summary)+".")
     return summary
if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "sample_article.txt"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    generate_summary(path, n)