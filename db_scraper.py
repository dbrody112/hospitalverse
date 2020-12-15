#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scraper_utils import scrape
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sqlalchemy
import regex as re
import googlemaps
import glob
from datetime import datetime
gmaps = googlemaps.Client('AIzaSyB1Z-6bjs8iuKOQPmHAGytnDFg13idfheI')
# In[2]:
def calculate_complete_score(hrc_score, hospital_name, hospital_latitude, hospital_longitude, hate_groups,max_dist,current_year,hate_group):
    if(hrc_score == 'N/A' or hrc_score == float("nan")):
        return float("nan")
    score = 0
    r = 6371 #radius of earth
    phi1 = np.radians(hospital_latitude)
    
    
    for i in range(len(hate_groups)):
        phi2 = np.radians(hate_groups['latitude'][i])
        delta_phi = np.radians(abs(hospital_latitude - hate_groups['latitude'][i]))
        delta_lambda = np.radians(abs(hospital_longitude-hate_groups['longitude'][i]))
        a = np.sin(delta_phi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        haversine = (r*c)
        
        if(haversine <= max_dist):
            hate_group.append([hospital_name,hate_groups['Title'][i], hate_groups['Ideology'][i], hate_groups['latitude'][i], hate_groups['longitude'][i],haversine,hate_groups['Year'][i]])
            if(hate_groups["Ideology"][i] == "Anti-LGBTQ"):
                score+=10 - .1*(current_year-int(hate_groups['Year'][i]))
            else:
                score+=2-.1*(current_year-int(hate_groups['Year'][i]))
    return hrc_score-score

def load_data(csv_path = "nst-est2019-01.csv", hate_groups_csv_path_glob = 'C:/Users/DELL/Documents/Databases-python/Databases-python/hate_groups/*',
              existing_hospital_csv = [], existing_hate_group_csv = [], sub_criteria_csv = [], criteria_csv = [], hate_group_csv = []):
    state_csv = pd.read_csv(csv_path)
    df = pd.DataFrame({'state':np.array(state_csv)[:,0][8:59].astype(str)}).applymap(lambda x: x.replace(".","").strip())
    x = []
    for year in glob.glob(hate_groups_csv_path_glob):
        x.append(pd.read_csv(year))
    new_df = pd.concat(x).reset_index().drop(['index','Headquarters','Statewide'],axis=1)
    
    lat = []
    lng = []
    if(len(existing_hate_group_csv)==0):
        for i in range(len(new_df)):
            print(i)
            if(type(new_df['City'][i] == 'float')):
                geocode_result = gmaps.geocode(new_df["State"][i])
            else:
                geocode_result = gmaps.geocode(new_df['City'][i] + ", " + new_df["State"][i])
        
            latitude = np.array(geocode_result)[0]['geometry']['location']['lat']
            longitude = np.array(geocode_result)[0]['geometry']['location']['lng']
            lat.append(latitude)
            lng.append(longitude)
    
        new_df['latitude']=lat
        new_df['longitude'] = lng
    else:
        new_df['latitude'] = existing_hate_group_csv['latitude']
        new_df['longitude'] = existing_hate_group_csv['longitude']
    hospital_info=[]
    sub_criteria_info = []
    criteria_info = []
    print(1)
    #scrape(hospital_info = hospital_info,sub_criteria_info = sub_criteria_info)
    final_product_hospital_info = []
    print(len(existing_hospital_csv))
    if(len(existing_hospital_csv)==0):
        for i in df['state']:
            scrape(string_input = i, hospital_info = hospital_info,sub_criteria_info= sub_criteria_info,criteria_info = criteria_info)
    
        print(1)
        split_scrape = []
        for j in range(len(np.array(hospital_info)[1])):
            col = []
            for i in range(len(np.array(hospital_info))):
                if(i%1600==0 and i!=0):
                    print(j)
                if(len(np.array(hospital_info)[i]) == 8):
                    (np.array(hospital_info)[i]).insert(2,"N/A")
                    col.append((np.array(hospital_info))[i][j])
                    split_scrape.append(col)
 
        final_product_hospital_info = pd.DataFrame({"Title":split_scrape[0],"Google Maps URL":split_scrape[1],"Phone Number":split_scrape[2],"Website":split_scrape[3],"Street":split_scrape[4],"Town":split_scrape[5],"State":split_scrape[6],"Zip code":split_scrape[7],"Score":split_scrape[8]})


        final_product_hospital_info['Street']


        final_product_hospital_info['Phone Number'] = final_product_hospital_info['Phone Number'].apply(lambda x: x[4:].strip())


        import math
        for i in range(len(final_product_hospital_info['Zip code'])):
            try:
                b = int(final_product_hospital_info['Zip code'][i])
            except:
                try:
                    final_product_hospital_info['Zip code'][i] = (final_product_hospital_info["Google Maps URL"][i][-10:])
                    int(final_product_hospital_info["Google Maps URL"][i][-10:].split("-")[0])
                except:
                    final_product_hospital_info['Zip code'][i] = (final_product_hospital_info["Google Maps URL"][i][-5:])
                    try:
                        int(final_product_hospital_info["Google Maps URL"][i][-5:])
                    except:
                        final_product_hospital_info['Zip code'][i] = "N/A"

        final_product_hospital_info['Delivery Code'] = final_product_hospital_info['Zip code'].apply(lambda x: np.array(x.split("-"))[1:2])
        final_product_hospital_info['Zip code'] = final_product_hospital_info['Zip code'].apply(lambda x: (np.array(x.split("-"))[:1][0]))


        final_product_hospital_info['Delivery Code'] = (final_product_hospital_info['Delivery Code']).apply(lambda x: x[0] if x.size>0 else math.nan)

        final_product_hospital_info['Street'] = final_product_hospital_info['Street'].apply(str)


        final_product_hospital_info['Street']



        str(final_product_hospital_info['Street'][1655])
    else:
        final_product_hospital_info = existing_hospital_csv
   
    lat = []
    long = []
    if(len(existing_hospital_csv)==0):
    
        
        for i in range(len(final_product_hospital_info)):
            try:
                geocode_result = gmaps.geocode(final_product_hospital_info["Street"][i] + ", " + final_product_hospital_info["Town"][i] + ", " + final_product_hospital_info['State'][i])
                latitude = np.array(geocode_result)[0]['geometry']['location']['lat']
                longitude = np.array(geocode_result)[0]['geometry']['location']['lng']
                lat.append(latitude)
                long.append(longitude)
            except:
                latitude = -1
                longitude = -1
                lat.append(latitude)
                long.append(longitude)

        final_product_hospital_info['latitude'] = lat
        final_product_hospital_info['longitude'] = long

        final_product_hospital_info[final_product_hospital_info['latitude']==-1]

        final_product_hospital_info['latitude'][0] = 33.5066
        final_product_hospital_info['longitude'][0] = -86.8031

        manual_indexes = []
        final_product_hospital_info["Street"][412] = '800 W Central Rd'
        final_product_hospital_info["Town"][412] = 'Arlington Heights'
        final_product_hospital_info["State"][412] = 'IL'
        manual_indexes.append(412)

        final_product_hospital_info["Street"][458] = '1221 S Gear Ave'
        final_product_hospital_info["Town"][458] = 'West Burlington'
        final_product_hospital_info["State"][458] = 'IA'
        manual_indexes.append(458)

        final_product_hospital_info["Street"][496] = '2800 Clay Edwards Dr'
        final_product_hospital_info["Town"][496] = 'North Kansas City'
        final_product_hospital_info["State"][496] = 'MO'
        manual_indexes.append(496)

        final_product_hospital_info["Street"][682] = '2316 S Cedar St'
        final_product_hospital_info["Town"][682] = 'Lansing'
        final_product_hospital_info["State"][682] = 'MI'
        manual_indexes.append(682)

        final_product_hospital_info["Street"][697] = '27351 Dequindre Rd'
        final_product_hospital_info["Town"][697] = 'Madison Heights'
        final_product_hospital_info["State"][697] = 'MI'
        manual_indexes.append(697)

        final_product_hospital_info["Street"][920] = '2 Stone Harbor Blvd'
        final_product_hospital_info["Town"][920] = 'Cape May Court House'
        final_product_hospital_info["State"][920] = 'NJ'
        manual_indexes.append(920)

        final_product_hospital_info["Street"][1151] = '27100 Chardon Rd'
        final_product_hospital_info["Town"][1151] = 'Richmond Heights'
        final_product_hospital_info["State"][1151] = 'OH'
        manual_indexes.append(1151)

        for i in manual_indexes:
            geocode_result = gmaps.geocode(final_product_hospital_info["Street"][i] + ", " + final_product_hospital_info["Town"][i] + ", " + final_product_hospital_info['State'][i])
            latitude = np.array(geocode_result)[0]['geometry']['location']['lat']
            longitude = np.array(geocode_result)[0]['geometry']['location']['lng']
            final_product_hospital_info['latitude'][i] = latitude
            final_product_hospital_info['longitude'][i] = longitude
    
    else:
        final_product_hospital_info['latitude'] = existing_hospital_csv['latitude']
        final_product_hospital_info['longitude'] = existing_hospital_csv['longitude']
    
    for i in sub_criteria_info:
        if(len(i)==3):
            i.append('N/A')
            i.append('N/A')
            i.append('N/A')
        
    if(len(sub_criteria_csv)==0):
        split_scrape = []
        for j in range(len(np.array(sub_criteria_info)[1])):
            col = []
            for i in range(len(np.array(sub_criteria_info))):
                if(i%1600==0 and i!=0):
                    print(j)
                    col.append((np.array(sub_criteria_info))[i][j])
                split_scrape.append(col)
    
        sub_criteria_df = pd.DataFrame({'Patient Non-Discrimination':split_scrape[0],'Visitation Non-Discrimination':split_scrape[1],'Employment Non-Discrimination':split_scrape[2],'Staff Training':split_scrape[3],'Employee Policies and Benefits':split_scrape[4],'Transgender Inclusive Health Insurance':split_scrape[5]})
    else:
        sub_criteria_df = sub_criteria_csv
    if(len(criteria_csv)==0):
        split_scrape = []
        for j in range(len(np.array(criteria_info)[1])):
            col = []
            for i in range(len(np.array(criteria_info))):
                if(i%1600==0 and i!=0):
                    print(j)
                    col.append((np.array(criteria_info))[i][j])
                split_scrape.append(col)
        
        criteria_df = pd.DataFrame({'Non-Discrimination & Staff Training':split_scrape[0],'Patient Services & Support':split_scrape[1],'Employee Benefits & Policies':split_scrape[2],'Patient & Community Engagement':split_scrape[3],'Responsible Citizenship':split_scrape[4]})
    else:
        criteria_df = criteria_csv
    current_year = datetime.now().year
    scores = []
    hate = []
    if(len(hate_group_csv)==0):
        for i in range(len(final_product_hospital_info)):
            print(i)
            score = calculate_complete_score(hrc_score = final_product_hospital_info['Score'][i],
                                 hospital_name = final_product_hospital_info['Title'][i],hospital_latitude = final_product_hospital_info['latitude'][i], 
                                 hospital_longitude = final_product_hospital_info['longitude'][i], 
                                 hate_groups = new_df, max_dist = 50, current_year = current_year, hate_group = hate)
        
            scores.append(score)
        
        scores = np.array(scores)
        hate = np.array(hate)
    
        scores = scores+np.nanmax(abs(scores))
        scores = (scores/np.nanmax(abs(scores)))*100
        final_product_hospital_info['total_score'] = scores
        
        hate_group_df = pd.DataFrame({"Hospital Name":hate[:,0],"hate_group_title":hate[:,1], "ideology":hate[:,2], "latitude":hate[:,3], "longitude":hate[:,4],'haversine':hate[:,5], 'year':hate[:,6]})
    else:
        hate_group_df = hate_group_csv
    score_df = pd.DataFrame({'score':scores})
    score_df.to_csv("score_df.csv")
    #final_product_hospital_info.to_csv('final_product_hospital_info.csv')
    #sub_criteria_df.to_csv('sub_criteria_df.csv')
    #criteria_df.to_csv('criteria_df.csv')
    hate_group_df.to_csv('hate_group_df.csv')
    print(hate)
    return criteria_df, sub_criteria_df, final_product_hospital_info, hate_group_df
