---
aid: tableau
url: https://raw.githubusercontent.com/api-evangelist/tableau/refs/heads/main/apis.yml
apis:
- name: Tableau REST API
  description: The Tableau REST API allows you to manage and change Tableau Server, Tableau Cloud site, and Tableau Prep Conductor resources programmatically, using HTTP.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm
  baseURL: https://[server]/api/[api-version]
  tags:
  - Data Sources
  - REST
  - Server Management
  - Sites
  - Workbooks
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm
  - type: OpenAPI
    url: openapi/tableau-rest-api-openapi.yml
  - type: JSONSchema
    url: json-schema/tableau-workbook-schema.json
  - type: JSONLD
    url: json-ld/tableau-context.jsonld
  - type: Authentication
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_auth.htm
  - type: Versioning
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm
  - type: Change Log
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_whats_new.htm
  - type: Getting Started
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_get_started_tutorial_part_1.htm
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/salesforce-developers/collection/x06mp2m/tableau-apis
  - type: GitHub
    url: https://github.com/tableau/rest-api-samples
  - type: Reference
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref.htm
  - type: OpenAPI Endpoints
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/TAG/index.html
  - type: Samples
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_samples.htm
  - type: SDKs
    url: https://tableau.github.io/server-client-python/
- name: Tableau Metadata API
  description: GraphQL-based API for querying metadata about Tableau content, data sources, and lineage information.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/metadata_api/en-us/index.html
  baseURL: https://[server]/api/metadata/graphql
  tags:
  - Data Catalog
  - GraphQL
  - Lineage
  - Metadata
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/metadata_api/en-us/index.html
  - type: Reference
    url: https://help.tableau.com/current/api/metadata_api/en-us/reference/index.html
  - type: Samples
    url: https://help.tableau.com/current/api/metadata_api/en-us/docs/use-cases.html
  - type: Getting Started
    url: https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_start.html
  - type: Authentication
    url: https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_auth.html
  - type: Change Log
    url: https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_release_notes.html
  - type: GitHub
    url: https://github.com/tableau/metadata-api-samples
- name: Tableau Hyper API
  description: API for creating, reading, and updating Hyper files, which are the data files that power Tableau extracts.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/hyper_api/en-us/index.html
  baseURL: https://github.com/tableau/hyper-api-samples
  tags:
  - Data Files
  - ETL
  - Extracts
  - Hyper
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/hyper_api/en-us/index.html
  - type: GitHub
    url: https://github.com/tableau/hyper-api-samples
  - type: Python Documentation
    url: https://help.tableau.com/current/api/hyper_api/en-us/reference/py/index.html
  - type: Java Documentation
    url: https://help.tableau.com/current/api/hyper_api/en-us/reference/java/index.html
  - type: Getting Started
    url: https://www.tableau.com/developer/learning/tableau-hyper-api
  - type: Installation
    url: https://tableau.github.io/hyper-db/docs/installation/
  - type: Change Log
    url: https://tableau.github.io/hyper-db/docs/releases/
- name: Tableau Embedding API
  description: JavaScript API for embedding Tableau visualizations in web applications with advanced interaction capabilities.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/embedding_api/en-us/index.html
  baseURL: https://[server]
  tags:
  - Embedding
  - JavaScript
  - Visualization
  - Web Components
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/embedding_api/en-us/index.html
  - type: Tutorial
    url: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_get_started.html
  - type: Reference
    url: https://help.tableau.com/current/api/embedding_api/en-us/reference/index.html
  - type: Migration Guide
    url: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_migrate.html
  - type: Authentication
    url: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_auth.html
  - type: Change Log
    url: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_release_notes.html
  - type: GitHub
    url: https://github.com/tableau/embedding-api-v3-samples
  - type: npm
    url: https://www.npmjs.com/package/@tableau/embedding-api
