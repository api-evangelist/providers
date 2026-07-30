---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sentera Agentic Access
  operation_count: 2
  slug: sentera-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Sentera — 1 operation(s) for graphql.
  name: Sentera GraphQL API
  slug: sentera-graphql-api
artifact_total: 9
collections:
- collection_type: open
  name: Sentera FieldAgent API
  slug: open-sentera
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sentera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentera-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sentera
- group: company
  title: ''
  type: Website
  url: https://sentera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.sentera.com/api/getting_started/introduction.html
- group: commercial
  title: ''
  type: Plans
  url: plans/sentera-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sentera-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sentera-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sentera.com/feed/
created: '2026-06-20'
description: Sentera is a precision-agriculture company building aerial imagery sensors, drones, and the FieldAgent platform for capturing, processing, and analyzing in-season field data. The FieldAgent API is a single-endpoint GraphQL interface (https://api.sentera.com/graphql) that gives customers and integration partners programmatic access to fields, surveys, flight tasks, imagery, mosaics, plot analytics, and orders. Sentera was acquired by John Deere in 2025.
finops:
- name: Sentera Finops
  service_category: Precision Agriculture and Geospatial Analytics
  slug: sentera-finops
graphqls:
- description: Sentera's FieldAgent API is a **GraphQL** API, not a resource-oriented REST API.
  name: Sentera FieldAgent GraphQL API
  slug: sentera-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sentera.png
layout: provider
modified: '2026-06-20'
name: Sentera
nav: Providers
network: true
overview: 'Sentera publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Precision Agriculture, Aerial Imagery, Drones, Sensors, and Analytics.


  Sentera''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Sentera Plans Pricing
  plan_count: 3
  slug: sentera-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Sentera Rate Limits
  slug: sentera-rate-limits
score:
  band: thin
  composite: 38.7
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sentera/refs/heads/main/screenshots/sentera-2026-06-20T193707.png
security:
- kind: authentication
  name: Sentera Authentication
  slug: sentera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sentera Domain Security
  slug: sentera-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sentera
tags:
- Precision Agriculture
- Aerial Imagery
- Drones
- Sensors
- Analytics
- GraphQL
website: https://sentera.com/
---
