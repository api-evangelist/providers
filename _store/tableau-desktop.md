---
aid: tableau-desktop
name: Tableau Desktop
description: APIs and integration points for Tableau Desktop, a data visualization and business intelligence platform from Salesforce. Tableau provides REST APIs, embedding APIs, extension APIs, and SDK tools for building custom visualizations, automating server operations, and extending analytics capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/tableau-desktop/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Analytics
  - Business Intelligence
  - Data Visualization
  - Desktop Application
apis:
  - aid: tableau-desktop:rest-api
    name: Tableau REST API
    description: Manage and interact with Tableau Server and Tableau Cloud resources programmatically including workbooks, data sources, users, and permissions.
    humanURL: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm
    baseURL: https://tableau-server/api/3.22
    tags:
      - Cloud
      - Publishing
      - REST
      - Server
      - Workbooks
    properties:
      - type: Documentation
        url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm
      - type: APIReference
        url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref.htm
      - type: Authentication
        url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_auth.htm
  - aid: tableau-desktop:extensions-api
    name: Tableau Extensions API
    description: Build dashboard extensions that enable users to interact with data from other applications directly in Tableau dashboards.
    humanURL: https://tableau.github.io/extensions-api/
    baseURL: https://tableau.github.io/extensions-api/
    tags:
      - Dashboard
      - Extensions
      - JavaScript
      - Web Components
    properties:
      - type: Documentation
        url: https://tableau.github.io/extensions-api/docs/trex_overview.html
      - type: APIReference
        url: https://tableau.github.io/extensions-api/docs/index.html
      - type: GitHubRepository
        url: https://github.com/tableau/extensions-api
      - type: GettingStarted
        url: https://tableau.github.io/extensions-api/docs/trex_getstarted.html
  - aid: tableau-desktop:hyper-api
    name: Tableau Hyper API
    description: Create, read, update, and delete data in .hyper files for use in Tableau Desktop and Server with high-performance data extract capabilities.
    humanURL: https://tableau.github.io/hyper-db/docs/
    baseURL: https://tableau.github.io/hyper-db/
    tags:
      - Data Extract
      - Database
      - ETL
      - Hyper
      - SQL
    properties:
      - type: Documentation
        url: https://tableau.github.io/hyper-db/docs/
      - type: APIReference
        url: https://tableau.github.io/hyper-db/lang_docs/py/tableauhyperapi.html
      - type: GitHubRepository
        url: https://github.com/tableau/hyper-api-samples
      - type: ReleaseNotes
        url: https://tableau.github.io/hyper-db/docs/releases/
  - aid: tableau-desktop:embedding-api
    name: Tableau Embedding API
    description: Embed Tableau visualizations into web applications using modern web components with v3 of the Embedding API.
    humanURL: https://help.tableau.com/current/api/embedding_api/en-us/index.html
    baseURL: https://help.tableau.com/current/api/embedding_api/
    tags:
      - Embedding
      - Integration
      - JavaScript
      - Web Components
    properties:
      - type: Documentation
        url: https://help.tableau.com/current/api/embedding_api/en-us/index.html
      - type: GitHubRepository
        url: https://github.com/tableau/embedding-api-v3-samples
      - type: Authentication
        url: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_auth.html
  - aid: tableau-desktop:metadata-api
    name: Tableau Metadata API
    description: Discover and query metadata about Tableau content using GraphQL, including workbooks, data sources, flows, and lineage information.
    humanURL: https://help.tableau.com/current/api/metadata_api/en-us/index.html
    baseURL: https://help.tableau.com/current/api/metadata_api/
    tags:
      - Data Governance
      - GraphQL
      - Lineage
      - Metadata
    properties:
      - type: Documentation
        url: https://help.tableau.com/current/api/metadata_api/en-us/index.html
      - type: GettingStarted
        url: https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_start.html
  - aid: tableau-desktop:server-client-python
    name: Tableau Server Client (Python)
    description: Python library that provides a convenient wrapper for the Tableau Server REST API for automation and integration workflows.
    humanURL: https://tableau.github.io/server-client-python/
    baseURL: https://tableau.github.io/server-client-python/
    tags:
      - Automation
      - Python
      - REST API
      - Server
    properties:
      - type: Documentation
        url: https://tableau.github.io/server-client-python/docs/
      - type: APIReference
        url: https://tableau.github.io/server-client-python/docs/api-ref
      - type: GitHubRepository
        url: https://github.com/tableau/server-client-python
common:
  - type: Portal
    url: https://www.tableau.com/developer
  - type: Documentation
    url: https://www.tableau.com/developer/tools
  - type: GettingStarted
    url: https://www.tableau.com/developer/getting-started
  - type: Blog
    url: https://www.tableau.com/about/blog/developers
  - type: Support
    url: https://www.tableau.com/support
  - type: TermsOfService
    url: https://www.tableau.com/tos
  - type: PrivacyPolicy
    url: https://www.tableau.com/privacy
  - type: Training
    url: https://trailhead.salesforce.com/content/learn/modules/tableau-developer-platform/get-started-with-the-tableau-developer-platform
  - type: GitHubOrganization
    url: https://github.com/tableau
  - type: Features
    data:
      - name: REST API Management
        description: Full CRUD operations on Tableau Server and Cloud resources including workbooks, data sources, and users.
      - name: Dashboard Extensions
        description: Build custom interactive extensions that integrate third-party data and functionality into dashboards.
      - name: High-Performance Data Extracts
        description: Create and manage .hyper data extract files with the Hyper API for optimized data loading.
      - name: Embedded Analytics
        description: Embed interactive Tableau visualizations in web applications with modern web components.
      - name: Metadata and Lineage
        description: Query content metadata and data lineage using GraphQL for governance and impact analysis.
      - name: Python Automation
        description: Automate Tableau Server operations with the Python Server Client library.
  - type: UseCases
    data:
      - name: Embedded Analytics
        description: Embed interactive dashboards and visualizations into customer-facing web applications.
      - name: Data Pipeline Automation
        description: Automate data extract creation and refresh workflows using the Hyper API and REST API.
      - name: Content Migration
        description: Migrate workbooks and data sources between Tableau Server environments programmatically.
      - name: Custom Dashboard Extensions
        description: Build write-back forms, custom controls, and third-party integrations as dashboard extensions.
      - name: Data Governance
        description: Track data lineage and content dependencies using the Metadata API for impact analysis.
  - type: Integrations
    data:
      - name: Salesforce
        description: Native integration with Salesforce CRM for embedded analytics and data connectivity.
      - name: Snowflake
        description: High-performance data connectivity with Snowflake cloud data warehouse.
      - name: AWS
        description: Cloud deployment on AWS with S3, Redshift, and Athena data source support.
      - name: Azure
        description: Azure integration with Synapse Analytics, Blob Storage, and Azure Active Directory.
      - name: Python
        description: TabPy server for executing Python scripts in Tableau calculated fields.
      - name: Slack
        description: Collaboration integration for sharing and subscribing to Tableau content in Slack.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
