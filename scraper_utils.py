#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import os
import regex as re



def findEndIndex(string):
    for i in range(len(string)):
        if(string[i] == "        <br/>"or string[i] == "        ' <br/> '"):
            return i;


def getPages(url = "https://www.hrc.org/resources/healthcare-facilities/",string_input="New Jersey"):
    url = url
    string_input= string_input.replace(" ","+")
    result = requests.get(os.path.join(url,"search?q="+string_input))
    src = result.content
    soup = BeautifulSoup(src,'lxml')
    return len(soup.find_all('li',{"class":"inline-block mr-8"}))
    


getPages()


#p class = heading-32 for full scores
def scrape(url = "https://www.hrc.org/resources/healthcare-facilities/",string_input="New Jersey",hospital_info = None,sub_criteria_info = None,criteria_info = None):
    url = url
    string_input= string_input.replace(" ","+")
    for i in range(getPages(url,string_input)):
        if(i==0):
            result = requests.get(os.path.join(url,"search?q="+string_input))
        else:
            url2 = url+"search/"
            print(os.path.join(url,"p" + str(i+1) + "?" +"q="+string_input))
            result = requests.get(os.path.join(url2,"p" + str(i+1) + "?" +"q="+string_input))
            
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        links = soup.find_all('a',{"class": "block text-current"})
        urls = []
        title = []
        for i in range(len(links)):
            arr = np.array(links[i])
            if(arr[1]["class"][0] == 'align-middle'or arr[1]["class"] == 'align-middle'):
                begin = re.search('href= ?',links[1].prettify()).start() + 5
                end = re.search('\>(.*)',links[i].prettify()).start()
                urls.append(links[i].prettify()[begin:end].replace('"',''))
                title.append(arr[1].get_text())
            else:
                break;
        attributes = []
        sub_criteria= []
        criteria = []
        k = 0
        for i in urls:
            attributes = []
            attributes.append(title[k])
            print(title[k])
            k+=1
            result = requests.get(i)
            src = result.content
            soup = BeautifulSoup(src,'lxml')
            for i in soup.find_all('dd',{"class": "mb-32"}):
                if(i.find_all('a')!= None):
                    for j in (i.find_all('a')):
                        attributes.append(j['href'])

            address = str(np.array(soup.find_all('dd',{"class": "mb-32"}))[1]).split("\n")
            if(address[1].strip(" ")[:2]) == '<a':
                address = str(np.array(soup.find_all('dd',{"class": "mb-32"}))).replace("\n","").replace("\\n","\n").split("\n")
            for i in range(len(address)):
                if(address[i]=="        <br/>" or address[i] == "        ' <br/>  '"):
                    address = np.delete(address,i)
                    break;
            ind = findEndIndex(address)
            street_address=""
            city = ""
            state = ""
            zipCode=""
            if(ind == 4):
                street_address = address[1].strip(" ")
                city,state = address[2].strip(" ").split(",")
                state = state.strip(" ")
                zipCode = address[3].strip(" ")
            if(ind==5):
                street_address = address[1].strip(" ") + " " + address[2].strip(" ")
                city,state = address[3].strip(" ").split(",")
                state = state.strip(" ")
                zipCode = address[3].strip(" ")
            
            attributes.append(street_address)
            attributes.append(city)
            attributes.append(state)
            attributes.append(zipCode)
            try:
                score = str(soup.find_all('div',{"class":"bg-yellow-500 heading-48 p-16 text-black text-center w-full md:p-32"})[0].get_text()).split("\n")[1].strip(" ")
            except:
                score = str(soup.find_all('div',{"class":"bg-blue-100 heading-48 p-16 text-black text-center w-full md:p-32"})[0].get_text()).split("\n")[1].strip(" ")
                
            
            attributes.append(score)
            sub_criteria = []
            criteria = []
            for i in soup.find_all('p',{"class":"font-bold text-18 text-right"}):
                sub_criteria.append(str(i.get_text()).strip(" ").strip("\n")[24:])
            for j in soup.find_all('p',{"class":"heading-32"}):
                criteria.append(str(j.get_text()).split("\n")[1].strip(" "))
            hospital_info.append(attributes)
            sub_criteria_info.append(sub_criteria)
            criteria_info.append(criteria)


