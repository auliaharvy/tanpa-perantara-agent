# Valuation Expert AI

## Overview
The **Valuation Expert AI** is an intelligent agent system designed to provide accurate and comprehensive property price recommendations. It leverages a multi-agent architecture to combine internal database records with external market sentiment analysis.

## Architecture
The system is orchestrated by a **Root Agent** which coordinates two specialized sub-agents:

1.  **Database Retrieval Agent**:
    *   **Role**: SQL Specialist.
    *   **Function**: Queries the internal PostgreSQL database (`tpg_dev`) to find comparable properties based on location, specs, and price.
    *   **Data Sources**: `public.propertys` and `public.property_details`.

2.  **Web Search Agent**:
    *   **Role**: Market Sentiment Analyst.
    *   **Function**: Performs web searches to gather external factors influencing property value.
    *   **Key Insights**: Market trends, infrastructure developments, environmental risks, and nearby facilities.

## Workflow
1.  **Input**: User provides property details (Location, Land Area, etc.).
2.  **Internal Search**: Database Agent finds similar properties and calculates average prices.
3.  **External Analysis**: Web Search Agent gathers news and sentiment about the location.
4.  **Synthesis**: Root Agent combines internal data and external sentiment.
5.  **Output**: A JSON response containing the recommended price, listing details, and a comprehensive analysis.

## Tools & Configuration
The system uses `tools.yaml` to define:
*   **Database Connection**: Connection details for the PostgreSQL database.
*   **SQL Tools**: Pre-defined SQL queries for property retrieval (`get-property-by-id`, `search-properties-by-coordinates`, etc.).

## Usage
The agent is designed to be interacted with via a chat interface or API that supports the defined toolset.
