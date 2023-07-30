import json

gcp_auth_key = <<gcp_auth>>

with open('/root/.config/gcloud/application_default_credentials.json', 'w') as outfile:
    json.dump(gcp_auth_key, outfile)