import json
import requests
import os

changelogFile = "../changelog.json"
changelogIndexFile = "../changelog_index.json"
operationIdsFile = "../operation_ids.json"
url = "https://dash.readme.com/api/v1/changelogs"
token = os.environ.get("README_TOKEN")

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
        # TODO expand to add release state changes
        # for new preview API: ditto below
        # for new beta API: ditto below
        # for new GA API: "New API <http method> <route template>: General Availability"

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
    if changelog.operationId is not None:
        details = "[{} {}](ref:{}): {}".format(changelog.method, changelog.route, changelog.operationId, changelog.details)
    else:
        details = "{} {}: {}".format(changelog.method, changelog.route, changelog.details)
    logType = ""
    if changelog.isBreakingChange is True:
        logType = "improved"
        title = "API Version: {}".format(changelog.versionDate)
    if changelog.isInitialRelease is True:
        logType = "added"
        state = "General Availability"
        title = "New API {} {}: {}".format(changelog.method, changelog.route, state) # TODO allow for beta and preview states
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
    return diff

def publishChangelogs(index, changelogs):
    diff = diffChangelogs(index, changelogs)
    operationIds = readPathOperationIds()
    for c in diff:
        k = c.key()
        if c.isDocumentationOnly is True:
            index[k] = "ignored"
            continue
        opKey = "{}__{}".format(c.method.lower(), c.route)
        if opKey in operationIds:
            c.operationId = operationIds[opKey]
        payload = formatChangelog(c)
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 201:
            index[k] = response.json()["_id"]
        else:
            print("got non-200 status code {} from readme for changelog {}".format(response.status_code, k))
    writeChangelogIndexFile(index)
    return

def readPathOperationIds():
    operationIds = {}
    if os.path.isfile(operationIdsFile):
        with open(operationIdsFile, "r") as f:
            o = json.load(f)
            for k,v in o.items():
                s = k.split("__")
                s[1] = s[1].removeprefix("/")
                operationIds["__".join(s)] = v.lower()
    return operationIds

if __name__ == "__main__":
    changelogs = readChangelogFile(changelogFile)
    index = readChangelogIndexFile(changelogIndexFile)
    publishChangelogs(index, changelogs)
