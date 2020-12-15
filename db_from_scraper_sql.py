from sqlalchemy import Column, Integer, String,Date,Float,Numeric
from sqlalchemy import Table, MetaData
meta = MetaData()
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative.api import declared_attr
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine("mysql://root:new_password@localhost/hospitals")
Session = sessionmaker(bind = engine)
session = Session()
from db_scraper import load_data
import pandas as pd

hospital_csv = pd.read_csv("./final_product_hospital_info.csv")
hate_group_csv = pd.read_csv("./hate-groups.csv")
sub_criteria_csv = pd.read_csv("./sub_criteria_df.csv")
criteria_csv = pd.read_csv("./criteria_df.csv")
hate_group_csv = pd.read_csv("./hate_group_df.csv")

criteria_df, sub_criteria_df, final_product_hospital_info,hate_group_df = load_data(existing_hospital_csv = hospital_csv,
                                                                      existing_hate_group_csv = hate_group_csv,
                                                                      sub_criteria_csv = sub_criteria_csv,
                                                                      criteria_csv = criteria_csv,
                                                                      hate_group_csv = hate_group_csv)
def stringCheckNan(x):
    if(x==None or x == float("nan") or x!=x):
        x = 'N/A'
def numCheckNan(x):
    if(x==None or x == float("nan") or x!=x):
        x = -1

@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    @declared_attr
    def __table_args__(cls):
        return {'extend_existing':True}


from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey

class Hospital(Base):
    
    __tablename__ = 'hospital'
    __table_args__ = (
            CheckConstraint('hospital_name IS NOT NULL'),
            CheckConstraint('total_score BETWEEN -1 AND 100'),
            )
    
    zip_code = Column(String(length = 5))
    
    latitude = Column(Float)
    longitude = Column(Float)
    phone_number = Column(String(length = 20))
    hospital_name = Column(String(length=100))
    website = Column(String(length = 200))
    mapsUrl = Column(String(length=200))
    total_score = Column(Float)
    street_address = Column(String(length = 200))
    state = Column(String(length = 10))
    town = Column(String(length = 100))
    hospital_id = Column(Integer,primary_key = True)
    non_discrimination_and_staff_training = Column(String(length = 10))
    sub_patient_non_discrimination = Column(String(length = 10))
    sub_visitation_non_discrimination = Column(String(length = 10))
    sub_employment_non_discrimination = Column(String(length = 10))
    sub_staff_training = Column(String(length = 10))
    patient_services_and_support = Column(String(length = 10))
    employee_benefits_and_policies = Column(String(length = 10))
    sub_employee_policies_and_benefits = Column(String(length = 10))
    sub_transgender_inclusive_health_insurance = Column(String(length = 10))
    patient_and_community_engagement = Column(String(length = 10))
    responsible_citizenship = Column(String(length = 100))
    
class Hate_Groups(Base):
    
    __tablename__ = 'hate_groups'
    
    hospital_name = Column(String(length=100), primary_key = True)
    hate_group_name = Column(String(length = 500))
    ideology = Column(String(length = 100))
    latitude = Column(Float, primary_key = True)
    longitude = Column(Float, primary_key = True)
    distance = Column(Float)
    year = Column(Integer)
    
    
    
   
    



Base.metadata.create_all(engine)




final_product_hospital_info["Zip code"][1689]


