#!/bin/bash

# Deployment script for Tanpa Perantara AI Agents to Cloud Run
# This script deploys both price_recomendation and buyer_assistant agents with web UI

# Set your Google Cloud project and region
export GOOGLE_CLOUD_PROJECT="adk-handson-auliaharvy"
export GOOGLE_CLOUD_LOCATION="us-central1"

# Activate virtual environment
source .venv/bin/activate

echo "Setting up Google Cloud project..."
gcloud config set project $GOOGLE_CLOUD_PROJECT

echo ""
echo "=== Deploying Price Recommendation Agent ==="
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=price-recommendation-agent \
  --app_name=price_recomendation \
  --with_ui \
  price_recomendation

echo ""
echo "=== Deploying Buyer Assistant Agent (Tata) ==="
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=buyer-assistant-agent \
  --app_name=buyer_assistant \
  --with_ui \
  buyer_assistant

echo ""
echo "Deployment complete!"
echo "Your agents are now running on Cloud Run with web UI."
echo "Check the output above for the service URLs."
