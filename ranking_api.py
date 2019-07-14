# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:45:45 2019

@author: Waqas
"""

from flask import Flask, request
from flask_restful import Resource, Api
import parsing_util as pu
import candidate_ranking as cr;

app = Flask(__name__)
api = Api(app)


class Ranking(Resource):
    def post(self):
        jb =  request.get_json(force=True);
   
        job_desc = jb['job_desc'];
        keywords = jb['keywords'];
        profile = jb['profile'];
        
        candidate = pu.parse_candidate_info(profile);
        #print(type(job_desc));
        job = pu.parse_job(job_desc,keywords);
        
        print(candidate.summary);
        print(candidate.skills);
        print(candidate.organizations);
        print(job.description);
        print(job.requirements);
        print(job.responsibilities);
        
        score = cr.rank_candidate(candidate,job);
        
        return score;
    
api.add_resource(Ranking, '/ranking') 


if __name__ == '__main__':
     app.run(port='5000')
