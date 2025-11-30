---
description: Deploy agents to Google Cloud Run with web UI
---

# Deploy to Cloud Run

This workflow deploys both the Price Recommendation Agent and Buyer Assistant Agent to Google Cloud Run with web UI using the ADK CLI.

## Prerequisites

1. **Google Cloud Project**: Ensure you have a Google Cloud project set up.
2. **Authentication**: Run `gcloud auth login` and `gcloud auth application-default login`.
3. **Enable APIs**: 
   - Enable Cloud Run API: `gcloud services enable run.googleapis.com`
   - Enable Artifact Registry API: `gcloud services enable artifactregistry.googleapis.com`
4. **ADK CLI**: Ensure ADK is installed in your virtual environment.
5. **Set Environment Variables**: Update `deploy.sh` with your project ID and region.

## Steps

1. **Update Configuration**
   
   Edit `deploy.sh` and set your Google Cloud project and region:
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   export GOOGLE_CLOUD_LOCATION="us-central1"
   ```

2. **Review Environment Variables**
   
   Ensure `.env` files in both `price_recomendation` and `buyer_assistant` contain the correct database credentials.

// turbo
3. **Run Deployment Script**
   
   Execute the deployment script:
   ```bash
   ./deploy.sh
   ```

   This script will:
   - Deploy `price_recomendation` agent to Cloud Run with web UI
   - Deploy `buyer_assistant` agent to Cloud Run with web UI

4. **Access Deployed Agents**
   
   After deployment, the script will output the URLs for both agents. Access them via:
   - Price Recommendation Agent: `https://price-recommendation-agent-<hash>-<region>.a.run.app`
   - Buyer Assistant Agent: `https://buyer-assistant-agent-<hash>-<region>.a.run.app`

## Manual Deployment

If you prefer to deploy manually, use the following commands:

**Price Recommendation Agent:**
```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=price-recommendation-agent \
  --app_name=price_recomendation \
  --with_ui \
  price_recomendation
```

**Buyer Assistant Agent:**
```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=buyer-assistant-agent \
  --app_name=buyer_assistant \
  --with_ui \
  buyer_assistant
```

## Testing Deployed Agents

### Using Web UI

Simply navigate to the service URLs provided after deployment. The web UI will be automatically available.

### Using REST API

You can also test using curl:

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d '{"query": "Your test query"}' \
  https://YOUR_SERVICE_URL
```

## Troubleshooting

- **Authentication Issues**: Run `gcloud auth application-default login`
- **API Not Enabled**: Enable Cloud Run API via `gcloud services enable run.googleapis.com`
- **Permission Denied**: Ensure you have the necessary IAM roles (Cloud Run Admin, Service Account User)
- **Database Connection**: Ensure database credentials in `.env` are correct and the database is accessible from Cloud Run
- **Build Failures**: Check that all dependencies are in `requirements.txt` or `pyproject.toml`

## Environment Variables

The deployment will use environment variables from the `.env` files in each agent directory. Make sure these are properly configured before deployment.
