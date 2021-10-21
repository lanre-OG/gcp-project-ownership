# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.cloud import bigquery
from google.cloud import resourcemanager
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# gcloud auth application-default login
credentials = GoogleCredentials.get_application_default()

# Construct a BigQuery client object and cloudresourcemanager service.
client = bigquery.Client()
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "your-project.your_dataset.your_table_name"
schema = [
    bigquery.SchemaField("projectid", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("owner", "STRING", mode="REPEATED"),
]

table = bigquery.Table(table_id, schema=schema)
# Make an API request.
table = client.create_table(table)  
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


get_iam_policy_request_body = {}
request = service.projects().list()
response = request.execute()

for project in response.get('projects', []):
    # TODO: Change code below to process each `project` resource:
    resource = project["projectId"]
    request = service.projects().getIamPolicy(resource=resource, body=get_iam_policy_request_body)
    response = request.execute()
    bindings = response.get('bindings', [])
    for bind in bindings:
        if bind['role'] == "roles/owner":
            print(bind['members'])
            rows_to_insert = [
                                {u"projectid": project, u"owner": bind['members']}
                            ]
            errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
            if errors == []:
                print("New rows have been added.")
            else:
                print("Encountered errors while inserting rows: {}".format(errors))
            # [END bigquery_table_insert_rows]