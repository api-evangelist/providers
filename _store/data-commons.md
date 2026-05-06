---
aid: data-commons
name: Data Commons
description: Data Commons is an open knowledge graph initiative led by Google that aggregates and harmonizes the world's public data into a single graph, making global statistical data simple to explore, query, and integrate through REST, Python, BigQuery, web component, and MCP interfaces.
type: Topic
xType: topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Commons
  - Knowledge Graph
  - Open Data
  - Public Data
  - Statistics
created: '2026-01-02'
modified: '2026-04-30'
url: https://raw.githubusercontent.com/api-evangelist/data-commons/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: data-commons:rest-v2
    name: Data Commons REST API V2
    description: HTTP REST interface for retrieving statistical observations, exploring the Data Commons knowledge graph, and resolving entities to Data Commons IDs (DCIDs). Returns structured JSON data covering variables, places, and observations.
    humanURL: https://docs.datacommons.org/api/rest/v2/
    tags:
      - Knowledge Graph
      - REST
      - Statistics
    properties:
      - type: Documentation
        url: https://docs.datacommons.org/api/rest/v2/
      - type: API Keys
        url: https://apikeys.datacommons.org
      - type: Reference
        url: https://docs.datacommons.org/api/
  - aid: data-commons:python
    name: Data Commons Python Client
    description: Official Python client library that wraps the Data Commons REST API with native Pandas DataFrame support for analytical workflows and notebook integration.
    humanURL: https://docs.datacommons.org/api/python/v2/
    tags:
      - Pandas
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://docs.datacommons.org/api/python/v2/
      - type: PyPI
        url: https://pypi.org/project/datacommons-client/
  - aid: data-commons:sheets
    name: Data Commons Google Sheets
    description: Custom Google Sheets functions that pull Data Commons statistical data directly into spreadsheets without requiring an API key.
    humanURL: https://docs.datacommons.org/api/sheets/
    tags:
      - Google Sheets
      - Spreadsheets
    properties:
      - type: Documentation
        url: https://docs.datacommons.org/api/sheets/
  - aid: data-commons:web-components
    name: Data Commons Web Components
    description: Drop-in JavaScript/HTML web components for embedding Data Commons charts, maps, rankings, and visualizations in any website.
    humanURL: https://docs.datacommons.org/api/web_components/
    tags:
      - JavaScript
      - Visualization
      - Web Components
    properties:
      - type: Documentation
        url: https://docs.datacommons.org/api/web_components/
  - aid: data-commons:bigquery
    name: Data Commons BigQuery
    description: SQL access to Data Commons through Google BigQuery enabling complex analytical queries and joins with private datasets.
    humanURL: https://docs.datacommons.org/api/bigquery.html
    tags:
      - BigQuery
      - SQL
    properties:
      - type: Documentation
        url: https://docs.datacommons.org/api/bigquery.html
  - aid: data-commons:mcp
    name: Data Commons MCP Server
    description: Model Context Protocol server that lets AI agents query Data Commons conversationally, surfacing variables, places, and observations through natural language tools.
    humanURL: https://docs.datacommons.org/api/mcp/
    tags:
      - AI Agents
      - MCP
      - Natural Language
    properties:
      - type: Documentation
        url: https://docs.datacommons.org/api/mcp/
      - type: API Keys
        url: https://apikeys.datacommons.org
common:
  - url: https://datacommons.org/
    name: Website
    type: Website
    description: Official Data Commons project website.
  - url: https://docs.datacommons.org/
    name: Documentation
    type: Documentation
    description: Full Data Commons documentation portal.
  - url: https://docs.datacommons.org/api/
    name: API Documentation
    type: API Documentation
    description: Programmatic access reference for all Data Commons APIs.
  - url: https://apikeys.datacommons.org
    name: API Keys
    type: API Keys
    description: Self-service portal for requesting Data Commons API keys.
  - url: https://github.com/datacommonsorg
    name: GitHub Organization
    type: GitHub Organization
    description: Data Commons open source organization on GitHub.
  - url: https://blog.datacommons.org/
    name: Blog
    type: Blog
    description: Data Commons project blog with announcements and tutorials.
  - url: vocabulary/data-commons-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Vocabulary of Data Commons knowledge graph concepts.
  - url: json-ld/data-commons-context.jsonld
    name: JSON-LD Context
    type: JSON-LD
    description: JSON-LD context mapping Data Commons concepts to Schema.org.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
