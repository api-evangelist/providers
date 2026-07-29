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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Treasure Data Agentic Access
  operation_count: 31
  slug: treasure-data-agentic-access
  summary_line: 31 operations · 17 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: REST API for configuring and managing bulk load sessions that import data from external sources into Treasure Data.
  name: Treasure Data Bulk Loads API
  slug: treasure-data-bulk-loads-api
- description: REST API for managing users, access control, and authentication within a Treasure Data account.
  name: Treasure Data User API
  slug: treasure-data-user-api
- description: REST API for checking server health and infrastructure status of the Treasure Data platform.
  name: Treasure Data System API
  slug: treasure-data-system-api
- description: JSON-based event ingestion API for submitting data records to Treasure Data from systems that cannot use the JavaScript SDK.
  name: Treasure Data Postback API
  slug: treasure-data-postback-api
- description: REST API for orchestrating and automating data workflows within the Treasure Data platform using Digdag-based workflow engine.
  name: Treasure Workflow API
  slug: treasure-workflow-api
- description: Bulk data import sessions
  name: Treasure Data Bulk Import API
  slug: treasure-data-bulk-import-api
- description: Bulk load sessions from external sources
  name: Treasure Data Bulk Loads API
  slug: treasure-data-bulk-loads-api
- description: Manage output connectors
  name: Treasure Data Connectors API
  slug: treasure-data-connectors-api
- description: Manage Treasure Data databases
  name: Treasure Data Databases API
  slug: treasure-data-databases-api
- description: Submit and manage query jobs
  name: Treasure Data Jobs API
  slug: treasure-data-jobs-api
- description: Identity federation and SSO settings
  name: Treasure Data SSO API
  slug: treasure-data-sso-api
- description: System health and status
  name: Treasure Data System API
  slug: treasure-data-system-api
- description: Manage tables within databases
  name: Treasure Data Tables API
  slug: treasure-data-tables-api
- description: User management
  name: Treasure Data Users API
  slug: treasure-data-users-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/treasure-data-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/treasure-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treasure-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/treasure-data-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.treasure.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.treasure.ai/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/treasure-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/treasure-data-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.treasure.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.treasure.ai/product/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treasure.ai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TreasureData
- group: commercial
  title: ''
  type: Plans
  url: plans/treasure-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/treasure-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/treasure-data-finops.yml
created: '2026-06-13'
description: Enterprise customer data platform (now Treasure AI) with a REST API for managing jobs, databases, tables, bulk import, authentication, and running Presto or Hive queries on big data.
examples:
- key_count: 10
  name: Bulk Import Session
  slug: bulk-import-session
- key_count: 3
  name: Issue Job Response
  slug: issue-job-response
- key_count: 1
  name: List Databases Response
  slug: list-databases-response
- key_count: 1
  name: User List Response
  slug: user-list-response
finops:
- name: Treasure Data Finops
  service_category: ''
  slug: treasure-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treasure-data.png
json_schemas:
- name: BulkImport
  property_count: 10
  slug: bulk-import
- name: Database
  property_count: 5
  slug: database
- name: Job
  property_count: 14
  slug: job
- name: User
  property_count: 14
  slug: user
jsonld:
- class_count: 38
  name: Treasure Data Context
  property_count: 2
  slug: treasure-data-context
layout: provider
modified: '2026-06-13'
name: Treasure Data
nav: Providers
network: true
overview: 'Treasure Data publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Bulk Loads API, System API, Bulk Import API, and 8 more. Tagged areas include Customer Data Platform, CDP, Big Data, Data Warehouse, and Hive.


  The Treasure Data catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Treasure Data''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Treasure Data Plans Pricing
  plan_count: 3
  slug: treasure-data-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 17
  name: Treasure Data Rate Limits
  slug: treasure-data-rate-limits
rules:
- name: Treasure Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: treasure-data-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.0
  delta: -4.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.9
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/treasure-data/refs/heads/main/screenshots/treasure-data-2026-06-20T195643.png
security:
- kind: authentication
  name: Treasure Data Authentication
  slug: treasure-data-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Treasure Data Domain Security
  slug: treasure-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Treasure Data Trust Center
  slug: treasure-data-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: treasure-data
tags:
- Customer Data Platform
- CDP
- Big Data
- Data Warehouse
- Hive
- Presto
- Enterprise
- AI
- Marketing
- Analytics
website: https://www.treasure.ai/
---
