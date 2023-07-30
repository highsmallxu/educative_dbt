import json
import yaml

gcp_auth_key = <<gcp_auth>>

with open('/root/.config/gcloud/application_default_credentials.json', 'w') as outfile:
    json.dump(gcp_auth_key, outfile)
PROJECT_ID = json.load(open("auth.json", "rb"))["quota_project_id"]

profile = {
    "educative": {
        "outputs": {
            "dev": {
                "dataset": "dbt",
                "job_execution_timeout_seconds": 300,
                "job_retries": 1,
                "location": "US",
                "method": "oauth",
                "priority": "interactive",
                "project": PROJECT_ID,
                "threads": 1,
                "type": "bigquery",
            }
        },
        "target": "dev",
    }
}
with open("/root/.dbt/profiles.yml", "w") as outfile:
    yaml.dump(profile, outfile, sort_keys=False)
