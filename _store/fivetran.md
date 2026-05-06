---
aid: fivetran
name: Fivetran
description: Fivetran is an automated data integration platform providing pre-built connectors for syncing data from SaaS applications, databases, and APIs into cloud data warehouses. The Fivetran REST API exposes management of users, groups, teams, roles, destinations, connections, transformations, webhooks, certificates, and connector metadata.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Connectors
  - Data Integration
  - Data Pipeline
  - ETL
  - SaaS
  - Unified API
url: https://raw.githubusercontent.com/api-evangelist/fivetran/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: fivetran:fivetran-rest-api
    name: Fivetran REST API
    description: The Fivetran REST API allows programmatic management of all platform resources including users, roles, teams, groups, destinations, connections, webhooks, transformations, transformation projects, certificates, system keys, hybrid deployment agents, log services, private links, proxy agents, and connector metadata. Authentication is performed using a system key.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://fivetran.com/docs/rest-api
    baseURL: https://api.fivetran.com/v1
    tags:
      - Connections
      - Connectors
      - Data Integration
      - Destinations
      - ETL
      - Transformations
      - Webhooks
    properties:
      - type: Documentation
        url: https://fivetran.com/docs/rest-api
      - type: Getting Started
        url: https://fivetran.com/docs/rest-api/getting-started
      - type: Authentication
        url: https://fivetran.com/docs/rest-api/getting-started/system-keys
common:
  - type: Website
    url: https://www.fivetran.com/
  - type: Documentation
    url: https://fivetran.com/docs
  - type: REST API Documentation
    url: https://fivetran.com/docs/rest-api
  - type: GitHub Organization
    url: https://github.com/fivetran
  - type: Features
    data:
      - 'Free: low-volume usage included'
      - 'Paid Connections: $5 base for 1M MAR, tiered declining above'
      - 'Transformations: free under 5K runs, $0.01 above, declining at scale'
      - 'Enterprise: PrivateLink, Hybrid, HIPAA, BAA, audit logs'
      - Annual contracts save up to 22%
      - 500+ pre-built connectors (SaaS, DBs, files, events)
      - 'Destinations: Snowflake, BigQuery, Redshift, Databricks, Postgres, etc.'
      - 'Management API: 600 req/min/account'
      - Sync frequency from 24/day (Free) to 1-minute (Paid)
      - dbt Core integration for transformations
      - Quickstart Data Models
      - Custom connectors via Connector SDK
      - Webhooks for sync events
      - OAuth 2.0 + service accounts
      - PrivateLink, Hybrid Deployment (Enterprise)
      - Customer-managed encryption keys (Enterprise)
    sources:
      - https://www.fivetran.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
