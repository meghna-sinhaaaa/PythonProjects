import time
from GoogleSheetsAPI.login import *
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import logging


def checkurl(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def get_response(url, baseurl):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('--blink-settings=imagesEnabled=false')
    driver_path = os.getcwd()+"/resources/chromedriver.exe"
    s = Service(driver_path)
    driver = webdriver.Chrome(options=op, service=s)
    try:
        driver.get(url)
        #time.sleep(2)
        html = driver.page_source
        driver.quit()
        return html
    except:
        return "wrong"


def isEmail(text):
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    return re.search(email_pattern, text)


def get_emailid(soup, website):
    answer = []
    # print("*"*100)
    # print(website)

    def extract_email(email_input):
        # define the email pattern to match
        href = email_input.get("href")
        #print("checking email in: {}".format(href))
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        match = re.search(pattern, href)
        if match:
            email_id = match.group()
            email_id = re.sub(r'^Mail\s*(to|:)\s*', '', email_id, flags=re.IGNORECASE)
            #print("email id found: {}".format(email_id))
            return email_id
        return None

    a_tags = soup.find_all("a", href=lambda href: href and "mailto:" in href)
    if a_tags != []:
        #email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        for a in a_tags:
            a1 = extract_email(a)
            if a1 is not None:
                answer.append(a1)

    if answer is []:
        p_tags = soup.find_all("p")
        for p in p_tags:
            if isEmail(p.text):
                email_id = extract_email(p)
                if email_id is not None:
                    answer.append(email_id)

    #print("answer here is  {}".format(answer))
    if len(answer)>0:
        return answer
    else:
        return None


def get_contact_page(soup, website):
    contact_links = soup.find_all(lambda tag: tag.name == "a" and "contact" in tag.get("href", ""))

    if len(contact_links) == 0:
        for li_tag in soup.find_all("li"):
            for link in li_tag.find_all(lambda tag: tag.name == "a" and "contact" in tag.get("href", "")):
                contact_links.append(link)
        if len(contact_links) == 0:
            for ul_tag in soup.find_all("ul"):
                for li_tag in ul_tag.find_all("li"):
                    for link in li_tag.find_all(lambda tag: tag.name == "a" and "contact" in tag.get("href", "")):
                        contact_links.append(link)
            if len(contact_links) == 0:
                for ul_tag in soup.find_all("ul"):
                    for div_tag in ul_tag.find_all("div"):
                        for li_tag in div_tag.find_all("li"):
                            for link in li_tag.find_all(lambda tag: tag.name == "a" and "contact" in tag.get("href", "")):
                                contact_links.append(link)
                if len(contact_links) == 0:
                    for div_tag in soup.find_all("div"):
                        for ul_tag in div_tag.find_all("ul"):
                            for li_tag in ul_tag.find_all("li"):
                                for link in li_tag.find_all(lambda tag: tag.name == "a" and "contact" in tag.get("href", "")):
                                    contact_links.append(link)
                    if len(contact_links) == 0:
                        for footer_tag in soup.find_all("footer"):
                            for div_tag in footer_tag.find_all("div"):
                                for ul_tag in div_tag.find_all("ul"):
                                    for li_tag in ul_tag.find_all("li"):
                                        for link in li_tag.find_all(lambda tag: tag.name == "a" and "contact" in tag.get("href", "")):
                                            contact_links.append(link)
    #print("contact links for  {} : \n {} \n".format(website, contact_links))

    if len(contact_links) == 0:
        a_tags_1 = soup.find_all('a', {'title': lambda x: x and 'contact' in x.lower()})
        #print("a_tags_1: {}".format(a_tags_1))
        for a in a_tags_1:
            contact_links.append(a)

    if len(contact_links) == 0:
        a_tags_2 = soup.find_all('a', text=lambda x: x and 'contact' in x.lower())
        #print("a_tags_2: {}".format(a_tags_2))
        for a in a_tags_2:
            contact_links.append(a)

    if len(contact_links) == 0:
        c = soup.find_all(lambda tag: tag.name == "a" and "feedback" in tag.get("href", ""))
        if c is not None:
            for e in c:
                contact_links.append(e)

    # check if each link is a valid URL and belongs to the same domain as the original website
    """for link in contact_links:
        print("checking link : {}".format(link))
        href = link.get('href')
        if not href:
            continue

        print("href recevied: {}".format(href))
        # make sure the link is a valid URL
        if not re.match(r'https?://', href):
            if href[0] == "/" and website[-1] == "/":
                href = website + href[1:]
                print("option 1 found, resulting answer: {}".format(href))
                return href
            elif href[0] != "/" and website[-1] != "/":
                href = website+"/"+href
                print("option 2 found, resulting answer: {}".format(href))
                return href
            else:
                href = website + href
                print("option 3 found, resulting answer: {}".format(href))
                return href
        else:
            print("Matched, resulting answer: {}".format(href))
            return href

        # check if the link belongs to the same domain as the original website
        #if href.startswith(website):
            #return href"""
    contact_links = list(set(contact_links))
    print("Final contact links : {}".format(contact_links))
    for link in contact_links:
        #link = link_c.get("href")
        #print("checking link : {}".format(link))
        href = link.get('href')
        if not href:
            continue
        #print("href recevied: {}".format(href))
        # make sure the link is a valid URL
        if "http" not in href:
            if href[0] == "/" and website[-1] == "/":
                href = website + href[1:]
                #print("option 1 found, resulting answer: {}".format(href))
                return href
            elif href[0] != "/" and website[-1] != "/":
                href = website+"/"+href
                #print("option 2 found, resulting answer: {}".format(href))
                return href
            else:
                href = website + href
                #print("option 3 found, resulting answer: {}".format(href))
                return href
        else:
            #print("Matched, resulting answer: {}".format(href))
            return href

        # check if the link belongs to the same domain as the original website
        #if href.startswith(website):
            #return href

    # if no contact page is found, return None
    return None


def check_submitform(soup, website):
    answer = None
    forms = soup.find_all("form")

    # Check if the form tag has any attributes related to contact
    for form in forms:
        if form.has_attr("action") and "contact" in form["action"].lower():
            answer = website
            break
        elif form.has_attr("name") and "contact" in form["name"].lower():
            answer = website
            break
        elif form.has_attr("method") and "post" in form["method"].lower():
            answer = website
            break
    else:
        answer = None

    return answer


def checkcontactcontainsemail(url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('--blink-settings=imagesEnabled=false')
    driver_path = os.getcwd() + "/resources/chromedriver.exe"
    s = Service(driver_path)
    # driver = webdriver.Chrome(driver_path, options=op, service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(options=op, service=s)
    try:
        driver.get(url)
        resp = driver.page_source
        driver.quit()
    except:
        return None

    if resp == "Error" or resp == "wrong":
        return None
    else:
        soup = BeautifulSoup(resp, "html.parser")
        ans = get_emailid(soup, website)
        #print("ans from contact page : {}".format(ans))
        return ans


def mainmod(website):
    answer = "no contact"
    print("{}".format(website))
    parsed_url = urlparse(website)

    base_url = parsed_url.scheme + "://" + parsed_url.netloc
    #print(base_url)
    resp = get_response(website.strip(), base_url)
    ttype = 0
    if resp == "Error" or resp == "wrong":
        answer = "Error"
    else:
        soup = BeautifulSoup(resp, "html.parser")
        answer = get_emailid(soup, website)
        ttype = 3
        print("answer from get email is : {}".format(answer))
        if answer is None:
            answer1 = get_contact_page(soup, base_url)
            if answer1 is not None:
                #print("Checking the contact page")
                answer2 = checkcontactcontainsemail(answer1)
                if answer2 is None:
                    answer = answer1
                    ttype = 2
                else:
                    answer = answer2
                    ttype = 3
            else:
                answer = answer1
                ttype = 2
            print("answer for contact page: {}".format(answer))
            if answer is None:
                answer = check_submitform(soup, website)
                ttype = 1
                print("answer for submit form: {}".format(answer))

    website = website.strip()
    if answer is not None:
        if not isinstance(answer, list):
            answer = answer.strip()
        else:
            answer_1 = list(set(answer))
            answer = ",".join(answer_1)
    else:
        answer = "no contact"
        ttype = 0
    #print("ans: {}".format(answer))
    return website, answer, ttype


if __name__ == "__main__":
    credential_file = os.getcwd() + "/resources/credentials.json"
    logging.basicConfig(filename=os.getcwd() + "/perf.txt", level=logging.INFO, format="%(asctime)s %(message)s",
                        filemode="w")
    gc = login(credential_file)
    print("gc: {}".format(gc))
    # file_url = input("Enter google sheet url: ")
    file_url = "from url"

    file_url_2 = "to url"

    ws_no = 1

    #gsheet = gc.open_by_url(file_url)
    gsheet = gc.open_by_url(file_url_2)
    print("title:")
    print(gsheet.title)
    print("-------------------------------------")

    # data from sheet 2

    worksheet = gsheet.get_worksheet(ws_no)
    records = worksheet.get_all_records()
    websites = []
    for i, record in enumerate(records):
        t1 = time.perf_counter()
        email = record["Email"]
        website = record["Actual website"]
        last_empty_cell = len(record)
        if email == "":
            w, ans, ttype = mainmod(website)
            """if ans == "Error" or ans == "no contact":
                worksheet.update_cell(i + 2, last_empty_cell, ans)
                time.sleep(1.5)
                worksheet.update_cell(i + 2, last_empty_cell - 3, "-")"""

            if ttype != 0:
                worksheet.update_cell(i + 2, last_empty_cell - ttype, ans)
                if ttype != 3:
                    worksheet.update_cell(i + 2, last_empty_cell - 3, "-")
            else:
                worksheet.update_cell(i + 2, last_empty_cell, "no contact")
                worksheet.update_cell(i + 2, last_empty_cell - 3, "-")
        t2 = time.perf_counter()
        print("time_taken for {}: {}".format(i, t2-t1))

    """print(len(websites))
    print("Removing duplicates")
    web = list(set(websites))
    print(len(web))
    logging.info("len of web : {}".format(web))

    c = len(web) // 5

    #c = 1
    print(c)
    logging.info("num of chunks : {}".format(c))
    url_chunks = [web[i:i + c] for i in range(0, len(web), c)]"""

    """ t3 = time.perf_counter()
    # Create a thread pool with the number of cores available
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(mainmod, [url for url_chunk in url_chunks for url in url_chunk])

    print("Creating data dictionary")
    result_dict = {k: [v, t] for k, v, t in results}
    with open(os.getcwd() + "/dictoutput.json", "a") as f:
        json.dump(result_dict, f)

    t4 = time.perf_counter()"""

    #print("time taken for gathering data: {}".format(t4 - t3))
    #logging.info("time taken for gathering data: {}".format(t4 - t3))
    #print(len(result_dict))

    """with open(os.getcwd() + "/dictoutput.json", "r") as f:
        result_dict = json.load(f)"""

    """gsheet2 = gc.open_by_url(file_url_2)
    worksheet = gsheet2.get_worksheet(ws_no)
    records = worksheet.get_all_records()

    t1 = time.perf_counter()

    for i, record in enumerate(records):
        # if record["Email"] == "":
        email = record["Email"]
        website = record["Actual website"]
        last_empty_cell = len(record)
        if website in result_dict.keys():
            if email == "":
                print("fetching entry no: {}".format(i))
                ans = result_dict[website][0]
                ttype = result_dict[website][1]
                ans = str(ans)
                print("adding : {}".format(ans))
                if ans == "Error" or ans == "no contact":
                    worksheet.update_cell(i + 2, last_empty_cell, ans)
                    time.sleep(1.5)
                    worksheet.update_cell(i + 2, last_empty_cell - 3, "-")

                if ttype!=0:
                    worksheet.update_cell(i + 2, last_empty_cell - ttype, ans)
                    time.sleep(1.5)
                    if ttype!=3:
                        worksheet.update_cell(i + 2, last_empty_cell - 3, "-")
                else:
                    worksheet.update_cell(i + 2, last_empty_cell, "no contact")
                    time.sleep(1.5)
                    worksheet.update_cell(i + 2, last_empty_cell - 3, "-")

                
    t2 = time.perf_counter()

    print("time to update sheet: {}".format(t2 - t1))
    logging.info("time taken for gathering data: {}".format(t2 - t1))"""



