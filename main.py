import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://hk.indeed.com/jobs?q=python&l=Hong%20Kong&from=searchOnHP&vjk=5a7eb95658b08892&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

indeed_pagination = indeed_soup.find("div", {"class":"pagination"})
links = indeed_pagination.find_all("a")

page_jobs_string = indeed_soup.find("div", {"id":"searchCountPages"}).text
page_jobs_string = page_jobs_string[21:] #delete indent before content
#Get the total number of jobs searched
jobs_cnt = int(page_jobs_string.replace("Page 1 of ", "").replace(" jobs", "").replace(",", ""))

#Calculate the start number of the last page
start_num = jobs_cnt - (jobs_cnt%50)
last_page = requests.get("https://hk.indeed.com/jobs?q=python&l=Hong%20Kong&from=searchOnHP&vjk=5a7eb95658b08892&limit=50&start={start_num}".format(start_num=start_num))
last_page_soup = BeautifulSoup(last_page.text, 'html.parser')
last_pagination = last_page_soup.find("div", {"class":"pagination"})
max_page = int(last_pagination.find_all("li")[-1].text)

