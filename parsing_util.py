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
 