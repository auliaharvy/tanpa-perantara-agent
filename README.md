# Tanpa Perantara AI Agents

## Overview
This repository houses the AI agents for the **Tanpa Perantara** platform. The system utilizes a multi-agent architecture to provide specialized assistance for different user needs, featuring two primary agents:

1.  **Price Recommendation Agent** (Buyer Support)
2.  **Tata - Tanpa Perantara Assistant** (Seller/Sales Support)

---

## 1. Price Recommendation Agent
**Goal:** Assist buyers in determining the fair market value of a property.

This agent acts as a **Valuation Expert**. It combines internal property data with external market sentiment to provide a comprehensive price analysis.

### Architecture
*   **Root Agent**: Coordinates the analysis.
*   **Database Retrieval Agent**: Queries the internal PostgreSQL database (`tpg_dev`) for comparable properties.
*   **Web Search Agent**: Analyzes external market trends, infrastructure news, and environmental factors.

### Workflow
1.  **Input**: User provides property specs (Location, Area, etc.).
2.  **Analysis**: The agent retrieves similar properties and scans the web for factors affecting value (e.g., new toll roads, flood risks).
3.  **Output**: A recommended price range with a detailed justification and confidence score.

---

## 2. Tata - Tanpa Perantara Assistant
**Goal:** Act as a Property Sales Agent to assist sellers and guide potential buyers.

**Tata** is a friendly and professional AI Sales Agent designed to build rapport with users and guide them towards a purchase. While it interacts with buyers, it serves the seller's interest by effectively marketing properties.

### Architecture
*   **Persona**: Friendly, professional, and persuasive.
*   **Database Retrieval Agent**: Finds properties matching user criteria.
*   **Web Search Agent**: Provides "point of view" and investment advice based on real-time market data.

### Workflow
1.  **Contextualize**: Tata researches the area's investment potential using the Web Search Agent.
2.  **Retrieve**: Finds properties in the database that match the user's needs.
3.  **Recommend & Persuade**: Presents the best options and explains *why* they are good investments, citing external sources (news, trends) to build trust.

---

## Technical Configuration
The agents share a common toolset defined in `tools.yaml`:
*   **Database**: PostgreSQL connection to `tpg_dev`.
*   **Tools**:
    *   `get-property-by-id`
    *   `search-properties-by-coordinates`
    *   `search-properties-by-coordinates-and-price`
