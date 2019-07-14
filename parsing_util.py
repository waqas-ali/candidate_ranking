# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:48:45 2019

@author: Waqas
"""

import json
from collections import namedtuple
import re

class Candidate(object):
    """__init__() functions as the class constructor"""
    def __init__(self, summary=None, organizations=None, skills=None):
        self.summary = summary
        self.organizations = organizations
        self.skills = skills

class Job(object):
    """__init__() functions as the class constructor"""
    def __init__(self, description=None, responsibilities=None, requirements=None, keywords=None):
        self.description = description
        self.responsibilities = responsibilities
        self.requirements = requirements
        self.keywords = keywords
        

def parse_candidate_info(d):
    orgDesc = ''
    skill = ''
    candidate = None;
    
    for x in range(1,7):
        if 'Organization Description '+ str(x) in d:
            orgDesc = orgDesc + ' ' + d['Organization Description ' + str(x)]
    result = [s.strip() for s in d['Skills'].split(',')]
    for r in result:
        inner_result = [y.strip() for y in r.split(':')]
        finner = inner_result[::2] 
        for fi in finner:
            skill = skill + ' ' + fi
    candidate = Candidate(d['Summary'], orgDesc, skill)
    return candidate;
'''
    data = json.loads(candidate_json)
    for d in data:
        for x in range(1,7):
            if 'Organization Description '+str(x) in d:
                orgDesc = orgDesc + ' ' + d['Organization Description '+str(x)]
        result = [s.strip() for s in d['Skills'].split(',')]
        for r in result:
            inner_result = [y.strip() for y in r.split(':')]
            finner = inner_result[::2] 
            for fi in finner:
                skill = skill + ' ' + fi
        candidate = Candidate(d['Summary'], orgDesc, skill)'''
        

def parse_job(job_text, keywords):
    
    myList = [item for item in job_text.split('\n')]
    sl_job = ' '.join(myList)
    
    result = re.search('Job brief(.*)Responsibilities', sl_job)
    
    jobBrief=result.group(1)
    
    result = re.search('Responsibilities(.*)Requirements', sl_job)
    
    resp=result.group(1)
    
    req=sl_job.split("Requirements",1)[1]
    
    job = Job(jobBrief,resp,req,keywords)

    return job;


profile = '''[
 {
   "id": "daniela-perlmutter-498522",
   "Full name": "Daniela (Green) Perlmutter",
   "Email": "danielapg1@gmail.com",
   "Profile url": "https://www.linkedin.com/in/daniela-perlmutter-498522/",
   "First name": "Daniela",
   "Last name": "Perlmutter",
   "Title": "Vice President, Marketing Executive",
   "Avatar": "https://media.licdn.com/dms/image/C4D03AQHCjSmPCvC4ng/profile-displayphoto-shrink_800_800/0?e=1568246400&v=beta&t=nFkJWKPxIUrwsjrbior7pz8ihHcn5_8u39M8Vn89eMg",
   "Location": "Israel",
   "Address": "",
   "Birthday": "",
   "Summary": "Over 15 years of experience in leading marketing groups and driving the business of large multi-billion dollar corporate companies as well as smaller start-up like companies.   Native English speaker with British citizenship i have managed and have been part of international teams harnessing the multicultural attributes to drive innovative marketing strategies.   Out-of-the-box thinker with a clear vision on market dynamics and hands on work ethic,  A strong believer in the power of a team and personable leadership in driving business results and enjoying our day jobs. Curious by nature;  I love learning, and finding interesting correlations to bring new perspectives and fresh thinking into mundane projects.  Highly effective in harnessing internal buy-in, managing cross-organizational teams, as well as profound engagement with partners, analysts and customers' technology and business decision makers.  Strong and broad commercial track record: marketing, venture capital, business development, analyst, and researcher.  Specialties: Business development, business strategy, strategic marketing, market analysis, mergers and acquisitions, hi-tech startup building.  Previous positions outside core marketing include investment management in the venture capital industry, and Economic Consultant to Government ministers and Knesset members, including a short period in the US Congress as an advisor to US Congressman Steve Largent (R:Oklahoma).  Publications: Daniela Green, Internet Policy in Israel, May 2002, IASPS http://www.israeleconomy.org/policystudies/psupdate4eng.pdf For other Economic Policy Commentaries - Google 'Daniela Green'.",
   "Twitter": "",
   "Phone 1": null,
   "Phone 1 type": "",
   "Phone 2": "",
   "Phone 2 type": "",
   "Phone 3": "",
   "Phone 3 type": "",
   "Messenger 1": "",
   "Messenger 1 type": "",
   "Messenger 2": "",
   "Messenger 2 type": "",
   "Messenger 3": "",
   "Messenger 3 type": "",
   "Website 1": "",
   "Website 2": "",
   "Website 3": "",
   "Organization 1": "CyberInt",
   "Organization Title 1": "Vice President",
   "Organization Start 1": "May 2018",
   "Organization End 1": "PRESENT",
   "Organization Description 1": "",
   "Organization Location 1": "",
   "Organization LI URL 1": "https://www.linkedin.com/company/2741671",
   "Organization LI ID 1": 2741671,
   "Organization WWW 1": "",
   "Organization Domain 1": "",
   "Organization 2": "Amdocs",
   "Organization Title 2": "Vice President Global Marketing",
   "Organization Start 2": "Sep 2015",
   "Organization End 2": "PRESENT",
   "Organization Description 2": "Head of global product and solutions marketing",
   "Organization Location 2": "",
   "Organization LI URL 2": "https://www.linkedin.com/company/1539",
   "Organization LI ID 2": 1539,
   "Organization WWW 2": "",
   "Organization Domain 2": "",
   "Organization 3": "Dar Web Marketing",
   "Organization Title 3": "Marketing and business development",
   "Organization Start 3": "2012",
   "Organization End 3": "PRESENT",
   "Organization Description 3": "Business development, product strategy and marketing for small businesses and start up companies in the IT industry.",
   "Organization Location 3": "Israel",
   "Organization LI URL 3": "https://www.linkedin.com/search/results/index/?keywords=Dar%20Web%20Marketing",
   "Organization LI ID 3": null,
   "Organization WWW 3": "",
   "Organization Domain 3": "",
   "Organization 4": "Essence",
   "Organization Title 4": "Vice President, Head of Marketing",
   "Organization Start 4": "2013",
   "Organization End 4": "Aug 2015",
   "Organization Description 4": "",
   "Organization Location 4": "Israel",
   "Organization LI URL 4": "https://www.linkedin.com/search/results/index/?keywords=Essence",
   "Organization LI ID 4": null,
   "Organization WWW 4": "",
   "Organization Domain 4": "",
   "Organization 5": "Tel Aviv - Yafo College",
   "Organization Title 5": "New Venture Financing - teaching assistant",
   "Organization Start 5": "2012",
   "Organization End 5": "less than a year",
   "Organization Description 5": "",
   "Organization Location 5": "Israel",
   "Organization LI URL 5": "https://www.linkedin.com/search/results/index/?keywords=Tel%20Aviv%20-%20Yafo%20College",
   "Organization LI ID 5": null,
   "Organization WWW 5": "",
   "Organization Domain 5": "",
   "Organization 6": "Amdocs",
   "Organization Title 6": "Director, Market Strategy",
   "Organization Start 6": "May 2007",
   "Organization End 6": "2012",
   "Organization Description 6": "",
   "Organization Location 6": "",
   "Organization LI URL 6": "https://www.linkedin.com/company/1539",
   "Organization LI ID 6": 1539,
   "Organization WWW 6": "",
   "Organization Domain 6": "",
   "Organization 7": "Tamir Fishman Ventures",
   "Organization Title 7": "Associate",
   "Organization Start 7": "2005",
   "Organization End 7": "2007",
   "Organization Description 7": "",
   "Organization Location 7": "",
   "Organization LI URL 7": "https://www.linkedin.com/search/results/index/?keywords=Tamir%20Fishman%20Ventures",
   "Organization LI ID 7": null,
   "Organization WWW 7": "",
   "Organization Domain 7": "",
   "Education 1": "Tel Aviv University",
   "Education Degree 1": "MBA",
   "Education FOS 1": "Finance and Business Strategy & Entrepreneurship",
   "Education Grade 1": "",
   "Education Start 1": 2002,
   "Education End 1": 2006,
   "Education Description 1": "",
   "Education 2": "Tel Aviv University",
   "Education Degree 2": "BA",
   "Education FOS 2": "Economics and Communcations",
   "Education Grade 2": "",
   "Education Start 2": 1997,
   "Education End 2": 2000,
   "Education Description 2": "",
   "Education 3": "",
   "Education Degree 3": "",
   "Education FOS 3": "",
   "Education Grade 3": "",
   "Education Start 3": "",
   "Education End 3": "",
   "Education Description 3": "",
   "Skills": "Start-ups : 87, Business Development : 65, Telecommunications : 61, Business Strategy : 52, Product Management : 51, Strategy : 48, Marketing Strategy : 36, Marketing : 30, Mobile Devices : 20, Entrepreneurship : 18, Competitive Analysis : 15, Product Marketing : 12, Go-to-market Strategy : 12, Strategic Planning : 10, Market Analysis : 9, Marketing Management : 9, Mergers & Acquisitions : 9, Business Analysis : 7, Customer Relationship Management (CRM)                                Customer Relationship Management (CRM) : 6, CRM : 5, Cloud Computing : 4, Mergers : 3, Venture Capital : 3, Analysis : 3, International Sales : 3, Analytics : 3, Digital Marketing : 1, Social Media Marketing : 1, Online Marketing : 1, SaaS : 8, Enterprise Software : 6, Strategic Partnerships : 26, Management : 21, Executive Management : 3, Leadership : 1",
   "Followers": 4168,
   "Relationship": 1,
   "Connected at": "January 29, 2019",
   "Industry": "Computer & Network Security",
   "Mutual Count": 247,
   "Mutual": "Alicia Roisman Ismach, Arlene Marom",
   "Mutual 1": "Alicia Ismach",
   "Mutual 2": "Arlene Marom",
   "Interests": "Spencer Rascoff; Tel Aviv University- Recanati - MBA Alumni; Jeff Weiner; Amdocs; TechCrunch; Satya Nadella"
 }
]'''
job = '''Job brief
If you live and breathe marketing, we need to talk. We’re looking for a flexible and versatile marketer who will be responsible for the growth of our inbound sales channels.
Marketing manager responsibilities include tracking and analyzing the performance of advertising campaigns, managing the marketing budget and ensuring that all marketing material is in line with our brand identity. To be successful in this role, you should have hands-on experience with web analytics tools and be able to turn creative ideas into effective advertising projects.
Ultimately, you will help us build and maintain a strong and consistent brand through a wide range of online and offline marketing channels.
Responsibilities
Develop strategies and tactics to get the word out about our company and drive qualified traffic to our front door
Deploy successful marketing campaigns and own their implementation from ideation to execution
Experiment with a variety of organic and paid acquisition channels like content creation, content curation, pay per click campaigns, event management, publicity, social media, lead generation campaigns, copywriting, performance analysis
Produce valuable and engaging content for our website and blog that attracts and converts our target groups
Build strategic relationships and partner with key industry players, agencies and vendors
Prepare and monitor the marketing budget on a quarterly and annual basis and allocate funds wisely
Oversee and approve marketing material, from website banners to hard copy brochures and case studies
Measure and report on the performance of marketing campaigns, gain insight and assess against goals
Analyze consumer behavior and adjust email and advertising campaigns accordingly
Requirements
Demonstrable experience in marketing together with the potential and attitude required to learn
Proven experience in identifying target audiences and in creatively devising and leading across channels marketing campaigns that engage, educate and motivate
Solid knowledge of website analytics tools (e.g., Google Analytics, NetInsight, Omniture, WebTrends)
Experience in setting up and optimizing Google Adwords campaigns
Numerically literate, comfortable working with numbers, making sense of metrics and processing figures with spreadsheets
A sense of aesthetics and a love for great copy and witty communication
Up-to-date with the latest trends and best practices in online marketing and measurement
BSc/MSc degree in Marketing or related field

can = parse_candidate_info(profile);
print(can.summary);
print(can.skills);
print(can.organizations);
jb = parse_job(job);
print(jb.description);
print(jb.requirements);
print(jb.responsibilities);

''' 
 