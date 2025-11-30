# Tanpa Perantara AI Agents

## Overview
This repository contains AI agents for the **Tanpa Perantara** platform, a revolutionary Property Technology Platform that eliminates intermediaries in property transactions. The system utilizes a multi-agent architecture powered by Google's Agent Development Kit (ADK) to provide specialized assistance for different user needs.

## System Architecture

### Multi-Agent System
The platform features two primary agents, each with specialized sub-agents:

1. **Price Recommendation Agent** (Valuation Expert for Buyers) | https://price-recommendation-agent-479525332500.us-central1.run.app
2. **Tata - Tanpa Perantara Assistant** (Property Sales Agent) | https://buyer-assistant-agent-479525332500.us-central1.run.app

Each agent employs a multi-agent architecture with:
- **Root Agent**: Orchestrates the workflow and synthesizes results
- **Database Retrieval Agent**: Queries internal PostgreSQL database for property data
- **Web Search Agent**: Analyzes external market trends and sentiment

## Implementation Details

### 1. Price Recommendation Agent

**Purpose**: Assist buyers in determining fair market value of properties.

**Location**: `price_recomendation/`

**Key Components**:
- `agent.py` - Root agent that coordinates sub-agents
- `prompts.py` - System instructions for all agents
- `sub_agents/database_agent.py` - Database retrieval specialist
- `sub_agents/web_search_agent.py` - Market sentiment analyst
- `api.py` - FastAPI endpoint for external integration

**Workflow**:
1. User provides property specifications (location, area, etc.)
2. Database Agent retrieves comparable properties from PostgreSQL
3. Web Search Agent gathers market trends and external factors
4. Root Agent synthesizes data and outputs JSON with:
   - Recommended price
   - Listing title and description
   - Analysis (internal data, external sentiment, investment potential)
   - Confidence score

**Output Format**:
```json
{
  "price_recommendation": 1500000000,
  "listing_title": "Strategic Investment Property in Prime Location",
  "listing_description": "...",
  "analysis": {
    "internal_data_summary": "...",
    "external_sentiment_summary": "...",
    "investment_potential": "..."
  },
  "confidence_score": 0.85
}
```

### 2. Tata - Property Sales Assistant

**Purpose**: Act as a friendly AI Sales Agent to guide buyers and market properties for sellers.

**Location**: `buyer_assistant/`

**Key Components**:
- `agent.py` - Root agent with sales persona
- `prompts.py` - Conversational instructions and sales strategies
- `sub_agents/database_agent.py` - Property search specialist
- `sub_agents/web_search_agent.py` - Investment advisor

**Workflow**:
1. Tata builds rapport with the user
2. Web Search Agent researches area's investment potential
3. Database Agent finds matching properties
4. Tata presents recommendations with persuasive investment rationale
5. Provides source citations for credibility

**Features**:
- Conversational Indonesian/English interface
- Geocoding for location-based searches
- Investment advice backed by real-time data
- Source citation for transparency

## Technical Stack

### Core Technologies
- **Google ADK (Agent Development Kit)**: Multi-agent orchestration
- **Google Gemini 2.0 Flash**: LLM for agent reasoning
- **PostgreSQL**: Property database
- **MCP Toolbox**: Database tool integration
- **FastAPI**: REST API endpoints
- **Google Cloud Run**: Deployment platform

### Database Schema

**Table: `propertys`**
- `id` (PK), `price`, `longitude`, `latitude`, `address`

**Table: `property_details`**
- `property_id` (FK), `surface_area`, `building_area`, `total_floor`, `total_bedroom`
- Distance fields (in meters): `hospital_distance`, `school_distance`, `market_distance`, `airport_distance`, `police_office_distance`, `train_station_distance`

### Tools Configuration (`tools.yaml`)

