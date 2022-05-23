from indeed import get_jobs as get_indeed_jobs
from jobsDB import get_jobs as get_jobsDB_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
jobsDB_jobs = get_jobsDB_jobs()
jobs = indeed_jobs + jobsDB_jobs
save_to_file(jobs)