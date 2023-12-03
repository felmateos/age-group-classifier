import pandas as pd
import re
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px


def get_all_string(sentences):
    sentence = ''
    for words in sentences:
        sentence += words
    sentence = re.sub(r'http\S+', '', sentence) #remove os links
    return sentence 

def preprocess(series):
    all_string = get_all_string(series)
    all_string = nltk.RegexpTokenizer(r'\w+').tokenize(all_string)
    return all_string

def create_freq_df(cleaned_tokens): 
    fdist = nltk.FreqDist(cleaned_tokens)
    freq_df = pd.DataFrame.from_dict(fdist, orient='index')
    freq_df.columns = ['Frequency']
    freq_df.index.name = 'Term'
    freq_df = freq_df.sort_values(by=['Frequency'], ascending=False)
    freq_df = freq_df.reset_index()
    return freq_df

def plot_text_distribution(x_df, y_df, color, title, xaxis_text, yaxis_text):
    
    fig = px.bar(x=x_df, 
                y=y_df,
                color=y_df,
                text=y_df,
                color_continuous_scale=color)

    fig.update_layout(
        title_text=title,
        template='plotly_white',
        xaxis=dict(
            title=xaxis_text,
        ),
        yaxis=dict(
            title=yaxis_text,
        )
    )

    fig.update_traces(marker_line_color='black', 
                    marker_line_width=1.5, 
                    opacity=0.8)
    
    fig.show()

def create_wordcloud(freq_df, title, color):
    
    data = freq_df.set_index('Term').to_dict()['Frequency']
    
    plt.figure(figsize = (20,15))
    wc = WordCloud(width=800, 
               height=400, 
               max_words=100,
               colormap= color,
               max_font_size=200,
               min_font_size = 1 ,
               random_state=8888, 
               background_color='white').generate_from_frequencies(data)
    
    plt.imshow(wc, interpolation='bilinear')
    plt.title(title, fontsize=20)
    plt.axis('off')
    plt.show()

