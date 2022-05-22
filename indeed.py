import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://hk.indeed.com/jobs?q=python&l=Hong%20Kong&from=searchOnHP&vjk=5a7eb95658b08892&limit={LIMIT}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all("a")

    page_jobs_string = soup.find("div", {"id":"searchCountPages"}).text
    page_jobs_string = page_jobs_string[21:] #delete indent before content
    #Get the total number of jobs searched
    jobs_cnt = int(page_jobs_string.replace("Page 1 of ", "").replace(" jobs", "").replace(",", ""))

    #Calculate the start number of the last page
    start_num = jobs_cnt - (jobs_cnt%50)
    last_page = requests.get("https://hk.indeed.com/jobs?q=python&l=Hong%20Kong&from=searchOnHP&vjk=5a7eb95658b08892&limit=50&start={start_num}".format(start_num=start_num))
    last_page_soup = BeautifulSoup(last_page.text, 'html.parser')
    last_pagination = last_page_soup.find("div", {"class":"pagination"})
    max_page = int(last_pagination.find_all("li")[-1].text)

    return max_page

def extract_job(html):
    title = html.find("h2", {"class":"jobTitle"}).find("span", title=True).string
    company = html.find("span", {"class":"companyName"})
    if company is not None:
        company = company.string
    else:
        company = None

    location = html.find("div", {"class":"companyLocation"}).string
    job_id = html.find("h2", {"class":"jobTitle"}).find("a")["data-jk"]
    return {"title":title, "company":company, "location":location, "link":f"https://hk.indeed.com/viewjob?jk={job_id}&q=python&l=Hong+Kong"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class":"cardOutline"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs