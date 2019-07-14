# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 01:46:56 2019

@author: Waqas
"""
import spacy;
from fuzzywuzzy import fuzz;

def rank_candidate(candidate, job):
    
    nlp = spacy.load('en_core_web_sm');
    
    score1 = description_score(nlp,candidate.summary,job.description);
#    print("Description Score :",score1);
    
    
    score2 = experience_score(nlp,candidate.organizations , job.responsibilities);
#    print("Experience Score :",score2);

    score3 = skills_score(nlp,candidate.skills,job.keywords);
#    print("Skills Score :",score3);

    score4 = requirement_score(nlp, candidate.summary + candidate.organizations , job.requirements);
#    print("Description Score :",score4);
    
    total_score = max(score1, score2 , score3 , score4);
    
    return total_score;
    
def description_score(nlp, profile_desc, job_desc):
    
    if profile_desc is None or profile_desc == '':
        return 0;
    
    profile = nlp(profile_desc);
    job = nlp(job_desc);
    
    candidate_pos = ['NOUN']
    profile_words = [];
    
    
    for sent in profile.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                profile_words.append(token.text);
    
    profile_set = set(profile_words);
    
    job_words = [];
    
    for sent in job.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                job_words.append(token.text)
        
    job_set = set(job_words);
    
    profile_str = " ".join(profile_set);
    job_str = " ".join(job_set);

    print(profile_str)
    print(job_str)
    score = fuzz.ratio(profile_str, job_str)

    return score;
    

def requirement_score(nlp, full_profile, requirements):
    if full_profile is None or full_profile == '':
        return 0;
    
    profile = nlp(full_profile);
    job = nlp(requirements);
    
    candidate_pos = ['NOUN']
    profile_words = [];

    for sent in profile.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                profile_words.append(token.text)
    
    profile_set = set(profile_words);
    
    job_words = [];
    
    for sent in job.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                job_words.append(token.text)
        
    job_set = set(job_words);   
    
    profile_str = " ".join(profile_set);
    job_str = " ".join(job_set);

    print(profile_str)
    print(job_str)
    score = fuzz.ratio(profile_str, job_str)

    return score;
    
def experience_score(nlp, experience, responsibilites):
    if experience is None or experience == '':
        return 0;
    
    profile = nlp(experience);
    job = nlp(responsibilites);
    
    candidate_pos = ['NOUN']
    profile_sentences = [];
    profile_words = [];

    for sent in profile.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                profile_words.append(token.text)
        profile_sentences.append(set(profile_words))
    
    
    profile_set = set(profile_words);
    
    job_words = [];
    
    for sent in job.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                job_words.append(token.text)
        
    job_set = set(job_words);   
    
    profile_str = " ".join(profile_set);
    job_str = " ".join(job_set);

    print(profile_str)
    print(job_str)
    
    score = fuzz.ratio(profile_str, job_str)

    return score;

def skills_score(nlp, skills, keywords):
    if skills is None or skills == '':
        return 0;
    
    profile = nlp(skills);
    job = nlp(keywords);
    
    candidate_pos = ['NOUN']
    profile_sentences = [];
    profile_words = [];

    for sent in profile.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                profile_words.append(token.text)
        profile_sentences.append(set(profile_words))
    
    profile_set = set(profile_words);
    
    job_words = [];
    
    for sent in job.sents: 
        for token in sent:
            if token.pos_ in candidate_pos and token.is_stop is False:
                job_words.append(token.text)
        
    job_set = set(job_words);   
    
    profile_str = " ".join(profile_set);
    job_str = " ".join(job_set);

    print(profile_str)
    print(job_str)
    
    score = fuzz.ratio(profile_str, job_str)

    return score;