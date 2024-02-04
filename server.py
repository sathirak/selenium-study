import subprocess

script_paths = ["xpress-jobs/xpress-jobs.py","xpress-jobs/job-filter.py"]

for script_path in script_paths:

    subprocess.run(["python", script_path]) 