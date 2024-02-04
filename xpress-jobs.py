import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open the CSV file in append mode
with open('xpress-jobs/xpress-jobs-listings.csv', 'a', newline='') as csvfile:

    csv_writer = csv.writer(csvfile)

    # Check if the file is empty, if it is, write the header
    if csvfile.tell() == 0:
        csv_writer.writerow(['job', 'job id', 'job title', 'company name', 'job link', 'description'])

    end_text = 'Your search did not match any records.'

    page_number = 1

    while True:
        driver.get(f"https://xpress.jobs/jobs?page={page_number}&Sectors=30")

        try:
            time.sleep(2)

            job_listings = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[2]/div/section[2]/div/div/div/ul/li')

            if not job_listings:
                print(f"No job listings found on page {page_number}")
                break  # Break out of the loop if no job listings are found

            for index, job_listing in enumerate(job_listings, start=1):

                job_title = job_listing.find_element(By.XPATH, 'div[2]/div[1]/h3').text

                company_name = job_listing.find_element(By.XPATH, 'div[2]/div[1]/div[1]/a/strong').text

                job_description = job_listing.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/section[2]/div/div/div/ul/li[7]/div[2]/div[2]').text

                job_link = job_listing.find_element(By.XPATH, 'a').get_attribute('href')
                
                job_id = job_link.split('/')[-1].split('?')[0]

                # Check if job_id already exists in the CSV
                with open('xpress-jobs/xpress-jobs-listings.csv', 'r') as csvfile_read:
                    csv_reader = csv.reader(csvfile_read)
                    existing_job_ids = [row[1] for row in csv_reader]

                if job_id not in existing_job_ids:
                    csv_writer.writerow([f"job {index + (page_number - 1) * len(job_listings)}", job_id, job_title, company_name, job_link, job_description])

            # Check if the end_text is present on the page
            if end_text in driver.page_source:
                print(f"Reached the end of listings on page {page_number}")
                break

            page_number += 1

        except Exception as e:
            print(f"Error processing job listings on page {page_number}: {e}")

driver.quit()