**Available Tools**:
1. `get-property-by-id` - Retrieve specific property details
2. `get-all-properties` - List all properties
3. `search-properties-by-coordinates` - Radius-based search (km)
4. `search-properties-by-coordinates-and-price` - Radius + price range search
5. `get-average-price` - Calculate average price within radius (meters)

**Database Connection**: Configured via environment variables in `.env`

### Web Search Strategy

Both agents use trusted domain restrictions for reliable data:
- **Property Data**: `rumah123.com`, `99.co`, `olx.com`
- **Market Trends**: `kontan.co.id`, `bisnis.com`, `katadata.co.id`, `cnbcindonesia.com`
- **Infrastructure**: `pu.go.id`, government sites
- **General News**: Major Indonesian media outlets

Search queries use `site:` operator to ensure data quality and require source citations in outputs.

## Deployment

### Prerequisites
- Google Cloud Project with billing enabled
- APIs enabled: Cloud Run, Artifact Registry
- `gcloud` CLI authenticated
- Python 3.13+ with virtual environment

### Environment Variables

Create `.env` files in each agent directory:

```bash
# Database Configuration
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=tpg_dev
DB_USER=postgres
DB_PASSWORD=your-password

# Toolbox Configuration
TOOLBOX_URL=http://127.0.0.1:5000

# Google Cloud
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

### Deployment Steps

1. **Install Dependencies**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   - Update `deploy.sh` with your project ID and region
   - Set database credentials in `.env` files

3. **Deploy to Cloud Run**:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

The script deploys both agents with web UI to Cloud Run.

### Manual Deployment

For individual agent deployment:

```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=price-recommendation-agent \
  --app_name=price_recomendation \
  --with_ui \
  price_recomendation
```

## Project Structure

```
AI Agent/
├── price_recomendation/          # Price Recommendation Agent
│   ├── agent.py                  # Root agent
│   ├── prompts.py                # Agent instructions
│   ├── api.py                    # FastAPI endpoint
│   ├── requirements.txt          # Python dependencies
│   ├── .env                      # Environment variables
│   └── sub_agents/
│       ├── database_agent.py     # DB retrieval specialist
│       └── web_search_agent.py   # Market analyst
├── buyer_assistant/              # Tata Sales Assistant
│   ├── agent.py                  # Root agent
│   ├── prompts.py                # Sales instructions
│   ├── requirements.txt          # Python dependencies
│   ├── .env                      # Environment variables
│   └── sub_agents/
│       ├── database_agent.py     # Property search
│       └── web_search_agent.py   # Investment advisor
├── tools.yaml                    # Database tools configuration
├── deploy.sh                     # Deployment script
└── README.md                     # This file
```

## Key Features

### Intelligent Property Valuation
- Combines internal comparable sales data with external market sentiment
- Considers infrastructure developments, environmental risks, and facilities
- Provides confidence scores for transparency

### Geocoding & Location Intelligence
- Converts location names to coordinates automatically
- Radius-based property search
- Distance calculations using Haversine formula

### Trusted Data Sources
- Enforces domain restrictions for web searches
- Requires source citations in all outputs
- Lists all sources used in analysis

### Multi-Agent Coordination
- Root agents orchestrate specialized sub-agents
- Database agents handle all data retrieval
- Web search agents provide market context
- Seamless information synthesis

## Testing

### Local Testing
```bash
adk web
```
Access at `http://127.0.0.1:8000`

### Production Testing
After deployment, access the web UI at the Cloud Run service URL provided in deployment output.

## Dependencies

### Price Recommendation Agent
- `google-adk` - Agent framework
- `toolbox-core` - Database tool integration
- `fastapi` - REST API
- `pydantic` - Data validation
- `uvicorn` - ASGI server

### Buyer Assistant Agent
- `google-adk` - Agent framework
- `toolbox-core` - Database tool integration

## License

Proprietary - Tanpa Perantara Platform

## Contact

For questions or support, contact the Tanpa Perantara development team.

---

**Built with Google Agent Development Kit (ADK)**
