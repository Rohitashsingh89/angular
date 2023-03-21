# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.common.exceptions import TimeoutException
# from bs4 import BeautifulSoup
# import pandas
# import csv
# import re


# driver = webdriver.Edge()
# wait = WebDriverWait(driver, 60)

# names = ()

# ch_links = ()
# phone_numbers = ()
# tele_links = ()
# insta_links = ()

# data_xl = pandas.read_excel('data.xlsx')
# for n in data_xl['Application name']:
#     names += n,

# with open('data.csv', 'w', encoding = 'utf-8', newline = '') as data_file:
#     writer = csv.writer(data_file)
#     writer.writerow(('Channel Name', 'Channel Link', 'Contact Num', 'Telegram Channel', 'Instagram Page'))

# for name in names:
#     print('extracting ', name, '...', sep = '')
#     csv_row = (name,)
#     link_param = '+'.join(name.split())
#     driver.get('https://www.youtube.com/results?search_query={}&sp=EgIQAg%253D%253D'.format(link_param))
#     try:
#         wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'channel-link')))
#     except TimeoutException:
#         ch_links += ' ',
#         phone_numbers += ' ',
#         tele_links += ' ',
#         insta_links += ' ',
#         continue

#     x=driver.find_elements(By.CLASS_NAME, 'channel-link')
#     if len(x) > 0:
#         channel_link = x[0].get_attribute('href')
#         ch_links += channel_link,
#         csv_row += channel_link,
#         driver.get(channel_link + '/about')
#         wait = WebDriverWait(driver, 10)
#         try:
#             wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="description-container"]')))
#             desc = driver.find_element(By.XPATH, '//div[@id="description-container"]').text
#             ph_numbers = re.findall('[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', desc)
#             if len(ph_numbers) > 0:
#                 phone_numbers += ' '.join(ph_numbers),
#                 csv_row += ' '.join(ph_numbers),
#             else:
#                 phone_numbers += ' ',
#                 csv_row += '-',
#         except TimeoutException:
#             phone_numbers += ' ',
#             csv_row += '-',
#             wait = WebDriverWait(driver, 60)
#         wait = WebDriverWait(driver, 10)
#         try:
#             wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="links-container"]')))
#             desc = driver.find_element(By.XPATH, '//div[@id="links-container"]')
#             links_html = desc.get_attribute('innerHTML')
#             soup = BeautifulSoup(links_html, 'html.parser')
#             about_links = soup.find_all('a', class_ = 'yt-simple-endpoint')
#             found_tele = False
#             found_insta = False
#             for l in about_links:
#                 href = l['href']
#                 if 't.me' in href:
#                     driver.get(href)
#                     tele_links += driver.current_url,
#                     csv_row += driver.current_url,
#                     found_tele = True
#                 if 'instagram.com' in href:
#                     driver.get(href)
#                     insta_links += driver.current_url,
#                     csv_row += driver.current_url,
#                     found_insta = True
#             if not found_tele:
#                 tele_links += ' ',
#                 csv_row += '-',
#             if not found_insta:
#                 insta_links += ' ',
#                 csv_row += '-',
#         except TimeoutException:
#             tele_links += ' ',
#             csv_row += '-',
#             insta_links += '-',
#             csv_row += '-',
#             wait = WebDriverWait(driver, 60)
#     else:
#         ch_links += ' ',
#         csv_row += '-',
#     with open('data.csv', 'a', encoding = 'utf-8', newline = '') as data_file:
#         writer = csv.writer(data_file)
#         writer.writerow(csv_row)

# driver.quit()

# data_xl['Channel Link'] = ch_links
# data_xl['Contact Num'] = phone_numbers
# data_xl['Telegram Channel'] = tele_links
# data_xl['Instagram Page'] = insta_links
# data_xl.to_excel('data.xlsx', index = False)

# print('completed!')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas
import csv
import re


driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

names = ()

ch_links = ()
phone_numbers = ()
# tele_links = ()
insta_links = ()
subs_count = ()

data_xl = pandas.read_excel('data.xlsx')
for n in data_xl['Application name']:
    names += n,

with open('data.csv', 'w', encoding = 'utf-8', newline = '') as data_file:
    writer = csv.writer(data_file)
    writer.writerow(('Channel Name', 'Channel Link', 'Contact Num', 'Instagram Page', 'Subscribers'))

subs= '-'

for name in names:
    print('extracting ', name, '...', sep = '')
    csv_row = (name,)
    link_param = '+'.join(name.split())
    driver.get('https://www.youtube.com/results?search_query={}&sp=EgIQAg%253D%253D'.format(link_param))
    try:
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'channel-link')))
    except TimeoutException:
        ch_links += ' ',
        phone_numbers += ' ',
        # tele_links += ' ',
        insta_links += ' ',
        continue

    x=driver.find_elements(By.CLASS_NAME, 'channel-link')
    if len(x) > 0:        
        channel_link = x[0].get_attribute('href')
        ch_links += channel_link,
        csv_row += channel_link,
        driver.get(channel_link + '/about')
        wait = WebDriverWait(driver, 7)
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="description-container"]')))
            subs = driver.find_element(By.XPATH, '//*[@id="subscriber-count"]').text
            subs_count += subs,
            
            desc = driver.find_element(By.XPATH, '//div[@id="description-container"]').text
            ph_numbers = re.findall('[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', desc)
            if len(ph_numbers) > 0:
                phone_numbers += ' '.join(ph_numbers),
                csv_row += ' '.join(ph_numbers),
            else:
                phone_numbers += ' ',
                csv_row += '-',
        except TimeoutException:
            subs = driver.find_element(By.XPATH, '//*[@id="subscriber-count"]').text
            subs_count += subs,
            
            phone_numbers += ' ',
            csv_row += '-',
            wait = WebDriverWait(driver, 10)
        wait = WebDriverWait(driver, 7)
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="links-container"]')))
            desc = driver.find_element(By.XPATH, '//div[@id="links-container"]')
            
            links_html = desc.get_attribute('innerHTML')
            soup = BeautifulSoup(links_html, 'html.parser')
            about_links = soup.find_all('a', class_ = 'yt-simple-endpoint')
            found_tele = False
            found_insta = False
            for l in about_links:
                href = l['href']
                # if 't.me' in href:
                #     driver.get(href)
                #     tele_links += driver.current_url,
                #     csv_row += driver.current_url,
                #     found_tele = True
                if 'instagram.com' in href:
                    driver.get(href)
                    insta_links += driver.current_url,
                    csv_row += driver.current_url,
                    found_insta = True
            # if not found_tele:
            #     tele_links += ' ',
            #     csv_row += '-',
            if not found_insta:
                insta_links += ' ',
                csv_row += '-',
        except TimeoutException:
            # tele_links += ' ',
            csv_row += '-',
            insta_links += '-',
            csv_row += '-',
            wait = WebDriverWait(driver, 10)
    else:
        ch_links += ' ',
        csv_row += '-',
    csv_row += subs,
    with open('data.csv', 'a', encoding = 'utf-8', newline = '') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(csv_row)

driver.quit()

data_xl['Channel Link'] = ch_links
data_xl['Contact Num'] = phone_numbers
# data_xl['Telegram Channel'] = tele_links
data_xl['Instagram Page'] = insta_links
data_xl['Subscribers'] = subs_count
data_xl.to_excel('data.xlsx', index = False)

print('completed!')
