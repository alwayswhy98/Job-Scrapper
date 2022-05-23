from matplotlib.backend_bases import LocationEvent
import requests
from bs4 import BeautifulSoup

URL = f"https://hk.jobsdb.com/hk/search-jobs/quant/1"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    search_result_bar = soup.find("div", {"data-automation":"searchResultBar"})
    search_result = search_result_bar.find("span").text
    total_jobs = int(search_result.replace("1-30 of ","").replace(",","").replace(" jobs",""))
    max_page = int(total_jobs/30) + 1

    return max_page

def extract_job(html):
    title = html.find("h1", {"class":"sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvca"}).string
    company = html.find("span", {"class":"sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _18qlyvca"}).string

    if html.find("span", {"class":"sx2jih0 zcydq84u zcydq80 iwjz4h0"}):
        location = html.find("span", {"class":"sx2jih0 zcydq84u zcydq80 iwjz4h0"}).string
    else:
        location = "None"
    link =  "https://hk.jobsdb.com" + html.find("a", {"class":"_1hr6tkx5 _1hr6tkx8 _1hr6tkxb sx2jih0 sx2jihf zcydq8h"})["href"]

    return {"title":title, "company":company, "location":location, "link":link}

def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page+1):
        print(f"Scrapping jobsDB page {page}")
        result = requests.get("https://hk.jobsdb.com/hk/search-jobs/quant/{page}".format(page=page))
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class":"sx2jih0 zcydq876 zcydq866 zcydq896 zcydq886 zcydq8n zcydq856 zcydq8f6 zcydq8eu"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs