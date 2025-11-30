# Price Recommendation AI Agent

An intelligent property valuation system built with the Google Agent Development Kit (ADK). This system uses a multi-agent architecture to combine internal database retrieval with external market sentiment analysis to provide comprehensive property price recommendations.

## 🏗️ Architecture

The system consists of a Root Agent orchestrating two specialized sub-agents:

1.  **Root Agent (`property_valuation_root_agent`)**:
    - Coordinates the workflow.
    - Synthesizes data from sub-agents.
    - Produces the final JSON recommendation.

2.  **Database Retrieval Agent (`database_retrieval_agent`)**:
    - **Role**: SQL Specialist.
    - **Tool**: `postgres_query_tool`.
    - **Function**: Queries the internal PostgreSQL database (`public.propertys` and `public.property_details`) to find comparable properties and fetch detailed specifications (price, area, facilities distance, etc.).

3.  **Web Search Agent (`web_search_agent`)**:
    - **Role**: Market Analyst.
    - **Tool**: `google_search`.
    - **Function**: Performs web searches to analyze market sentiment, news, and environmental factors (infrastructure, floods, etc.) affecting the property's location.

## 🚀 Features

- **Multi-Agent Collaboration**: Specialized agents for distinct tasks (Data vs. Sentiment).
- **TOON Format Integration**: Uses Token-Oriented Object Notation (TOON) for efficient prompt engineering and schema description.
- **Database Integration**: Direct SQL querying capability for precise internal data retrieval.
- **API Access**: Exposed via FastAPI for easy integration with other systems.

## 🛠️ Prerequisites

- Python 3.10+
- PostgreSQL Database
- Google Cloud Project (for Vertex AI) or Google AI Studio API Key

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://gitlab.com/tanpa-perantara-platform/ai_agent-price_recomendation.git
    cd ai_agent-price_recomendation
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    # Or manually:
    pip install google-adk google-cloud-aiplatform google-generativeai psycopg2-binary fastapi uvicorn
    ```

3.  **Configure Environment**:
    Copy `.env.example` to `.env` and fill in your credentials.
    ```bash
    cp .env.example .env
    ```
    
    Update the following variables in `.env`:
    - `GOOGLE_API_KEY` (or Google Cloud credentials)
    - `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`

## 🏃‍♂️ Usage

### Option 1: Run via API (Recommended)

1.  Start the API server:
    ```bash
    uvicorn api:app --host 0.0.0.0 --port 8000 --reload
    ```

2.  Send a request:
    ```bash
    curl -X POST "http://127.0.0.1:8000/analyze" \
         -H "Content-Type: application/json" \
         -d '{
               "lokasi": "Bintaro Sektor 9",
               "luas_tanah": 120,
               "kamar": 3
             }'
    ```

### Option 2: Run via CLI Script

Run the agent directly in the terminal:
```bash
python agent.py
```

## 📂 Project Structure

```
.
├── agent.py                # Root Agent definition and CLI entry point
├── api.py                  # FastAPI application
├── prompts.py              # Centralized prompts (TOON format)
├── tools/
│   └── database.py         # PostgreSQL tool implementation
├── sub_agents/
│   ├── database_agent.py   # Database retrieval sub-agent
│   └── web_search_agent.py # Web search sub-agent
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
```

## 📝 License

[Add your license here]
