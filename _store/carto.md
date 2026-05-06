---
aid: carto
name: Carto
description: CARTO is a cloud-native location intelligence platform that lets developers and analysts build spatial applications directly on top of modern data warehouses (BigQuery, Snowflake, Redshift, Databricks). It exposes a Maps API for vector and tileset map data, an SQL API for spatial analytics, a Workflows API for executing no-code spatial pipelines, an Import API for data ingestion, and the Data Observatory for curated third-party spatial datasets — all backed by OAuth access tokens and API access tokens.
type: Index
position: Provider
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Location Intelligence
  - Geospatial
  - Mapping
  - GIS
  - SQL
  - BigQuery
  - Snowflake
  - Data Warehouse
created: '2025-01-08'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/carto/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: carto:maps-api
    name: CARTO Maps API
    description: Serves vector tables, SQL-query-backed tilesets, tileset sources, and raster/H3/quadbin tilesets for visualization in deck.gl, MapLibre, Google Maps, Amazon Location, or Mapbox GL clients.
    humanURL: https://docs.carto.com/carto-for-developers/reference/maps-api-reference
    baseURL: https://gcp-us-east1.api.carto.com
    tags:
      - Maps
      - Tiles
      - Vector
      - Geospatial
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/reference/maps-api-reference
  - aid: carto:sql-api
    name: CARTO SQL API
    description: Executes SQL (including CARTO's spatial functions and analytics extensions) against a connected data warehouse from applications, returning GeoJSON / JSON results for spatial analysis, scoring, and dashboarding.
    humanURL: https://docs.carto.com/carto-for-developers/reference/sql-api-reference
    baseURL: https://gcp-us-east1.api.carto.com
    tags:
      - SQL
      - Analytics
      - Spatial
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/reference/sql-api-reference
  - aid: carto:workflows-api
    name: CARTO Workflows API
    description: Executes visually-designed CARTO Workflows (spatial data pipelines) programmatically, enabling scheduled, CI-driven, or application- triggered spatial analytics runs.
    humanURL: https://docs.carto.com/carto-for-developers/reference/workflows-api-reference
    baseURL: https://gcp-us-east1.api.carto.com
    tags:
      - Workflows
      - Analytics
      - Automation
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/reference/workflows-api-reference
  - aid: carto:import-api
    name: CARTO Import API
    description: Ingests files and URLs (CSV, GeoJSON, Shapefile, etc.) into a user's connected CARTO data warehouse for downstream spatial analysis and mapping.
    humanURL: https://docs.carto.com/carto-for-developers/reference/import-api-reference
    baseURL: https://gcp-us-east1.api.carto.com
    tags:
      - Import
      - Ingestion
      - Data
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/reference/import-api-reference
  - aid: carto:data-observatory
    name: CARTO Data Observatory
    description: Curated catalog of third-party spatial datasets (demographics, POIs, mobility, financial, environmental) accessible via subscription and queryable directly from the customer's cloud data warehouse.
    humanURL: https://docs.carto.com/data-observatory
    tags:
      - Data Catalog
      - Datasets
      - Third-Party Data
    properties:
      - type: Documentation
        url: https://docs.carto.com/data-observatory
  - aid: carto:accounts-api
    name: CARTO Accounts API
    description: Manages CARTO user accounts, organizations, and API access tokens, including OAuth clients used for secure programmatic access.
    humanURL: https://docs.carto.com/carto-for-developers/reference/accounts-api-reference
    baseURL: https://accounts.app.carto.com
    tags:
      - Accounts
      - Authentication
      - OAuth
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/reference/accounts-api-reference
  - aid: carto:deck-gl
    name: CARTO for deck.gl
    description: Client library providing deck.gl layers for CARTO vector, H3, quadbin, raster, and query sources, simplifying application-layer integration with the Maps API.
    humanURL: https://docs.carto.com/carto-for-developers/carto-for-deck.gl
    tags:
      - SDK
      - deck.gl
      - Client Library
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/carto-for-deck.gl
      - type: Repository
        url: https://github.com/CartoDB/deck.gl
  - aid: carto:carto-for-react
    name: CARTO for React
    description: React library of components and hooks for building CARTO-powered location intelligence applications with widgets, filters, and deck.gl map integration.
    humanURL: https://docs.carto.com/carto-for-developers/carto-for-react
    tags:
      - SDK
      - React
      - Client Library
    properties:
      - type: Documentation
        url: https://docs.carto.com/carto-for-developers/carto-for-react
common:
  - type: Website
    url: https://carto.com
  - type: Portal
    name: CARTO Documentation
    url: https://docs.carto.com/
  - type: Developer
    name: CARTO for Developers
    url: https://docs.carto.com/carto-for-developers
  - type: GettingStarted
    url: https://docs.carto.com/getting-started/quickstart-guides
  - type: Authentication
    url: https://docs.carto.com/carto-for-developers/fundamentals/authorization
  - type: FAQ
    url: https://docs.carto.com/faqs
  - type: WhatsNew
    url: https://docs.carto.com/whats-new
  - type: Glossary
    url: https://carto.com/glossary
  - type: Webinars
    url: https://carto.com/webinars
  - type: Blog
    url: https://carto.com/blog
  - type: Partners
    url: https://carto.com/partners
  - type: Pricing
    url: https://carto.com/pricing
  - type: Support
    url: https://docs.carto.com/faqs/support-packages
  - type: Status
    url: https://status.carto.com
  - type: Login
    url: https://auth.carto.com/u/login
  - type: SignUp
    url: https://auth.carto.com/u/signup
  - type: TermsOfService
    url: https://carto.com/legal
  - type: PrivacyPolicy
    url: https://carto.com/privacy
  - type: GitHubOrg
    url: https://github.com/CartoDB
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