#{"Title":split_scrape[0],"Google Maps URL":split_scrape[1],"Phone Number":split_scrape[2],"Website":split_scrape[3],"Street":split_scrape[4],"Town":split_scrape[5],"State":split_scrape[6],"Zip code":split_scrape[7],"Score":split_scrape[8]})
j = 1
for i in range(len(final_product_hospital_info)):
    
    zip_code = final_product_hospital_info["Zip code"][i]
    try:
        zip_code = str(int(zip_code))
    except:
        zip_code = 'N/A'
        
    if(zip_code!=zip_code):
        zip_code = "N/A"
    latitude = final_product_hospital_info["latitude"][i]
    numCheckNan(latitude)
    if(latitude!=latitude):
        latitude = -1
        
    longitude = final_product_hospital_info["longitude"][i]
    if(longitude!=longitude):
        longitude = -1
        
    phone_number = final_product_hospital_info["Phone Number"][i]
    if(phone_number!=phone_number):
       phone_number = 'N/A'
    
    
    
    hospital_name = final_product_hospital_info["Title"][i]
    if(hospital_name!=hospital_name):
       hospital_name = 'N/A'
    
    website = final_product_hospital_info["Website"][i]
    if(website!=website):
       website = 'N/A'
    
    mapsUrl = final_product_hospital_info["Google Maps URL"][i]
    if(mapsUrl!=mapsUrl):
       mapsUrl = 'N/A'
    
    total_score = final_product_hospital_info["total_score"][i]
    numCheckNan(total_score)
    if(total_score!=total_score):
        total_score = -1
    if(str(total_score) == "[]"):
        print(total_score)
        print(1)
        total_score+=1
    
        
    street_address = final_product_hospital_info["Street"][i]
    stringCheckNan(street_address)
    if(street_address!=street_address):
       street_address = 'N/A'
    
    state = final_product_hospital_info["State"][i]
    stringCheckNan(state)
    if(state!=state):
       state = 'N/A'
    
    
    town = final_product_hospital_info["Town"][i]
    if(town!=town):
       town = 'N/A'
    
    non_discrimination_and_staff_training = criteria_df['Non-Discrimination & Staff Training'][i]
    stringCheckNan(non_discrimination_and_staff_training)
    
    if(non_discrimination_and_staff_training!=non_discrimination_and_staff_training):
       non_discrimination_and_staff_training = 'N/A'
    
    
    sub_patient_non_discrimination = sub_criteria_df['Patient Non-Discrimination'][i]
    
    if(sub_patient_non_discrimination!=sub_patient_non_discrimination):
       sub_patient_non_discrimination = 'N/A'
       
    sub_visitation_non_discrimination = sub_criteria_df['Visitation Non-Discrimination'][i]
    
    if(sub_visitation_non_discrimination!=sub_visitation_non_discrimination):
       sub_visitation_non_discrimination = 'N/A'
    
    sub_employment_non_discrimination = sub_criteria_df['Employment Non-Discrimination'][i]
    
    if(sub_employment_non_discrimination!=sub_employment_non_discrimination):
       sub_employment_non_discrimination = 'N/A'
    
    sub_staff_training = sub_criteria_df['Staff Training'][i]
    
    if( sub_staff_training!= sub_staff_training):
        sub_staff_training = 'N/A'
    
    patient_services_and_support = criteria_df['Patient Services & Support'][i]
    
    if( patient_services_and_support!= patient_services_and_support):
        patient_services_and_support = 'N/A'
    
    employee_benefits_and_policies = criteria_df['Employee Benefits & Policies'][i]
    
    if(employee_benefits_and_policies!= employee_benefits_and_policies):
        employee_benefits_and_policies = 'N/A'
    
    sub_employee_policies_and_benefits = sub_criteria_df['Employee Policies and Benefits'][i]
    
    if( sub_employee_policies_and_benefits!= sub_employee_policies_and_benefits):
        sub_employee_policies_and_benefits = 'N/A'
    
    sub_transgender_inclusive_health_insurance = sub_criteria_df['Transgender Inclusive Health Insurance'][i]
    
    if( sub_transgender_inclusive_health_insurance!= sub_transgender_inclusive_health_insurance):
        sub_transgender_inclusive_health_insurance = 'N/A'
    
    patient_and_community_engagement = criteria_df['Patient & Community Engagement'][i]
    
    if( patient_and_community_engagement!= patient_and_community_engagement):
       patient_and_community_engagement= 'N/A'
    
    responsible_citizenship = criteria_df['Responsible Citizenship'][i]
    
    if( responsible_citizenship!= responsible_citizenship):
        responsible_citizenship = 'N/A'
        
    if(total_score<-1 or total_score > 100):
        print(str(total_score))
        total_score=-1
    try:
        session.add(Hospital(zip_code = zip_code,latitude = latitude, longitude = longitude,phone_number = phone_number, hospital_name = hospital_name, website = website, mapsUrl = mapsUrl,total_score = total_score,street_address = street_address,state = state, town = town, hospital_id = j,
                              non_discrimination_and_staff_training = non_discrimination_and_staff_training, sub_patient_non_discrimination = sub_patient_non_discrimination,sub_visitation_non_discrimination = sub_visitation_non_discrimination, 
                             sub_employment_non_discrimination = sub_employment_non_discrimination,sub_staff_training = sub_staff_training,patient_services_and_support=patient_services_and_support,employee_benefits_and_policies=employee_benefits_and_policies,
                             sub_employee_policies_and_benefits = sub_employee_policies_and_benefits, sub_transgender_inclusive_health_insurance=sub_transgender_inclusive_health_insurance,patient_and_community_engagement=patient_and_community_engagement,responsible_citizenship=responsible_citizenship))
    except:
        session.add(Hospital(zip_code = zip_code,latitude = latitude, longitude = longitude, phone_number = phone_number, hospital_name = hospital_name, website = website, mapsUrl = mapsUrl,street_address = street_address,state = state, town = town, hospital_id = j,
                             non_discrimination_and_staff_training = non_discrimination_and_staff_training, sub_patient_non_discrimination = sub_patient_non_discrimination,sub_visitation_non_discrimination = sub_visitation_non_discrimination, 
                             sub_employment_non_discrimination = sub_employment_non_discrimination,sub_staff_training = sub_staff_training,patient_services_and_support=patient_services_and_support,employee_benefits_and_policies=employee_benefits_and_policies,
                             sub_employee_policies_and_benefits = sub_employee_policies_and_benefits, sub_transgender_inclusive_health_insurance=sub_transgender_inclusive_health_insurance,patient_and_community_engagement=patient_and_community_engagement,responsible_citizenship=responsible_citizenship))
    
    k = 0
    for i in [total_score,zip_code, latitude, longitude,phone_number, hospital_name, website,mapsUrl,street_address,state, town,j,
                              non_discrimination_and_staff_training, sub_patient_non_discrimination,sub_visitation_non_discrimination,sub_employment_non_discrimination,sub_staff_training,patient_services_and_support,employee_benefits_and_policies,
                             sub_employee_policies_and_benefits, sub_transgender_inclusive_health_insurance,patient_and_community_engagement,responsible_citizenship]:
        if(i!=i):
            print(j,int(j/len([total_score,zip_code, latitude, longitude,phone_number, hospital_name, website,mapsUrl,street_address,state, town,j,
                              non_discrimination_and_staff_training, sub_patient_non_discrimination,sub_visitation_non_discrimination,sub_employment_non_discrimination,sub_staff_training,patient_services_and_support,employee_benefits_and_policies,
                             sub_employee_policies_and_benefits, sub_transgender_inclusive_health_insurance,patient_and_community_engagement,responsible_citizenship])), i)
        k+=1
            
    j+=1
   
    


