import json
import requests
import os

changelogFile = "./changelog.json"
changelogIndexFile = "./changelog_index.json"
operationIdsFile = "./operation_ids.json"
url = "https://dash.readme.com/api/v1/changelogs"
token = os.environ.get("README_API_TOKEN")

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic {}".format(token)
}

class Changelog():
    def __init__(self, route, method, index, versionDate, description, details, isBreakingChange, isInitialRelease, isDocumentationOnly):
        self.route = route
        self.method = method
        self.index = index
        self.versionDate = versionDate
        self.description = description
        self.details = details
        self.isBreakingChange = isBreakingChange
        self.isInitialRelease = isInitialRelease
        self.isDocumentationOnly = isDocumentationOnly
        self.operationId = None

    def __str__(self):
        return "{} {}: {} index {}\n{}\n{}\nisBreakingChange {}\nisInitialRelease: {}\nisDocumentationOnly: {}\nswagger operation id: {}".format(
            self.method, self.route, self.versionDate, self.index, self.description, self.details, self.isBreakingChange, self.isInitialRelease, self.isDocumentationOnly, self.operationId)

    def key(self):
        return "{}__{}__{}__{}".format(self.route, self.method, self.versionDate, self.index)


def changelogDecoder(obj):
    if "Changelog" in obj:
        c = obj["Changelog"]
        return Changelog(obj["Route"], obj["Method"],c["Index"],c["VersionDate"],c["Description"],c["Details"],c["IsBreakingChange"],c["IsInitialRelease"],c["IsDocumentationOnly"])
    return obj

def formatChangelog(changelog):
    title = "{} {}: {}".format(changelog.method, changelog.route, changelog.description)
    endpoint_ref = "{} {}".format(changelog.method, changelog.route)
    if changelog.operationId is not None:
        endpoint_ref = "[{} {}](ref:{})".format(changelog.method, changelog.route, changelog.operationId)
    details = "The {} has some new features! {}".format(endpoint_ref, changelog.details.replace("<br>","\n"))
    logType = ""
    if changelog.isBreakingChange is True:
        logType = "improved"
        title = "API Version: {}".format(changelog.versionDate)
        details = "We've released a new [version](doc:versioning) of the API. This version updates the behavior of the {}: {}".format(endpoint_ref, changelog.details.replace("<br>","\n"))
    if changelog.isInitialRelease is True:
        logType = "added"
        details = "The {} endpoint is now generally available and fully supported for production :tada:! Check it out and happy coding :computer:.".format(endpoint_ref)
        title = "{} {} (Generally Available)".format(changelog.method, changelog.route)
        if changelog.route.startswith("preview"):
            details = "The {} endpoint is now in the Preview stage. Feel free to send in your comments via our [feedback](https://forms.gle/zkD4NCH7HjKb7mm69) form.  (Note this endpoint should not be used in production until it is made generally available).".format(endpoint_ref)
            title = "New Preview API: {} {}".format(changelog.method, changelog.route)
        elif changelog.route.startswith("beta"):
            details = "The {} endpoint is now in the Beta stage. Feel free to send in your comments via our [feedback](https://forms.gle/zkD4NCH7HjKb7mm69) form.  (Note this endpoint should not be used in production until it is made generally available).".format(endpoint_ref)
            title = "New Beta API: {} {}".format(changelog.method, changelog.route)
    payload = {
        "hidden": True, #TODO remove after testing end-to-end
        "title": title,
        "type": logType,
        "body": details
    }
    return payload

def readChangelogFile(changelog):
    decodedChangelogs = {}
    if os.path.isfile(changelog):
        with open(changelog, "r") as f:
            changelogs = json.load(f)
        for c in changelogs:
            c = changelogDecoder(c)
            decodedChangelogs[c.key()] = c
    return decodedChangelogs

def writeChangelogIndexFile(index):
    indexes = []
    for k,v in index.items():
        indexes.append((k,v))
    if os.path.isfile(changelogIndexFile):
        with open(changelogIndexFile, "w") as f:
            json.dump(sorted(indexes), f)

def writeFirstChangelogIndexFile(changelogs):
    indexes = []
    for k,c in changelogs.items():
       indexes.append((k,"ignored"))
    if os.path.isfile(changelogIndexFile):
        with open(changelogIndexFile, "w") as f:
            json.dump(sorted(indexes), f)

"""
Returns a map of changelog key : public changelog _id | `ignored` for changelogs that existed before we began syncing changelogs.
"""
def readChangelogIndexFile(changelogIndex):
    index = {}
    if os.path.isfile(changelogIndex):
        with open(changelogIndex, "r") as f:
            indexJson = json.load(f)
        for i in indexJson:
            index[i[0]] = i[1]
    return index

"""
Determines which changelogs should be published in this run.
"""
def diffChangelogs(index, changelogs):
    diff = []
    for k,c in changelogs.items():
        if k not in index:
            diff.append(c)
            print("New changelog {}".format(c.key()))
    return diff

def publishChangelogs(index, changelogs):
    diff = diffChangelogs(index, changelogs)
    operationIds = readPathOperationIds()
    for c in diff:
        k = c.key()
        if c.isDocumentationOnly is True:
            print("{} is documentation only changelog, ignoring".format(k))
            index[k] = "ignored"
            continue
        opKey = "{}__{}".format(c.method.lower(), c.route)
        if opKey in operationIds:
            c.operationId = operationIds[opKey]
        payload = formatChangelog(c)
        print("Posting {} changelog".format(k))
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 201:
            index[k] = response.json()["_id"]
        else:
            print("got non-201 status code {} from readme for changelog {}".format(response.status_code, k))
    writeChangelogIndexFile(index)
    return

def readPathOperationIds():
    operationIds = {}
    if os.path.isfile(operationIdsFile):
        with open(operationIdsFile, "r") as f:
            o = json.load(f)
            for k,v in o.items():
                s = k.split("__")
                if s[1].startswith("/"):
                    s[1] = s[1][1:]
                operationIds["__".join(s)] = v.lower()
    return operationIds

if __name__ == "__main__":
    print("Reading changelog...")
    changelogs = readChangelogFile(changelogFile)
    print("Reading changelog index...")
    index = readChangelogIndexFile(changelogIndexFile)
    print("Publishing changelog diff...")
    publishChangelogs(index, changelogs)
