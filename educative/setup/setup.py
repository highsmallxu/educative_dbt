import json
import yaml


def dbt_profile(project_id):
    return {
        "educative": {
            "outputs": {
                "dev": {
                    "dataset": "dbt",
                    "job_execution_timeout_seconds": 300,
                    "job_retries": 1,
                    "location": "US",
                    "method": "oauth",
                    "priority": "interactive",
                    "project": project_id,
                    "threads": 1,
                    "type": "bigquery",
                }
            },
            "target": "dev",
        }
    }


def setup_gcp_auth(path, gcp_auth_key):
    with open(path, "w") as obj:
        json.dump(gcp_auth_key, obj)
    return gcp_auth_key["quota_project_id"]


def setup_dbt_auth(path, project_id):
    with open(path, "w") as outfile:
        yaml.dump(dbt_profile(project_id), outfile, sort_keys=False)


gcp_path = "/root/.config/gcloud/application_default_credentials.json"
dbt_path = "/root/.dbt/profiles.yml"
gcp_auth_key = <<gcp_auth>>
PROJECT_ID = setup_gcp_auth(gcp_path, gcp_auth_key)
setup_dbt_auth(dbt_path, PROJECT_ID)