- name: Tableau Document API
  description: Python library for programmatically updating Tableau workbook and data source files.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://tableau.github.io/document-api-python/
  baseURL: https://github.com/tableau/document-api-python
  tags:
  - Automation
  - Data Sources
  - Python
  - Workbooks
  properties:
  - type: Documentation
    url: https://tableau.github.io/document-api-python/
  - type: GitHub
    url: https://github.com/tableau/document-api-python
  - type: PyPI
    url: https://pypi.org/project/tableaudocumentapi/
  - type: Getting Started
    url: https://tableau.github.io/document-api-python/docs/
  - type: Reference
    url: https://tableau.github.io/document-api-python/docs/api-ref
- name: Tableau Server Client (Python)
  description: Python library that wraps the Tableau REST API for easier programmatic access.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://tableau.github.io/server-client-python/
  baseURL: https://github.com/tableau/server-client-python
  tags:
  - Python
  - REST
  - SDK
  - Wrapper
  properties:
  - type: Documentation
    url: https://tableau.github.io/server-client-python/
  - type: GitHub
    url: https://github.com/tableau/server-client-python
  - type: PyPI
    url: https://pypi.org/project/tableauserverclient/
  - type: Samples
    url: https://tableau.github.io/server-client-python/docs/samples
  - type: Reference
    url: https://tableau.github.io/server-client-python/docs/api-ref
  - type: Getting Started
    url: https://tableau.github.io/server-client-python/docs/
  - type: Change Log
    url: https://github.com/tableau/server-client-python/blob/master/CHANGELOG.md
- name: Tableau Extensions API
  description: The Tableau Extensions API allows developers to create dashboard extensions and viz extensions that users can interact with directly in Tableau, enabling integration with other applications and custom visualization types.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://tableau.github.io/extensions-api/docs/
  baseURL: https://[server]
  tags:
  - Dashboard Extensions
  - Extensibility
  - JavaScript
  - Viz Extensions
  - Web Components
  properties:
  - type: Documentation
    url: https://tableau.github.io/extensions-api/docs/
  - type: GitHub
    url: https://github.com/tableau/extensions-api
  - type: Getting Started
    url: https://tableau.github.io/extensions-api/docs/dashext/trex_getstarted/
  - type: Reference
    url: https://tableau.github.io/extensions-api/docs/trex_tableau_viz_ref/
  - type: Change Log
    url: https://tableau.github.io/extensions-api/docs/trex_release-notes/
  - type: Samples
    url: https://tableau.github.io/extensions-api/docs/dashext/trex_examples/
  - type: Installation
    url: https://tableau.github.io/extensions-api/docs/installation/
- name: Tableau Web Data Connector
  description: The Tableau Web Data Connector (WDC) provides an SDK for building connectors to any data accessible over HTTP, allowing users to bring external data into Tableau for analysis and visualization.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/webdataconnector/en-us/index.html
  baseURL: https://[server]
  tags:
  - Connectors
  - Data Integration
  - HTTP
  - JavaScript
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/webdataconnector/en-us/index.html
  - type: Reference
    url: https://tableau.github.io/webdataconnector/docs/api_ref.html
  - type: GitHub
    url: https://github.com/tableau/webdataconnector
  - type: Change Log
    url: https://help.tableau.com/current/api/webdataconnector/en-us/docs/wdc_whats_new.html
  - type: Overview
    url: https://help.tableau.com/current/api/webdataconnector/en-us/docs/wdc_overview.html
  - type: Tutorial
    url: https://tableau.github.io/webdataconnector/docs/wdc_tutorial.html
  - type: Samples
    url: https://tableau.github.io/webdataconnector/docs/wdc_samples.html
