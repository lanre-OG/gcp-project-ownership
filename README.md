## Purpose 

This repository will provide a method to get the project owner information(membership) for all the projects in a given GCP organization and save the information on a Bigquery table. This cript does the following:

- Defines schema and creates a Big query table to store ownership information.
- Retrieves project owner role members and save to bigquery table.


## Prerequisites

### Install Google Client Library
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Install BigQuery Client Library
```
pip install --upgrade google-cloud-bigquery
```

### Install Resource Manager Client
```
pip install google-cloud-resource-manager
```

### Login/Acquire new user credentials to use for Application Default Credentials
```
gcloud auth application-default login
```

## Run Script
```
python3 gcp-project-owner.py 
```

## Reference links
- [Create table query result](https://cloud.google.com/bigquery/docs/tables#creating_a_table_from_a_query_result)
- [Insert row into BQ table](https://github.com/googleapis/python-bigquery/blob/master/samples/table_insert_rows.py).