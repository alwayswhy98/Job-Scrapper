from indeed import get_jobs as get_indeed_jobs
from jobsDB import get_jobs as get_jobsDB_jobs
from save import save_to_file

def start_scrapping(word):
    indeed_jobs = get_indeed_jobs(word)
    jobsDB_jobs = get_jobsDB_jobs(word)
    jobs = indeed_jobs + jobsDB_jobs

    return jobs
#save_to_file(indeed_jobs)