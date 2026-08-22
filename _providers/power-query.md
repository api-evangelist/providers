---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: REST API for executing Power Query mashups and managing data transformations programmatically.
  name: Power Query REST API
  slug: rest-api
- description: API and language reference for the M formula language used in Power Query for data transformation expressions and custom functions.
  name: Power Query M Formula Language
  slug: m-language
- description: API for building and managing custom data connectors for Power Query using the M language and Connector SDK.
  name: Power Query Connectors API
  slug: connectors-api
- description: API for managing and executing Power Query dataflows in Power Platform and Power BI for self-service ETL workflows.
  name: Power Query Dataflows API
  slug: dataflows-api
- description: Development toolkit for building custom Power Query connectors using Visual Studio Code, including project scaffolding, testing, and packaging of .mez connector files.
  name: Power Query SDK
  slug: sdk
- description: REST API for programmatically executing Power Query M transformations in Microsoft Fabric, enabling integration with Spark notebooks, pipelines, and external applications.
  name: Fabric Power Query Programmatic API
  slug: fabric-api
artifact_total: 27
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/Microsoft/DataConnectors/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-query-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://app.powerbi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-query/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.microsoft.com/en-us/power-platform/products/power-bi/getting-started-with-power-bi
- group: company
  title: ''
  type: Blog
  url: https://powerbi.microsoft.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs/powerquery-docs
- group: operate
  title: ''
  type: Support
  url: https://powerbi.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerbi.microsoft.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://support.fabric.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: Signup
  url: https://www.microsoft.com/en-us/power-platform/products/power-bi/landing/free-account
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/powerquery
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-change-log
created: '2024-01-01'
description: Power Query is a data transformation and mashup engine used across Microsoft products including Excel, Power BI, and Azure. This API collection provides programmatic access to Power Query functionality for data connectivity, transformation, and integration using the M formula language and connector SDK.
features:
- description: Powerful M formula language for complex data transformations including filtering, pivoting, merging, and custom functions.
  name: Data Transformation Engine
- description: Build custom data connectors using the Power Query SDK for connecting to any data source.
  name: Custom Connector Development
- description: Dataflows provide self-service ETL capabilities for business users without IT dependency.
  name: Self-Service ETL
- description: Pre-built connectors for databases, cloud services, files, and web APIs.
  name: 300+ Built-In Connectors
- description: Efficient data loading with incremental refresh policies for large datasets.
  name: Incremental Refresh
- description: Execute Power Query transformations programmatically in Microsoft Fabric pipelines.
  name: Microsoft Fabric Integration
finops:
- name: Power Query Finops
  service_category: API
  slug: power-query-finops
image: /assets/icons/power-query.png
integrations:
- description: Native integration with Power BI for data preparation and visualization workflows.
  name: Power BI
- description: Built-in Power Query editor in Excel for spreadsheet-based data transformation.
  name: Microsoft Excel
- description: Mapping data flows using Power Query transformations in Azure Data Factory.
  name: Azure Data Factory
- description: Programmatic execution of Power Query in Fabric notebooks and pipelines.
  name: Microsoft Fabric
- description: Direct connectivity and query folding optimization for SQL Server databases.
  name: SQL Server
jsonld:
- class_count: 35
  name: Power Query Context
  property_count: 12
  slug: power-query-context
layout: provider
modified: '2026-04-18'
name: Power Query
nav: Providers
network: true
overview: 'Power Query publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Business Intelligence, Data Integration, Data Transformation, ETL, and Microsoft.


  The Power Query catalog on APIs.io includes 1 JSON-LD context.


  Power Query''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Power Query Plans Pricing
  plan_count: 3
  slug: power-query-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Power Query Rate Limits
  slug: power-query-rate-limits
score:
  band: thin
  composite: 36.5
  delta: -0.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 15.5
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 36.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-query/refs/heads/main/screenshots/power-query-2026-06-20T192025.png
security:
- kind: domain-security
  name: Power Query Domain Security
  slug: power-query-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: power-query
tags:
- Business Intelligence
- Data Integration
- Data Transformation
- ETL
- Microsoft
use_cases:
- description: Clean, transform, and shape data from multiple sources for analytics and reporting.
  name: Data Preparation
- description: Build reusable connectors for proprietary or specialized data sources.
  name: Custom Data Connectors
- description: Create scheduled dataflows for automated data refresh and transformation workflows.
  name: Automated Data Pipelines
- description: Integrate data across Power BI, Excel, Azure Data Factory, and Microsoft Fabric.
  name: Cross-Platform Data Integration
- description: Implement data quality rules and transformations for consistent enterprise data.
  name: Data Quality Management
website: https://app.powerbi.com/
---
