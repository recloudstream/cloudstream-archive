import requests
import glob
import os

REPO = "recloudstream/cloudstream"
LIMIT = 30
MARKERS = ['<!--begin table-->', '<!--end table-->']

r = requests.get(f"https://api.github.com/repos/{REPO}/commits?per_page={LIMIT}")
commits = {}
for commit in r.json():
    short = commit['sha'][:7]
    commits[short] = commit

for apk in glob.glob("*.apk"):
    sha, _ = apk.split(".")
    if sha not in commits.keys():
        os.remove(apk)