from indeed import get_jobs as get_indeed_jobs
from jobsDB import get_jobs as get_jobsDB_jobs

indeed_jobs = get_indeed_jobs()
jobsDB_jobs = get_jobsDB_jobs()
jobs = indeed_jobs + jobsDB_jobs
print(jobs)