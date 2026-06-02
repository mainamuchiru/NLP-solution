import re
from collections import Counter
from pathlib import Path

def count_specific_word(text, word_search):
    
    if not text or not word_search:
        return 0
    
    pattern = r'\b' + re.escape(word_search.lower()) + r'\b'
    matches = re.findall(pattern, text.lower())
    
    count = len(matches)
    return count

def identify_most_common_word(text):
    
    if not text:
        return None
    
    pattern = r"\b\w+\b"
    words = re.findall(pattern, text.lower())
    word_counts = Counter(words)
    
    most_common_word = word_counts.most_common(1)
    if most_common_word:
        top_word = most_common_word[0]

        word = top_word[0]

        return word
    else:
        return 0
    
    
     
    

def calculate_average_word_length(text):
    if not text:
        return 0
    pattern = r"\b\w+\b"
    words = re.findall(pattern, text)
    
    total_length = sum(len(word) for word in words)
    
    average_length = total_length / len(words)
    return float(average_length)

def count_paragraphs(text):
    
    if not text:
        return 1
    pattern = "\n\n"
    paragraphs = text.split(pattern)
    
    clean_paragraphs = []
    for p in paragraphs:
        if p.strip():          
         clean_paragraphs.append(p)

    count = len(clean_paragraphs)
    return int(count)


def count_paragraphs(text):
    if not text:
        return 1
    
    paragraphs = text.split("\n\n")
    clean_paragraphs = []
    
    count = 0
    while count < len(paragraphs):
        if paragraphs[count].strip():
            clean_paragraphs.append(paragraphs[count])
        count += 1
    
    return int(len(clean_paragraphs))



def count_sentences(text):
    
    if not text:
        return 1
    
    pattern = r"(?<=[.!?])+"
    sentences = re.split(pattern, text)
    clean_sentences = []
    for sentence in sentences:
        if sentence.strip() != "":
            clean_sentences.append(sentence)
    
    sentence_count = len(clean_sentences)
    return int(sentence_count)
    


if __name__ == "__main__":
    with open("newsarticle.txt", "r", encoding="utf-8") as f:
        word_text = f.read()
        
    print("Specific word count:", count_specific_word(word_text, "machine"))
    print("Most common word:", identify_most_common_word(word_text))
    print("Average word length:", calculate_average_word_length(word_text))
    print("Paragraph count:", count_paragraphs(word_text))
    print("Sentence count:", count_sentences(word_text))