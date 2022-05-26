from indeed import get_jobs as get_indeed_jobs
from jobsDB import get_jobs as get_jobsDB_jobs

def start_scrapping(word):
    indeed_jobs = get_indeed_jobs(word)
    jobsDB_jobs = get_jobsDB_jobs(word)
    jobs = indeed_jobs + jobsDB_jobs

    return jobs
