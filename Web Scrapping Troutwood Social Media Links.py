## Importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/13.1.2'}




#getting a datafile:
df= pd.read_excel('excelFile.xls')
df = df.dropna(subset= ['website']) #drops any values that are empty


# this function takes in a data file, html content of a website, and a counter
#adds linkedin, facebook, twitter, instagram and careers page of that webste 
#returns the datafile

def findSocialMediaLinks(df, soup1,i):
    find_all_a = soup1.find_all("a", href=True) #gets all href tags

    for el in find_all_a:

        if "linkedin" in el['href']:
            df.linkedin_url[i] = el['href']
        elif "facebook" in el['href']:
            df.facebook_url[i] = el['href']
        elif "twitter" in el['href']:
            df.twitter_url[i] = el['href']
        elif "instagram" in el['href']:
            df.instagram_url[i] = el['href']
        elif "career" in el['href']:
            df.careers_url[i] = el['href']
        elif "youtube" in el['href']:
            df.youtube_url[i] = el['href']
    return df




for i in range(len(df.website)):
        try: 
            print(df.website[i])
            webpage= df.website[i]
            if webpage != "n":
                r=requests.get(webpage, headers=headers)
                soup1 = BeautifulSoup(r.content, 'html5lib') 
                df = findSocialMediaLinks(df, soup1,i )
        except:
            pass

df.to_excel('saved_file.xlsx')
