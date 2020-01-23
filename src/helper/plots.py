import os
import datetime
import glob

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

def delete_all_files_in_image():
    """ 
        Deletes all files in image directory 
    """
    
    [os.remove(file) for file in glob.glob(os.path.join(os.getcwd(),"src/static/images/","*.png"))]

def get_filename(name):
    """
        Generated imagename and filename
    Parameters: 
        name: Suggested name ( type of plot) to add to image name
    Returns: 
        str : imagecname and file name """
        
    image_name='{}_{}_plot.png'.format(datetime.datetime.now().strftime("%Y-%m-%d"),name)
    file_name = os.path.join(os.path.sep,os.getcwd(),"src","static","images",image_name)

    return image_name,file_name
    
   

def generate_barplot(df,name,xlabel,ylabel,rot_val=0): 
    """
        Generated bar plot 
    Parameters: 
        dataframe , name , labels and label rotation
    Returns: 
        Saves the plot as image"""

    image_name,file_name=get_filename(name)
    
    plt.figure()
    df.T.plot(kind='bar',rot=rot_val)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.savefig(file_name, format='png')
    plt.close()
    

    return image_name

def generate_histplot(df,name,xlabel,ylabel,col1,col2):
    """
      Generated histogram plot 
    Parameters: 
     dataframe , name , labels and label rotation
    Returns: 
       Saves the plot as image"""

    image_name,file_name=get_filename(name)
    plt.figure()
    df.plot.bar(x=col1, y=col2)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.savefig(file_name, format='png')
    plt.close()

    return image_name


def generate_word_cloud(df,name):

    """
     Removes stopwords, tokenizes the lyrics and generated a word cloud 
    Parameters: 
     dataframe , name for the file
    Returns: 
       Saves the plot as image"""
  
    lyrics_words = ' '
    stopwords = set(STOPWORDS) 
    
    # iterate through the csv file 
    for val in df.LyricsList: 
        
        # typecaste each val to string 
        val = str(val) 
    
        # split the value 
        tokens = val.split() 
        
        # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
            
        for words in tokens: 
            lyrics_words = lyrics_words + words + ' '
    
    
        wordcloud = WordCloud(width = 800, height = 800, 
                        background_color ='white', 
                        stopwords = stopwords, 
                        min_font_size = 10).generate(lyrics_words) 
        
        # plot the WordCloud image                        
        plt.figure(figsize = (8, 8), facecolor = None) 
        plt.imshow(wordcloud) 
        plt.axis("off") 
        plt.tight_layout(pad = 0) 
        
        image_name,file_name=get_filename(name)
        plt.savefig(file_name, format='png')
        f = plt.figure()
        f.clear()
        plt.clf()
        plt.close(f)      
        
        
        return image_name