session.commit()

uniques = []
for i in range(len(hate_group_df)):
    hospital_name = hate_group_df["Hospital Name"][i]
    stringCheckNan(hospital_name)
    
    hate_group_name = hate_group_df["hate_group_title"][i]
    stringCheckNan(hate_group_name)
    
    ideology = hate_group_df['ideology'][i]
    stringCheckNan(ideology)
    
    latitude = hate_group_df['latitude'][i]
    numCheckNan(latitude)
    
    longitude = hate_group_df['longitude'][i]
    numCheckNan(longitude)
    
    distance = hate_group_df['haversine'][i]
    year = hate_group_df['year'][i]
    
    if((hospital_name, latitude, longitude) not in uniques):
        print((hospital_name, latitude, longitude))
        uniques.append((hospital_name, latitude, longitude))
        session.add(Hate_Groups(hospital_name = hospital_name, hate_group_name = hate_group_name, ideology = ideology,
                            latitude = latitude, longitude = longitude,distance = distance, year = year))
    
session.commit()



def getCriteria(hospital_name):
    if(len(hospital_name)>= 17 and hospital_name[:17] == "Kaiser Permanente"):
        hospital_name = hospital_name[:19] + " " + hospital_name[19:]
    criteria = session.query(Hospital.hospital_name,Hospital.score,Hospital.non_discrimination_and_staff_training,Hospital.sub_patient_non_discrimination,Hospital.sub_visitation_non_discrimination,Hospital.sub_employment_non_discrimination,Hospital.sub_staff_training,Hospital.patient_services_and_support, Hospital.employee_benefits_and_policies, Hospital.sub_employee_policies_and_benefits,Hospital.sub_transgender_inclusive_health_insurance, Hospital.patient_and_community_engagement,Hospital.responsible_citizenship).select_from(Hospital).filter(Hospital.hospital_name == hospital_name).all()
    return pd.DataFrame({"Hospital Name":criteria[0][0],"HRC Total Score": criteria[0][1], "Non-Discrimination & Staff Training Total Score":criteria[0][2],"Patient Non-Discrimination Sub-Score":criteria[0][3],                        'Visitation Non-Discrimination Sub-Score':criteria[0][4],'Employment Non-Discrimination Sub-Score':criteria[0][5],'Staff Training Sub-Score':criteria[0][6],'Patient Services & Support Total Score':criteria[0][7],                        'Employee Benefits & Policies Total Score':criteria[0][8],'Employee Policies and Benefits Sub-Score':criteria[0][9],"Transgender Inclusive Health Insurance Sub-Score":criteria[0][10],                        'Patient & Community Engagement Total Score':criteria[0][11],'Responsible Citizenship Total Score':criteria[0][12]},index=[0])
getCriteria('Kaiser Permanente - Manteca Medical Center')


#note that zip code is a string
#also note that since latitude and longitude are not provided to scrape in the website this is the best filtering that can be done.
def filter_by_state_or_zip(state = None, zip_code = None):
    if(state!= None):
        return session.query(Hospital.hospital_name).select_from(Hospital).filter(Hospital.state == state).all()[0][0]
    elif(zip_code!= None):
        return session.query(Hospital.hospital_name).select_from(Hospital).filter(Hospital.zip_code == str(zip_code)).all()[0][0]



filter_by_state_or_zip(zip_code = "93291")


def getAddress(hospital_name):
    if(len(hospital_name)>= 17 and hospital_name[:17] == "Kaiser Permanente"):
        hospital_name = hospital_name[:19] + " " + hospital_name[19:]
    return session.query(Hospital.street_address,Hospital.town,Hospital.state,Hospital.zip_code).select_from(Hospital).filter(Hospital.hospital_name == hospital_name).all()




getAddress(filter_by_state_or_zip(zip_code = "93291"))

