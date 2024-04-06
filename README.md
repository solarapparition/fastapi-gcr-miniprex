# FastAPI on Google Cloud Run Minimal Example

Instructions are for MacOS. Adapt as needed.

## Setup
1. Follow ['Before you begin'](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?skip_cache=true) steps.
  - Note this is just to set up gcloud CLI. You can skip this if you already have it set up.
  - Rest of that page uses Flask. This example uses FastAPI.
2. Clone this repo.
3. `cd` into root directory here.
3. `gcloud run deploy --port 7860`
  - Follow prompts. Take note of `Service name` and `region` used.
  - Port used here must be the same as one used in the Dockerfile, otherwise you get this:
    ```text
    ERROR: (gcloud.run.deploy) Revision '<service-name>' is not ready and cannot serve traffic. The user-provided container failed to start and listen on the port defined provided by the PORT=8080 environment variable. Logs for this revision might contain more information.
    ```

## Test
```bash
SERVICE_NAME: service-name
REGION=us-east1
URL=$(gcloud run services describe $SERVICE_NAME --region $REGION --format 'value(status.url)')
curl -X POST $URL/api/hello  # Should return {"message":"Hello World!"}
```

## References
- Deploying Python Service in GCR: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?skip_cache=true
- Inspiration: https://github.com/sekR4/FastAPI-on-Google-Cloud-Run
- Setting ports in GCR: https://cloud.google.com/run/docs/configuring/services/containers#command-line
- Logs: https://console.cloud.google.com/logs

## Secrets

### Create Secret
1. In terminal:
```bash
echo "SECRET_VALUE" | gcloud secrets create SECRET_NAME \
--replication-policy="automatic" \
--data-file=-
```
2. Add secret access permissions for xxxxxxxxxxxx-compute@developer.gserviceaccount.com. See https://cloud.google.com/run/docs/configuring/services/secrets#access-secret
3. When deploying, add `--update-secrets=ENV_VAR_NAME=SECRET_NAME:VERSION`.
  - Note: for some reason `ENV_VAR_NAME` will get a "\n" appended to it, so might need to strip it when using it in code.

### Secrets References
- Configuring Secrets in GCR: https://cloud.google.com/run/docs/configuring/services/secrets#command-line
- Adding Secret: https://cloud.google.com/secret-manager/docs/create-secret-quickstart#secretmanager-quickstart-gcloud
  - `gcloud secrets create`: https://cloud.google.com/sdk/gcloud/reference/secrets/create
- Secrets Manager: https://console.cloud.google.com/security/secret-manager
