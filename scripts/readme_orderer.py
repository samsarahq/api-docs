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

readme_auth = BasicAuth(README_API_TOKEN)

response = requests.get('https://dash.readme.io/api/v1/categories/samsara-api/docs', auth=readme_auth)
response_body = response.json()

tags = []
for doc in response_body:
    if "children" not in doc or doc["children"] == []:
        continue
    tags.append({
        "title": doc["title"],
        "slug": doc["slug"],
    })

tags = sorted(tags, key=lambda x: x["title"])

# Start at order=1, because overview is at order=0.
order = 1
previewApi = None
betaApi = None
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
    print(resp.status_code)
    order += 1

# Add Beta APIs and Preview APIs at the end.
if betaApi:
    payload = {
        "title": betaApi["title"],
        "category": README_CATEGORY_ID,
        "order": order,
    }
    resp = requests.put("https://dash.readme.io/api/v1/docs/" + betaApi["slug"], auth=readme_auth, data=payload)
    print(resp.status_code)
    order += 1

if previewApi:
    payload = {
        "title": previewApi["title"],
        "category": README_CATEGORY_ID,
        "order": order,
    }
    resp = requests.put("https://dash.readme.io/api/v1/docs/" + previewApi["slug"], auth=readme_auth, data=payload)
    print(resp.status_code)
    order += 1
