import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import src.helper.plots as plot


class SentimentAnalyzer(object):

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.labels = ['negative', 'neutral', 'positive']
        self.explode = (0.1, 0, 0)
        self.colors = ['gold', 'yellowgreen', 'lightcoral',]

    def _generate_scores(self, text):
        return self.analyzer.polarity_scores(text)

    def generate_sentiment_graph(self, df, name):
        lyrics_words=''
        for val in df.LyricsList: 
            val = str(val) 
            tokens = val.split() 
            for i in range(len(tokens)): 
                tokens[i] = tokens[i].lower() 
            for words in tokens: 
                lyrics_words = lyrics_words + words + ' '

        score = self._generate_scores(lyrics_words)
        sizes = [score['neg'], score['neu'], score['pos']]
        plt.figure()
        plt.pie(sizes,explode=self.explode,labels=self.labels,colors=self.colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        circle=plt.Circle( (0,0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(circle)
        image_name,file_name=plot.get_filename(name)
        plt.savefig(file_name)
        plt.close()
       

        return image_name