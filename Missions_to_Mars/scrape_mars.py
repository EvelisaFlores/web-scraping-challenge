# Dependencies
import os
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import pymongo
from selenium import webdriver


def init_browser():
     executable_path = {'executable_path': 'chromedriver.exe'}
     browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_news ={}

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title text
    title = soup.title.text
    
    # Print all paragraph texts
    paragraphs = soup.find_all('p')
    
    # Store data in a dictionary
    mars_data ["news_title"]=title
    mars_data ["news_paragraph"]= paragraphs
    

    # JPL MARS SPACE IMAGES-FEATURED IMAGE
    #url for Sapce image
    base_url='https://www.jpl.nasa.gov'
    images_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(images_url)

    results = browser.find_by_xpath('//*[@id="fancybox-lock"]/div/div[1]/img').click()
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img = soup.find("img", class_="fancybox-image")["src"]
    featured_image_url=base_url+img
    #mar_news["featured_image"]=featured_image_url

    # MARS FACTS
    facts_url='https://space-facts.com/mars/'
    time.sleep(2)
    table = pd.read_html(facts_url)
    table[0]
    df=table[0]
    df.columns = ['Descriptions','Values']
    df.set_index(['Descriptions'])
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    mars_news["mars_facts"]=html_table

    #MARS HEMISPHERES
    base_url='https://astrogeology.usgs.gov/'
    hemispheres_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    hemisphere_image_urls=[]

    ##Cerberus Hemisphere Enhanced
    results = browser.find_by_xpath('//*[@id="wide-image"]/img').click()
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find("img", class_="wide-image")["src"]
    cereberus_img_url=base_url+img_url
    #print(cereberus_img_url)
    img_title=soup.find('h2', class_="title").text
    #print(img_title)
    cerberus_hemisphere ={"image title":img_title, "img_url":cereberus_img_url}
    hemisphere_image_urls.append(cerberus_hemisphere)

    ##Schiaparelli Hemisphere Enhanced
    results = browser.find_by_xpath('//*[@id="wide-image"]/img').click()
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url=base_url+img_url
    #print(schiaparelli_img_url)
    img_title=soup.find('h2', class_="title").text
    #print(img_title)
    schiaparelli_hemisphere ={"image title":img_title, "img_url":schiaparelli_img_url}
    hemisphere_image_urls.append(schiaparelli_hemisphere)

    ##Syrtis Major Hemisphere Enhanced
    results = browser.find_by_xpath('//*[@id="wide-image"]/img').click()
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find("img", class_="wide-image")["src"]
    syrtis_img_url=base_url+img_url
    #print(syrtis_img_url)
    img_title=soup.find('h2', class_="title").text
    #print(img_title)
    syrtis_hemisphere ={"image title":img_title, "img_url":syrtis_img_url}
    hemisphere_image_urls.append(syrtis_hemisphere)

    ##Valles Marineris Hemisphere Enhanced
    results = browser.find_by_xpath('//*[@id="wide-image"]/img').click()
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find("img", class_="wide-image")["src"]
    valles_img_url=base_url+img_url
    #print(valles_img_url)
    img_title=soup.find('h2', class_="title").text
    #print(img_title)
    valles_hemisphere ={"image title":img_title, "img_url":valles_img_url}
    hemisphere_image_urls.append(valles_hemisphere)

    #mars_news[hemisphere_image_urls]

    mars_data={
        "news_title":title,
        "news_paragraph":paragraph,
        "featured_image":featured_image_url,
        "mars_hemisphere":hemisphere_image_urls
       }
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data 