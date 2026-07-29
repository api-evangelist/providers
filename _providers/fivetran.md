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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Fivetran Agentic Access
  operation_count: 36
  slug: fivetran-agentic-access
  summary_line: 36 operations · 23 acting
api_count: 9
apis:
- description: The Fivetran REST API allows programmatic management of all platform resources including users, roles, teams, groups, destinations, connections, webhooks, transformations, transformation projects, cer
  name: Fivetran REST API
  slug: fivetran-rest-api
- description: The Connections API from Fivetran — 7 operation(s) for connections.
  name: Fivetran Connections API
  slug: fivetran-connections-api
- description: The Destinations API from Fivetran — 2 operation(s) for destinations.
  name: Fivetran Destinations API
  slug: fivetran-destinations-api
- description: The Groups API from Fivetran — 2 operation(s) for groups.
  name: Fivetran Groups API
  slug: fivetran-groups-api
- description: The Metadata API from Fivetran — 1 operation(s) for metadata.
  name: Fivetran Metadata API
  slug: fivetran-metadata-api
- description: The Roles API from Fivetran — 1 operation(s) for roles.
  name: Fivetran Roles API
  slug: fivetran-roles-api
- description: The Teams API from Fivetran — 1 operation(s) for teams.
  name: Fivetran Teams API
  slug: fivetran-teams-api
- description: The Users API from Fivetran — 2 operation(s) for users.
  name: Fivetran Users API
  slug: fivetran-users-api
- description: The Webhooks API from Fivetran — 5 operation(s) for webhooks.
  name: Fivetran Webhooks API
  slug: fivetran-webhooks-api
artifact_total: 35
collections:
- collection_type: open
  name: Fivetran REST API
  slug: open-fivetran
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fivetran-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fivetran-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fivetran-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fivetran-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fivetran
- group: company
  title: ''
  type: Website
  url: https://www.fivetran.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fivetran.com/docs
- group: docs
  title: ''
  type: REST API Documentation
  url: https://fivetran.com/docs/rest-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fivetran
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/fivetran/fivetran-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/fivetran/claude-sap-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://fivetran.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.fivetran.com/blog/rss.xml
created: '2026-03-27'
description: Fivetran is an automated data integration platform providing pre-built connectors for syncing data from SaaS applications, databases, and APIs into cloud data warehouses. The Fivetran REST API exposes management of users, groups, teams, roles, destinations, connections, transformations, webhooks, certificates, and connector metadata.
features:
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
finops:
- name: Fivetran Finops
  service_category: Data Integration
  slug: fivetran-finops
graphqls:
- description: 'Conceptual GraphQL schema for the Fivetran managed data pipeline service. Fivetran provides automated data integration with 500+ pre-built connectors that sync data from SaaS applications, databases, '
  name: Fivetran GraphQL Schema
  slug: fivetran-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fivetran.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Fivetran
nav: Providers
network: true
overview: 'Fivetran publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Destinations API, Groups API, and 5 more. Tagged areas include Connectors, Data Integration, Data Pipeline, ETL, and SaaS.


  Fivetran''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Fivetran Plans Pricing
  plan_count: 4
  slug: fivetran-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Fivetran Rate Limits
  slug: fivetran-rate-limits
score:
  band: developing
  composite: 42.7
  delta: -0.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fivetran/refs/heads/main/screenshots/fivetran-2026-06-20T181255.png
security:
- kind: authentication
  name: Fivetran Authentication
  slug: fivetran-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fivetran Domain Security
  slug: fivetran-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fivetran Trust Center
  slug: fivetran-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: fivetran
tags:
- Connectors
- Data Integration
- Data Pipeline
- ETL
- SaaS
- Unified API
website: https://www.fivetran.com/
---
