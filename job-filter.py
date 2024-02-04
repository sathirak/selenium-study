import csv

with open('xpress-jobs/xpress-jobs-listings.csv', 'r') as original_file:
    csv_reader = csv.reader(original_file)

    with open('xpress-jobs/filtered-jobs.csv', 'w', newline='') as filtered_file:
        csv_writer = csv.writer(filtered_file)
        csv_writer.writerow(['job', 'job id', 'job title', 'company name', 'job link', 'description'])

        include_keywords = ['software engineer', 'developer']
        exclude_keywords = ['senior', 'manager', 'sse', 'lead', 'architect']

        # Set the filter mode (1, 2, or 3)
        filter_mode = 1

        # Iterate through rows in the original CSV file
        for row in csv_reader:
            if filter_mode == 1:
                # Check if any include keyword is in the job title (case-insensitive) and not in exclude keywords
                if any(keyword.lower() in row[2].lower() for keyword in include_keywords) and not any(exclude_keyword.lower() in row[2].lower() for exclude_keyword in exclude_keywords):
                    csv_writer.writerow(row)
            elif filter_mode == 2:
                # Only check if any exclude keyword is in the job title (case-insensitive)
                if not any(exclude_keyword.lower() in row[2].lower() for exclude_keyword in exclude_keywords):
                    csv_writer.writerow(row)
            elif filter_mode == 3:
                # Only check if any include keyword is in the job title (case-insensitive)
                if any(keyword.lower() in row[2].lower() for keyword in include_keywords):
                    csv_writer.writerow(row)
            else:
                print("Invalid filter mode. Choose 1, 2, or 3.")
