import requests
from requests.auth import HTTPBasicAuth

# === CONFIGURATION ===
JIRA_DOMAIN = "votre-domaine.atlassian.net"   # ex: openai.atlassian.net
PROJECT_KEY = "ABC"                           # Clé du projet JIRA
EMAIL = "votre.email@example.com"             # Votre email Atlassian
API_TOKEN = "votre_token_api"                 # API token sécurisé

# === JIRA API Endpoint ===
JIRA_API_URL = f"https://{JIRA_DOMAIN}/rest/api/3/search"

# === JQL pour filtrer les User Stories dans le backlog ===
# "issuetype = Story" peut être modifié selon votre workflow
JQL = f'project = {PROJECT_KEY} AND issuetype = Story ORDER BY priority DESC'

# === Requête ===
headers = {
    "Accept": "application/json"
}

params = {
    "jql": JQL,
    "maxResults": 50,      # Modifier si besoin
    "fields": "key,summary,status"
}

response = requests.get(
    JIRA_API_URL,
    headers=headers,
    params=params,
    auth=HTTPBasicAuth(EMAIL, API_TOKEN)
)

# === Résultat ===
if response.status_code == 200:
    data = response.json()
    print(f"🟢 {len(data['issues'])} User Stories trouvées dans le backlog :\n")
    for issue in data["issues"]:
        key = issue["key"]
        summary = issue["fields"]["summary"]
        status = issue["fields"]["status"]["name"]
        print(f"- [{key}] {summary} (Statut: {status})")
else:
    print(f"❌ Erreur {response.status_code} : {response.text}")
