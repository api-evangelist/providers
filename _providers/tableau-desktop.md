---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Tableau Desktop Agentic Access
  operation_count: 25
  slug: tableau-desktop-agentic-access
  summary_line: 25 operations · 15 acting
api_count: 12
apis:
- description: Build dashboard extensions that enable users to interact with data from other applications directly in Tableau dashboards.
  name: Tableau Extensions API
  slug: extensions-api
- description: Create, read, update, and delete data in .hyper files for use in Tableau Desktop and Server with high-performance data extract capabilities.
  name: Tableau Hyper API
  slug: hyper-api
- description: Embed Tableau visualizations into web applications using modern web components with v3 of the Embedding API.
  name: Tableau Embedding API
  slug: embedding-api
- description: Discover and query metadata about Tableau content using GraphQL, including workbooks, data sources, flows, and lineage information.
  name: Tableau Metadata API
  slug: metadata-api
- description: Python library that provides a convenient wrapper for the Tableau Server REST API for automation and integration workflows.
  name: Tableau Server Client (Python)
  slug: server-client-python
- description: Sign in and sign out operations.
  name: Tableau Desktop Authentication API
  slug: tableau-desktop-authentication-api
- description: Manage and refresh published data sources.
  name: Tableau Desktop Data Sources API
  slug: tableau-desktop-data-sources-api
- description: Manage projects on a site.
  name: Tableau Desktop Projects API
  slug: tableau-desktop-projects-api
- description: Server information.
  name: Tableau Desktop Server API
  slug: tableau-desktop-server-api
- description: Manage Tableau sites.
  name: Tableau Desktop Sites API
  slug: tableau-desktop-sites-api
- description: Manage users on a site.
  name: Tableau Desktop Users API
  slug: tableau-desktop-users-api
- description: Manage and download workbooks.
  name: Tableau Desktop Workbooks API
  slug: tableau-desktop-workbooks-api
artifact_total: 37
collections:
- collection_type: open
  name: Tableau REST API
  slug: open-tableau-desktop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tableau-desktop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tableau-desktop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tableau-desktop-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.tableau.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.tableau.com/developer/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tableau.com/developer/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.tableau.com/about/blog/developers
- group: operate
  title: ''
  type: Support
  url: https://www.tableau.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tableau.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tableau.com/privacy
- group: learn
  title: ''
  type: Training
  url: https://trailhead.salesforce.com/content/learn/modules/tableau-developer-platform/get-started-with-the-tableau-developer-platform
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tableau
created: '2024-01-01'
description: APIs and integration points for Tableau Desktop, a data visualization and business intelligence platform from Salesforce. Tableau provides REST APIs, embedding APIs, extension APIs, and SDK tools for building custom visualizations, automating server operations, and extending analytics capabilities.
features:
- description: Full CRUD operations on Tableau Server and Cloud resources including workbooks, data sources, and users.
  name: REST API Management
- description: Build custom interactive extensions that integrate third-party data and functionality into dashboards.
  name: Dashboard Extensions
- description: Create and manage .hyper data extract files with the Hyper API for optimized data loading.
  name: High-Performance Data Extracts
- description: Embed interactive Tableau visualizations in web applications with modern web components.
  name: Embedded Analytics
- description: Query content metadata and data lineage using GraphQL for governance and impact analysis.
  name: Metadata and Lineage
- description: Automate Tableau Server operations with the Python Server Client library.
  name: Python Automation
finops:
- name: Tableau Desktop Finops
  service_category: API
  slug: tableau-desktop-finops
graphqls:
- description: Discover and query metadata about Tableau content using GraphQL, including workbooks, data sources, flows, and lineage information.
  name: Tableau Desktop GraphQL API
  slug: tableau-desktop-graphql
image: /assets/icons/tableau-desktop.png
integrations:
- description: Native integration with Salesforce CRM for embedded analytics and data connectivity.
  name: Salesforce
- description: High-performance data connectivity with Snowflake cloud data warehouse.
  name: Snowflake
- description: Cloud deployment on AWS with S3, Redshift, and Athena data source support.
  name: AWS
- description: Azure integration with Synapse Analytics, Blob Storage, and Azure Active Directory.
  name: Azure
- description: TabPy server for executing Python scripts in Tableau calculated fields.
  name: Python
- description: Collaboration integration for sharing and subscribing to Tableau content in Slack.
  name: Slack
layout: provider
modified: '2026-05-19'
name: Tableau Desktop
nav: Providers
network: true
overview: 'Tableau Desktop publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Data Sources API, Projects API, and 4 more. Tagged areas include Analytics, Business Intelligence, Data Visualization, and Desktop Application.


  Tableau Desktop''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, training material, and 5 more developer resources.'
plans:
- name: Tableau Desktop Plans Pricing
  plan_count: 3
  slug: tableau-desktop-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Tableau Desktop Rate Limits
  slug: tableau-desktop-rate-limits
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.1
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tableau-desktop/refs/heads/main/screenshots/tableau-desktop-2026-06-20T194845.png
security:
- kind: authentication
  name: Tableau Desktop Authentication
  slug: tableau-desktop-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tableau Desktop Domain Security
  slug: tableau-desktop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tableau-desktop
tags:
- Analytics
- Business Intelligence
- Data Visualization
- Desktop Application
use_cases:
- description: Embed interactive dashboards and visualizations into customer-facing web applications.
  name: Embedded Analytics
- description: Automate data extract creation and refresh workflows using the Hyper API and REST API.
  name: Data Pipeline Automation
- description: Migrate workbooks and data sources between Tableau Server environments programmatically.
  name: Content Migration
- description: Build write-back forms, custom controls, and third-party integrations as dashboard extensions.
  name: Custom Dashboard Extensions
- description: Track data lineage and content dependencies using the Metadata API for impact analysis.
  name: Data Governance
website: https://www.tableau.com/developer
---
