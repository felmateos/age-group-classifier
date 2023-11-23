import pandas as pd
import numpy as np
import string
from nltk.tokenize import word_tokenize
import spacy
import os
from nltk.util import ngrams

#class encode
def encode_class(df, label_column):
    if (isinstance(df, pd.DataFrame)):
        l_unique = sorted(df[label_column].unique())
        label_map = {x: i for i, x in enumerate(l_unique)} 
        df[label_column+'_encoded'] = df[label_column].map(label_map)

#tokenization
def tokenize(df, text_column, to_lower=True, trans_nums=True):
    if (isinstance(df, pd.DataFrame)):
        if (to_lower):
            df[text_column] = df[text_column].str.lower()
        if (trans_nums):
            df[text_column] = df[text_column].str.translate(str.maketrans('', '', string.punctuation))
        df['word_tokens'] = [word_tokenize(text) for text in df[text_column]]

#lemmatization
def lemmatize(df, tokens_column, remove_punct=True):
    if (isinstance(df, pd.DataFrame)):
        try:
            nlp = spacy.load("pt_core_news_sm")
        except Exception:
            os.system("python -m spacy download pt_core_news_sm")
            nlp = spacy.load("pt_core_news_sm")
        filtered = []
        for sent in df[tokens_column]:
            sent = str(sent)
            doc = nlp(sent)
            temp = [token.lemma_ for token in doc if not token.is_punct and remove_punct]
            temp = " ".join(temp)
            filtered.append(temp)
        df['lemma'] = filtered