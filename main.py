import pandas as pd
# import requests
# from bs4 import BeautifulSoup
import numpy as np
from pprint import pprint
# from nltk.util import ngrams
# from nltk.stem.porter import *
# from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Create a function to calculate polarity score
def polarity_score (text):
    # Use TextBlob to give polarity score for a given string
    return TextBlob(text).polarity

def subjectivity_score (text):
    # Use TextBlob to give polarity score for a given string
    return TextBlob(text).subjectivity

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Read in data, format and combine
    from Data import companies

    # Use apply to call the polarity_score function and obtain a score for each company's purpose
    companies['Polarity'] = companies['Purpose'].apply(polarity_score)

    # Use apply to call the subjectivity_score function and obtain a score for each company's purpose
    companies['Subjectivity'] = companies['Purpose'].apply(subjectivity_score)

    # Sort based on the polarity score for each company's purpose
    companies = companies.sort_values(by = ['Polarity'], ascending = False)

    # Print our the top and bottom 10 values
    pprint(companies.head(10))
    pprint(companies.tail(10))

    # Save companies with polarity and subjectivity to Excel file for easy viewing
    #companies.to_excel("D:\Dan\Stevens\Fin Tech\Companies_with_Purpose.xlsx", index = False)

"""
I noticed that most of the purposes are either neutral or positive.  Very few had a negative value.
While this is subjective and may not be incredibly accurate with just one evaluation,
it does make sense that any given company would want to have a positive, or at least neutral purpose.
Companyies with a negative purpose would not be looked at favorably and would not attract investors,
talent, etc.

I also noticed that most of the subjectivity seems to be low (majority at a value of 0).  I would tend
to agree, after skimming the list of purposes.  This either makes sense given that I think the purposes
are pretty neutral, or it means I'm of a similar bias as the population that generated the sentiment
analysis.  Probably a bit of both in this case.

"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