- name: Tableau Connector SDK
  description: SDK for developing custom Tableau connectors using ODBC or JDBC drivers, including documentation, example files, a test harness, and a packaging tool for distribution.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://tableau.github.io/connector-plugin-sdk/
  baseURL: https://github.com/tableau/connector-plugin-sdk
  tags:
  - Connectors
  - Custom Connectors
  - JDBC
  - ODBC
  - SDK
  properties:
  - type: Documentation
    url: https://tableau.github.io/connector-plugin-sdk/docs/
  - type: GitHub
    url: https://github.com/tableau/connector-plugin-sdk
  - type: Reference
    url: https://tableau.github.io/connector-plugin-sdk/docs/api-reference
  - type: Examples
    url: https://tableau.github.io/connector-plugin-sdk/docs/example
  - type: Getting Started
    url: https://tableau.github.io/connector-plugin-sdk/docs/
  - type: Testing
    url: https://tableau.github.io/connector-plugin-sdk/docs/tdvt
- name: Tableau Analytics Extensions API
  description: The Analytics Extensions API allows integration of external analytics engines such as Python, R, MATLAB, and data science platforms with Tableau calculations for advanced analytics.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://tableau.github.io/analytics-extensions-api/docs/ae_intro.html
  baseURL: https://[server]
  tags:
  - Analytics
  - Data Science
  - Machine Learning
  - Python
  - R
  properties:
  - type: Documentation
    url: https://tableau.github.io/analytics-extensions-api/docs/ae_intro.html
  - type: Examples
    url: https://tableau.github.io/analytics-extensions-api/docs/ae_example_tabpy.html
  - type: Getting Started
    url: https://tableau.github.io/analytics-extensions-api/docs/ae_connect_desktop.html
  - type: Reference
    url: https://tableau.github.io/analytics-extensions-api/docs/ae_summary.html
  - type: GitHub
    url: https://github.com/tableau/TabPy
- name: Tableau Webhooks
  description: Tableau Webhooks enable event-driven automation by sending HTTP POST notifications to specified URLs when events occur on Tableau Server or Tableau Cloud.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/developer/webhooks/en-us/
  baseURL: https://[server]/api/[api-version]
  tags:
  - Automation
  - Events
  - Notifications
  - Webhooks
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/developer/webhooks/en-us/
  - type: GitHub
    url: https://github.com/tableau/webhooks-docs
  - type: Getting Started
    url: https://help.tableau.com/current/developer/webhooks/en-us/docs/webhooks-get-started.html
  - type: Reference
    url: https://help.tableau.com/current/developer/webhooks/en-us/docs/webhooks-events-payload.html
- name: Tableau VizQL Data Service
  description: The VizQL Data Service provides a programmatic HTTP interface to query published data sources outside of Tableau visualizations, enabling headless data access from any application.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/vizql-data-service/en-us/index.html
  baseURL: https://[server]/api/v1
  tags:
  - Data Access
  - Headless
  - Query
  - REST
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/vizql-data-service/en-us/index.html
  - type: Reference
    url: https://help.tableau.com/current/api/vizql-data-service/en-us/reference/index.html
  - type: Change Log
    url: https://help.tableau.com/current/api/vizql-data-service/en-us/docs/vds_whats_new.html
  - type: GitHub
    url: https://github.com/tableau/VizQL-Data-Service
  - type: Getting Started
    url: https://help.tableau.com/current/api/vizql-data-service/en-us/docs/vds_create_queries.html
  - type: Postman Collection
    url: https://help.tableau.com/current/api/vizql-data-service/en-us/docs/vds_using_postman.html
- name: Tableau Pulse API
  description: The Tableau Pulse API enables programmatic creation, management, and querying of Tableau Pulse metrics and subscriptions, as well as embedding Pulse insights into web applications.
  image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
  humanURL: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_pulse.htm
  baseURL: https://[server]/api/[api-version]
  tags:
  - Analytics
  - Insights
  - Metrics
  - Pulse
  properties:
  - type: Documentation
    url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_pulse.htm
  - type: Embedding
    url: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_pulse.html
  - type: Reference
    url: https://help.tableau.com/current/api/embedding_api/en-us/reference/interfaces/pulse.html
  - type: GitHub
    url: https://github.com/tableau/pulse-api-utilities
name: Tableau
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
type: Contract
image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Tableau is a visual analytics platform transforming the way we use data to solve problems—empowering people and organizations to make the most of their data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

