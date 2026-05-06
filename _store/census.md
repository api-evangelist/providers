---
aid: census
url: https://raw.githubusercontent.com/api-evangelist/census/refs/heads/main/apis.yml
name: Census
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Connectors
  - Data Activation
  - Data Warehouse
  - Destinations
  - Fivetran Activations
  - Reverse ETL
  - Unified API
created: '2026-03-27'
modified: '2026-04-23'
specificationVersion: '0.19'
description: Census is a reverse ETL and data activation platform that syncs data from cloud data warehouses (Snowflake, BigQuery, Databricks, Redshift) into operational SaaS applications. Census was acquired by Fivetran and is now branded as Fivetran Activations, offering a REST API for managing workspaces, datasets, syncs, destinations, and custom destinations, plus embedded Activations (Connect Links) for Powered by Fivetran use cases.
apis:
  - aid: census:census-activations-api
    name: Census Activations REST API
    tags:
      - Data Activation
      - REST
      - Reverse ETL
    humanURL: https://fivetran.com/docs/activations/rest-api/api-reference/introduction
    properties:
      - url: https://fivetran.com/docs/activations/rest-api/api-reference/introduction
        type: Documentation
      - url: https://docs.getcensus.com/
        type: LegacyDocumentation
      - url: https://docs.getcensus.com/basics/getting-started
        type: GettingStarted
    description: The Census Activations REST API (formerly Census Management API) lets teams programmatically manage reverse ETL pipelines, sources, models, destinations, syncs, and sync runs. The API is region-scoped and authenticated with personal access tokens, with organization-level resources (workspaces, users, invitations) and workspace-level resources (datasets, destinations, syncs).
  - aid: census:census-custom-destinations-api
    name: Census Custom Destinations API
    tags:
      - Custom Destinations
      - Destinations
      - Integration
    humanURL: https://fivetran.com/docs/activations/rest-api/custom-destinations/destination-spec
    properties:
      - url: https://fivetran.com/docs/activations/rest-api/custom-destinations/destination-spec
        type: Documentation
    description: Custom Destinations API lets partners declare the type of data a destination can process, the operations allowed on that data, and the loading mechanism so that Activations can orchestrate loads into any custom SaaS or application system.
  - aid: census:census-connect-links-api
    name: Census Connect Links (Powered by Fivetran)
    tags:
      - Embedded
      - Connect Links
      - Powered by Fivetran
    humanURL: https://fivetran.com/docs/activations/rest-api/activations-in-powered-by-fivetran/features/connect-links/connect-links
    properties:
      - url: https://fivetran.com/docs/activations/rest-api/activations-in-powered-by-fivetran/features/connect-links/connect-links
        type: Documentation
      - url: https://fivetran.com/docs/activations/rest-api/embedded
        type: Overview
    description: Connect Links enable embedded Activations flows for Powered by Fivetran partners, letting end users configure destinations and syncs from within a host application via hosted URLs.
common:
  - type: Website
    url: https://www.getcensus.com/
  - type: Documentation
    url: https://fivetran.com/docs/activations/
  - type: Reference
    url: https://fivetran.com/docs/activations/rest-api/api-reference/introduction
  - type: GettingStarted
    url: https://docs.getcensus.com/basics/getting-started
  - type: Parent Company
    url: https://www.fivetran.com/
  - type: GitHub
    url: https://github.com/sutrolabs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
