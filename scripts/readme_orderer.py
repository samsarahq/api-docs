import requests
import os

README_CATEGORY_ID = os.getenv('README_CATEGORY_ID')

README_API_TOKEN = os.environ.get('README_API_TOKEN')

class BasicAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["Authorization"] = "Basic " + self.token
        return r

# Read markdown files and store by slug.
slugToBody = {}
markdownFilePath = "./markdown"

files = []
for f in os.listdir(markdownFilePath):
    filePath = os.path.join(markdownFilePath, f)
    if os.path.isfile(filePath):
        files.append(filePath)
        with open(filePath, 'r') as file:
            # Slug is file name, without .md extension.
            slugToBody[f[:-3]] = file.read()

readme_auth = BasicAuth(README_API_TOKEN)

response = requests.get('https://dash.readme.io/api/v1/categories/samsara-api/docs', auth=readme_auth)
response_body = response.json()

slugToDocTitle = {}
tags = []
for doc in response_body:
    slugToDocTitle[doc["slug"]] = doc["title"]
    if "children" in doc and doc["children"] != []:
        tags.append({
            "title": doc["title"],
            "slug": doc["slug"],
        })
        for child in doc["children"]:
            slugToDocTitle[child["slug"]] = child["title"]

tags = sorted(tags, key=lambda x: x["title"])

# Update the markdown docs for all slugs.
print("Updating markdown for all docs...\n")
for slug in slugToBody:
    curSlug = slug
    body = slugToBody[slug]
    if slug not in slugToDocTitle:
        print(slug + " has associated markdown file, but was not found in readme")
        curSlug = slug + "-1"
        if curSlug not in slugToDocTitle:
            continue
    title = slugToDocTitle[curSlug]

    payload = {
        "title": title,
        "category": README_CATEGORY_ID,
        "body": body,
    }

    resp = requests.put("https://dash.readme.io/api/v1/docs/" + curSlug, auth=readme_auth, data=payload)
    print(curSlug + ": " + str(resp.status_code))

# Start at order=1, because overview is at order=0.
order = 1
previewApi = None
betaApi = None
print("Reordering sidebar tags...\n")
for tag in tags:
    if tag["title"] == "Preview APIs":
        previewApi = tag
        continue
    elif tag["title"] == "Beta APIs":
        betaApi = tag
        continue

    payload = {
        "title": tag["title"],
        "category": README_CATEGORY_ID,
        "order": order,
    }
    resp = requests.put("https://dash.readme.io/api/v1/docs/" + tag["slug"], auth=readme_auth, data=payload)
    print(tag["slug"] + ": " + str(resp.status_code))
    order += 1

# Add Beta APIs and Preview APIs at the end.
if betaApi:
    payload = {
        "title": betaApi["title"],
        "category": README_CATEGORY_ID,
        "order": order,
    }
    resp = requests.put("https://dash.readme.io/api/v1/docs/" + betaApi["slug"], auth=readme_auth, data=payload)
    print(betaApi["slug"] + ": " + str(resp.status_code))
    order += 1

if previewApi:
    payload = {
        "title": previewApi["title"],
        "category": README_CATEGORY_ID,
        "order": order,
    }
    resp = requests.put("https://dash.readme.io/api/v1/docs/" + previewApi["slug"], auth=readme_auth, data=payload)
    print(previewApi["slug"] + ": " + str(resp.status_code))
    order += 1
