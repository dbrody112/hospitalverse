# db_final_project
[12/23/2020]*small update in api.py changing radius to int(radius)

The project shown above uses SQL, ReactJS, Python, and Flask to create an iteractive webapp for those experiencing healthcare discrimination in the LGBTQIA+ community. The webapp is 
called Hospitalverse. The .py files outside of the folders were used to scrape data from the Human Rights Campaign  Healthcare Equality index, the api folder houses the files for flask,
the src folder for ReactJS, and the rest to connect ReactJS and Flask. Also note that for the hospital search section of the webapp you may have to refresh after your search since I send the data to local storage so it could take longer than expected. Another thing to not is that I use the Google Maps API here so you MUST use your own API Key. In multiple sections of the code I have outlined where to place it. It also should be noted that in api.py and filtered_hospitals.js I have placed updates in the form of comments (because they were commited after the morning of 12/15). If there is an update below a line that is similar then it is a replacement. otherwise it is an addition to the code. If these updates are allowed, feel free to run the code with the replacements and additions.


Requirements:

Latest versions of:
<li>python</li>
<li>semantic UI</li>
<li>react-router-dom</li>
<li>react</li>
<li>flask</li>
<li>glob</li>
<li>beautifulsoup</li>
<li>numpy</li>
<li>pandas</li>
<li>bootstrap</li>
<li>sqlalchemy</li>
<li>marshmallow</li>
<li>marshmallow-sqlalchemy</li>
<li>flask-sqlalchemy</li>
<li>passlib</li>
<li>flask jwt extended</li>

__________________________________________________________________________________
<strong>ERD</strong>

![erd](https://user-images.githubusercontent.com/59486373/102302352-e3e9f580-3f26-11eb-8eba-904cac306304.png)

<strong>Search Case:</strong>

![search_form](https://user-images.githubusercontent.com/59486373/102262441-18d35980-3ee1-11eb-8cf5-5c4e1c6b6270.png)
